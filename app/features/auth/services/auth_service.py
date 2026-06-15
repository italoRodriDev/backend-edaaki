from datetime import datetime

import firebase_admin
from firebase_admin import auth
from app.features.profile.repositories.profile_repo import IProfileRepository
from app.features.profile.models.profile_model import ProfileModel 
from app.features.auth.schemas.auth_schemas import RegisterRequest 

class AuthService:
    def __init__(self, user_repo: IProfileRepository):
        self.user_repo = user_repo

    async def sync_firebase_user(self, decoded_token: dict) -> ProfileModel:
        email = decoded_token.get("email")
        name = decoded_token.get("name", "Usuário")
        picture = decoded_token.get("picture", None)
        firebase_uid = decoded_token.get("uid") 

        if not email:
            raise ValueError("Token não contém um e-mail válido.")

        user = await self.user_repo.find_by_email(email)

        if user:
            if picture and user.logo != picture:
                user.logo = picture
                await self.user_repo.update(user.id, {"logo": picture})
            return user
        else:
            new_user_data = {
                "email": email,
                "name": name,
                "logo": picture,
                "status": "ATIVO",
                "role": "USER",
                "type": "CLIENTE",
                "access_token": firebase_uid,
                "password": "SOCIAL_LOGIN"  # Preenchido para atender a NOT NULL
            }
            return await self.user_repo.save(new_user_data)

    async def register_with_email_and_password(self, data: RegisterRequest) -> ProfileModel:
        print("DEBUG: Entrou no método de registro")
        
        # 1. Verificação SQL
        existing_user = await self.user_repo.find_by_email(data.email)
        if existing_user:
            raise ValueError("Este e-mail já está em uso no sistema.")

        # 2. Criação Firebase
        try:
            print("DEBUG: Chamando auth.create_user")
            firebase_user = auth.create_user(
                email=data.email,
                password=data.password,
                display_name=data.name
            )
            print(f"DEBUG: Firebase criou user: {firebase_user.uid}")
        except Exception as e:
            print(f"DEBUG: ERRO NO FIREBASE: {str(e)}")
            raise ValueError(f"Erro no Firebase: {str(e)}")

        # 3. Persistência SQL
        try:
            print("DEBUG: Montando dicionário SQL")
            currentDate = datetime.now()
            new_user_data = {
                "name": data.name,
                "email": data.email,
                "password": "FIREBASE_MANAGED",
                "cpf_cnpj": data.cpf_cnpj,
                "cep": data.cep,
                "lat": data.lat,
                "long": data.long,
                "address": data.address,
                "city": data.city,
                "state": data.state,
                "country": data.country,
                "region": data.region,
                "type": data.type,
                "code_flat": data.code_flat,
                "status": "ATIVO",
                "access_token": firebase_user.uid,
                "role": "USER",
                "gender": data.gender,
                "civil_state": data.civil_state,
                "phone": data.phone,
                "birth_date": data.birth_date.replace(tzinfo=None) if data.birth_date else None,
                "fantasy_name": data.fantasy_name,
                "logo": data.logo,
                "created_at": currentDate,
                "updated_at": currentDate
            }
            
            print("DEBUG: Chamando user_repo.save_user")
            return await self.user_repo.save_user(new_user_data)
            
        except Exception as e:
            print(f"DEBUG: ERRO CRÍTICO NO SQL: {str(e)}")
            raise ValueError(f"Erro ao salvar no banco: {str(e)}")

    async def generate_reset_password_link(self, email: str) -> str:
        try:
            return auth.generate_password_reset_link(email)
        except firebase_admin.auth.UserNotFoundError:
            raise ValueError("Usuário não encontrado no Firebase.")
        except Exception as e:
            raise ValueError(f"Erro ao gerar link de resete: {str(e)}")
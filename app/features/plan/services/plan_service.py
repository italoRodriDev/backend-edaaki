from app.features.plan.schemas.plan_schemas import PlanCreate
from app.features.plan.interfaces.plan_interface import IPlanRepository

class PlanService:
    def __init__(self, repo: IPlanRepository):
        self.repo = repo

    async def list_plans(self, limit: int = 100):
        return await self.repo.get_all(limit=limit)

    async def create_plan(self, data: PlanCreate):
        # Transforma o schema em dicionário para o repositório
        plan_dict = data.model_dump()
        return await self.repo.create(plan_dict)

    async def delete_plan(self, plan_id: int) -> bool:
        return await self.repo.delete(plan_id)
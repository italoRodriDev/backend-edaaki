from fastapi import APIRouter
from app.features.profile.router.profile_router import router as profiles_router
from app.features.product.router.product_router import router as product_router 
from app.features.category.router.category_router import router as category_router
from app.features.privacity.router.privacity_router import router as privacity_router
from app.features.contact.router.contact_router import router as contact_router
from app.features.address.router.address_router import router as address_router
from app.features.delivery.router.delivery_router import router as delivery_router
from app.features.order.router.order_router import router as order_router
from app.features.cards.router.credit_card_router import router as cards_router
from app.features.plan.router.plan_router import router as plan_router

api_router = APIRouter()

api_router.include_router(router=profiles_router)
api_router.include_router(router=product_router)
api_router.include_router(router=category_router)
api_router.include_router(router=privacity_router)
api_router.include_router(router=contact_router)
api_router.include_router(router=address_router)
api_router.include_router(router=delivery_router)
api_router.include_router(router=order_router)
api_router.include_router(router=cards_router)
api_router.include_router(router=plan_router)
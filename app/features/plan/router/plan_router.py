from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db_session

from app.features.plan.schemas.plan_schemas import PlanCreate, PlanResponse
from app.features.plan.services.plan_service import PlanService
from app.features.plan.repositories.plan_repo import SQLPlanRepository

router = APIRouter(prefix="/plans", tags=["Plans"])

# Injeção de dependência do Service
def get_plan_service(db: AsyncSession = Depends(get_db_session)):
    repo = SQLPlanRepository(db)
    return PlanService(repo)

@router.get("/", response_model=list[PlanResponse])
async def list_plans(service: PlanService = Depends(get_plan_service)):
    return await service.list_plans()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PlanResponse)
async def create_plan(data: PlanCreate, service: PlanService = Depends(get_plan_service)):
    return await service.create_plan(data)

@router.delete("/{plan_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_plan(plan_id: int, service: PlanService = Depends(get_plan_service)):
    deleted = await service.delete_plan(plan_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Plano não encontrado.")
    return None
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.features.plan.models.plan_model import PlanModel

class SQLPlanRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self, limit: int = 100):
        stmt = select(PlanModel).limit(limit)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def create(self, plan_data: dict):
        new_plan = PlanModel(**plan_data)
        self.session.add(new_plan)
        await self.session.commit()
        await self.session.refresh(new_plan)
        return new_plan
    
    async def delete(self, plan_id: int) -> bool:
        stmt = delete(PlanModel).where(PlanModel.id == plan_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount > 0
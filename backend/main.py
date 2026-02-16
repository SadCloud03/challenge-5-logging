from fastapi import FastAPI, Depends, Header, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db import engine, Base
from deps import get_db
from models import Service, Token, Log
from schemas import LogIn

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/logs")
async def create_log(
    log_in: LogIn,
    token: str = Header(..., alias="Authorization"),
    session: AsyncSession = Depends(get_db)
):
    token = token.replace("Bearer ", "")

    result = await session.execute(
        select(Token).where(Token.token == token, Token.is_active == True)
    )
    token_obj = result.scalar_one_or_none()

    if not token_obj:
        raise HTTPException(status_code=401, detail="Invalid token")

    new_log = Log(
        service_id=token_obj.service_id,
        level=log_in.level,
        message=log_in.message,
        extra=log_in.extra
    )

    session.add(new_log)
    await session.commit()

    return {"status": "ok"}


@app.get("/logs")
async def get_logs(
    service: str | None = Query(None),
    level: str | None = Query(None),
    limit: int = Query(100, le=500),
    db: AsyncSession = Depends(get_db)
):
    query = select(Log).order_by(Log.created_at.desc()).limit(limit)

    if level:
        query = query.where(Log.level == level)

    if service:
        query = query.join(Service).where(Service.name == service)

    res = await db.execute(query)
    logs = res.scalars().all()

    return logs

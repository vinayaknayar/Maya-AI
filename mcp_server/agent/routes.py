from fastapi import APIRouter
from fastapi.concurrency import run_in_threadpool
from .schemas import AgentMessage
from .service import process_message

router = APIRouter(prefix="/agent", tags=["agent"])



@router.post("/message")
async def agent_message(payload: AgentMessage):
    reply = await process_message(
        payload.user_id,
        payload.message
    )
    return {"reply": reply}
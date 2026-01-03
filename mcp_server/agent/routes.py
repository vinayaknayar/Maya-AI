from fastapi import APIRouter
from .schemas import AgentMessage
from .service import process_message

router = APIRouter(prefix="/agent", tags=["agent"])

@router.post("/message")
async def agent_message(payload: AgentMessage):
    reply = await process_message(
        user_id=payload.user_id,
        message=payload.message
    )
    return {"reply": reply}
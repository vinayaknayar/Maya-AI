from sqlmodel import Session, select
from mcp_server.database import engine
from mcp_server.models import Message

MAX_MEMORY = 8  # last N messages

def load_memory(user_id: int):
    with Session(engine) as session:
        messages = session.exec(
            select(Message)
            .where(Message.user_id == user_id)
            .order_by(Message.created_at.desc())
            .limit(MAX_MEMORY)
        ).all()
    # reverse → oldest → newest
    return list(reversed(messages))

def save_message(user_id: int, role: str, content: str):
    with Session(engine) as session:
        msg = Message(
            user_id=user_id,
            role=role,
            content=content
        )
        session.add(msg)
        session.commit()

from pydantic import BaseModel

class AgentMessage(BaseModel):
    user_id: int
    message: str
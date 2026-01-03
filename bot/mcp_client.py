import httpx
from config import MCP_SERVER_URL


async def send_message_to_mcp(user_id: int, message: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{MCP_SERVER_URL}/agent/message",
            json={
                "user_id": user_id,
                "message": message
            },
            timeout=30
        )
        response.raise_for_status()
        return response.json()

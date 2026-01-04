import os
from dotenv import load_dotenv
load_dotenv()
from mcp_server.agent.memory import MAX_MEMORY

SYSTEM_PROMPT = """
You are Maya, a calm, empathetic AI assistant.
You help users think clearly, reflect, and take small positive steps.
You remember context from the conversation.
Respond concisely but thoughtfully.
"""

# Gemini version (can swap to OpenAI easily)
from google import genai
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def call_llm(messages: list[dict]) -> str:
    # Gemini expects a single string prompt, so we concatenate
    prompt = "\n".join([m["content"] for m in messages])
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()


from .llm import call_llm, SYSTEM_PROMPT
from .memory import load_memory, save_message

import asyncio

async def process_message(user_id: int, message: str) -> str:
    # 1️⃣ Load memory
    memory = load_memory(user_id)

    # 2️⃣ Build prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for m in memory:
        messages.append({
            "role": m.role,
            "content": m.content
        })
    messages.append({"role": "user", "content": message})

    # 3️⃣ Save user message
    save_message(user_id, "user", message)

    # 4️⃣ Call LLM (sync, so use threadpool)
    from fastapi.concurrency import run_in_threadpool
    reply = await run_in_threadpool(call_llm, messages)

    # 5️⃣ Save assistant message
    save_message(user_id, "assistant", reply)

    return reply
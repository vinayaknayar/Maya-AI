from fastapi import FastAPI
from .database import init_db
from .auth import router as auth_router
from .models import Task
from .tools import router as tools_router
from .agent.routes import router as agent_router
from contextlib import asynccontextmanager


####
#Creates FastAPI app
#Runs DB initialization on startup
#Includes the auth router
#Adds /healthz endpoint
####

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Maya MCP Server",
    lifespan=lifespan
)


# Routers
app.include_router(auth_router, prefix="/auth")
app.include_router(tools_router)
app.include_router(agent_router)

@app.get("/healthz")
def health():
    return {"status": "ok"}
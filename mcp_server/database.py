from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from mcp_server.models import Message  # Ensure Message is imported for table creation
from sqlmodel import SQLModel


DATABASE_URL = "sqlite:///./mcp_server/mcp.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def init_db():
    SQLModel.metadata.create_all(engine)

# Dependency – used by FastAPI to inject DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

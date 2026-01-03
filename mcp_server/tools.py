from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import JournalEntry, User

router = APIRouter(prefix="/tools", tags=["tools"])

@router.post("/save-journal")
def save_journal(user_id: int, text: str, db: Session = Depends(get_db)):
    entry = JournalEntry(user_id=user_id, content=text)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {"status": "saved", "entry_id": entry.id}

@router.get("/journal-history")
def journal_history(user_id: int, db: Session = Depends(get_db)):
    entries = db.query(JournalEntry).filter_by(user_id=user_id).all()
    return {"entries": [e.content for e in entries]}
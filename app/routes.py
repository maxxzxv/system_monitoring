from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Metric

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Metrics(BaseModel):
    cpu: float
    memory: float
    disk: float

@router.post("/metrics")
def create_metric(metrics: Metrics, db: Session = Depends(get_db)):
    db_metric = Metric(cpu=metrics.cpu, memory=metrics.memory, disk=metrics.disk)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return {"status": "ok", "id": db_metric.id}
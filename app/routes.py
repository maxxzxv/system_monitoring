from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Metric
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Metrics(BaseModel):
    cpu: float = Field(..., ge=0, le=100)
    memory: float = Field(..., ge=0, le=100)
    disk: float = Field(..., ge=0, le=100)

@router.post("/metrics")
def create_metric(metrics: Metrics, db: Session = Depends(get_db)):
    db_metric = Metric(cpu=metrics.cpu, memory=metrics.memory, disk=metrics.disk)
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)

    logger.info(f"Metrics stored, id={db_metric.id}")

    return {"status": "ok", "id": db_metric.id}
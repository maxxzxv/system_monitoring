from fastapi import FastAPI
from .database import SessionLocal, engine, Base
from .models import Metric
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Monitoring API running"}

from fastapi import Depends, FastAPI

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.dependencies import get_db

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cloud Data Platform API"}


@app.get("/health/database")
def database_health(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {
    "database": "connected",
    "result": result.scalar(),
     }
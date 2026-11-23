from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import engine, Base
from app import models
from app.database import get_db

app = FastAPI(title='Expense Management API', version='1.0.0')

@app.on_event("startup")
def create_database_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
    
@app.get('/')
def root():
    return {"message": "Welcome to the Expense Management API"}

@app.get('/health')
def health():
    return {"status": "healthy"}

@app.get('/health/db')
def check_database(db: Session = Depends(get_db)):
    try:
        # Execute a simple query to check database connectivity
        db.execute(text("SELECT 1"))
        return {
            'status': 'success',
            "message": "Database connection is healthy"
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")
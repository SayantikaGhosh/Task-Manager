from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user
from app.routes import auth

app = FastAPI()

Base.metadata.create_all(bind=engine) #creates all table define using Base

@app.get("/")
def read_root():
    return {"message":"Hey Bitches!!!!!!"}

app.include_router(auth.router)
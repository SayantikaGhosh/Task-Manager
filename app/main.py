from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user, task
from app.routes import auth, tasks



app = FastAPI()

Base.metadata.create_all(bind=engine) #creates all table define using Base

@app.get("/")
def read_root():
    return {"message":"Hello!!!!!!"}

app.include_router(auth.router)


app.include_router(tasks.router)
from fastapi import FastAPI
from routes import sync
from db.session import Base, engine
from models import sync_link

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sync.router)

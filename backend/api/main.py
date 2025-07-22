# main.py
from fastapi.middleware.cors import CORSMiddleware

import loguru
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .endpoints import pow, fibo, factorial
from .db import Base, engine
from fastapi import Depends
from sqlalchemy.orm import Session
from .db import get_db, Computation, DeletedItem
from .endpoints.util import Cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    loguru.logger.info("Started lifespan", app)
    app.state.cache = Cache()

    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routing part
app.include_router(pow.router)
app.include_router(fibo.router)
app.include_router(factorial.router)

# persistent db - SQLite
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.get("/db")
def get_db_contents(db: Session = Depends(get_db)):
    computations = db.query(Computation).all()
    deleted_items = db.query(DeletedItem).all()

    return {
        "computations": [c.__dict__ for c in computations],
        "deleted_items": [d.__dict__ for d in deleted_items],
    }

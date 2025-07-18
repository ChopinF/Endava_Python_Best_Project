# main.py
from fastapi import FastAPI

from api.database import init_db
init_db()
from api.endpoints import pow, fibo, factorial
from api.database import SessionLocal, RequestLog
def log_request(operation: str, input_data: str, result: str, api_key: str):
    db = SessionLocal()
    try:
        log = RequestLog(operation=operation, input=input_data, output=result, api_key=api_key)
        db.add(log)
        db.commit()
    finally:
        db.close()


from .endpoints import pow, fibo, factorial
from .db import Base, engine
from fastapi import Depends
from sqlalchemy.orm import Session
from .db import get_db, Computation, DeletedItem



app = FastAPI()

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

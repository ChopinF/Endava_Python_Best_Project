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

app = FastAPI()

app.include_router(pow.router)
app.include_router(fibo.router)
app.include_router(factorial.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

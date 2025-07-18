from api.database import SessionLocal, RequestLog

db = SessionLocal()
rows = db.query(RequestLog).all()

if not rows:
    print("⚠️ No entries found in the database.")
else:
    for row in rows:
        print(f"{row.id} | {row.operation} | {row.input} → {row.output} | API: {row.api_key}")
db.close()

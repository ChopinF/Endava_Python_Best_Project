from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///requests.db"

Base = declarative_base()

class RequestLog(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    input = Column(String)
    output = Column(String)
    api_key = Column(String)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the table on startup
def init_db():
    Base.metadata.create_all(bind=engine)

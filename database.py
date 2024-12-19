from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 



load_dotenv()

DB_URL = os.environ['DB_URL']

sql_engine_connector = create_engine(url=DB_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=sql_engine_connector , autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
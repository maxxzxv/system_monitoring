from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database url format "postgresql://username:password@hostname:port/database"
# change depending on your needs
DATABASE_URL = "postgresql://monitoring_user:mntusr-pass-3517@localhost:5432/monitoring_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
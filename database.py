from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit = False, autoflash=False, bin=engine)

class Base(DeclarativeBase):
    pass

Base = declarative_base()

class Usuario(Base):
    __tablename__="usuarios"

def create_tables():
    Base.metadata.create_all(bin=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
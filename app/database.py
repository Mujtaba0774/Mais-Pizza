from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from database import engine,Base
from models import User,Order

engine=create_engine("postgresql://postgres:asdfghjkl@localhost//pizza_delivery",echo=True)
Base=declarative_base()
Session=sessionmaker()
Base.metadata.create_all(bind=engine)
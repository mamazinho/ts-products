from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

class Settings:

    Engine = create_engine('postgresql+psycopg2://postgres:olist123@localhost:5432/postgres', echo=False)
    Base = declarative_base()

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from settings import SQL_CONNECTION_STRING

engine = create_engine(SQL_CONNECTION_STRING)
Base = declarative_base()


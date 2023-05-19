from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('postgresql+psycopg2://web:qwerty@localhost:5432/postgres')

Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base.metadata.drop_all(engine)

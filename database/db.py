import configparser
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URI:  postgresql://username:koss@domain:port/database
file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

# username = config.get('DEV_DB', 'USER')
# password = config.get('DEV_DB', 'PASSWORD')
# domain = config.get('DEV_DB', 'DOMAIN')
# port = config.get('DEV_DB', 'PORT')
# database = config.get('DEV_DB', 'DB_NAME')

# URI = f"postgresql+psycopg2://{username}:{password}@{domain}:{port}/{database}"

engine = create_engine('postgresql+psycopg2://postgres:qwerty@localhost:5432/postgres')
DBSession = sessionmaker(bind=engine)
session = DBSession()

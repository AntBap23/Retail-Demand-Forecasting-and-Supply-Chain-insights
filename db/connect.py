from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

def get_engine():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    db = os.getenv('DB_NAME')
    host = 'localhost'
    port = 5432

    return create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')

import sqlalchemy
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
import os

host = os.getenv("HOST")
user = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
db = os.getenv("DATABASE")

connection_uri = f"mysql+pymysql://{user}:{password}@{host}/{db}"
engine = create_engine(
    connection_uri,
    connect_args={"ssl": {"ca": "/etc/ssl/cert.pem"}},
)


def load_database():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = [r._asdict() for r in result.all()]
    return jobs

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi_zero.settings import Setting

engine = create_engine(Setting().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session

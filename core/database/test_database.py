import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database import get_db
from main import app
from core.models.models import Base
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("TEST_SQLALCHEMY_DATABASE_URL")
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    # Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db

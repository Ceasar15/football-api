import pytest
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker
from core.database.database import get_db, Base
from core.models.models import User
from main import app

SQLALCHEMY_DATABASE_URL = os.getenv("TEST_SQLALCHEMY_DATABASE_URL")
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


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
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-8000}
alembic revision --autogenerate -m "database creatonion"
alembic upgrade head
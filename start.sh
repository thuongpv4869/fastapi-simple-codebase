export PYTHONPATH=$PWD

# migrate db
alembic upgrade head

# run app
cd app
uvicorn main:app --reload

#!/bin/bash

export PYTHONPATH=$PWD

# migrate db
alembic upgrade head

# run fake data script
python app/scripts/fake_data.py
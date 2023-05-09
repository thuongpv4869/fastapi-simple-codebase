#!/bin/bash

export PYTHONPATH=$PWD

# migrate db
alembic upgrade head
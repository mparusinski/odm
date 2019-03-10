#!/usr/bin/env bash

source venv/bin/activate

export FLASK_APP=odm
export FLASK_DEBUG=1

flask run
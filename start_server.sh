#!/usr/bin/env bash

source venv/bin/activate

export FLASK_APP=view.route_entry
export FLASK_DEBUG=1

flask run
#!/bin/sh

pip install bottle psycopg2-binary redis
python -u sender.py

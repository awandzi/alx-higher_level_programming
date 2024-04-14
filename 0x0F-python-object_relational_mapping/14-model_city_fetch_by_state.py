#!/usr/bin/python3
"""Module that retrieves and prints a list of cities with their\
        associated states from a MySQL database using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials


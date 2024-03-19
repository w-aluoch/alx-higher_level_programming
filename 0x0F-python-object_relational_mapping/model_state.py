#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script_name.py username password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database_name}", pool_pre_ping=True)
    Base.metadata.create_all(engine)


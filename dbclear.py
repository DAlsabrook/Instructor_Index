#!/usr/bin/python3
"""
Script to drop all tables from the database using DBStorage.
"""

from models import storage
from models.base_model import Base

def drop_all_tables():
    """Drops all tables managed by SQLAlchemy Base metadata."""
    storage.reload()
    Base.metadata.drop_all(bind=storage.get_engine())
    print("Dropped all tables")

if __name__ == "__main__":
    drop_all_tables()

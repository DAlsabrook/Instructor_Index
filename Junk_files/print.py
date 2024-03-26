#!/usr/bin/python3
from models.engine.db_storage import DBStorage
from models.place import Place
from models.state import State
from models.city import City

def print_tables():
    session = DBStorage()
    session.reload()

    # Assuming DBStorage session provides access to the ORM session
    orm_session = session.get_session()

    # fetching all State instances
    states = orm_session.query(State).all()
    print("States:\n\t", end="")
    for state in states:
        print(f"{state.name}", end=" | ")

    # Fetching all City instances
    cities = orm_session.query(City).all()
    print()
    print("Cities:\n\t", end="")
    for city in cities:
        print(f"{city.name}", end=" | ")

    # Fetching all Place instances
    places = orm_session.query(Place).all()

    print("\n\nPlaces and their amenities:")
    for place in places:
        print(f"\t-{place.name} in {place.cities.name}, {place.cities.state.name}\n\t\tamenities:", end=" | ")
        for amenity in place.amenities:
            print(amenity.name, end=" | ")
        print("\n")

    # Other table prints...

if __name__ == "__main__":
    print_tables()

#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity

### This file will create a state, city, user, and multiple places that should
### be tied to multiple amenities (many 2 many relationship)

## Works for db but error for fs (still creates json and adds objs to it)
# Traceback (most recent call last):
#   File "/com.docker.devenvironments.code/./create_data.py", line 69, in <module>
#     create_tables()
#   File "/com.docker.devenvironments.code/./create_data.py", line 53, in create_tables
#     place_0.amenities.append(wifi)
#   File "/com.docker.devenvironments.code/models/place.py", line 74, in amenities
#     if amenity.place_id == self.id:
# AttributeError: 'Amenity' object has no attribute 'place_id'
def create_tables():
    # creation of a State
    california = State(name="California")
    california.save()
    oklahoma = State(name="Oklahoma")
    oklahoma.save()
    texas = State(name="Texas")
    texas.save()

    # creation of a City
    san_fran = City(state_id=california.id, name="San Francisco")
    san_fran.save()
    tulsa = City(state_id=oklahoma.id, name="Tulsa")
    tulsa.save()
    austin = City(state_id=texas.id, name="Austin")
    austin.save()
    # creation of a User
    user = User(email="john@snow.com", password="johnpwd")
    user.save()
    # creation of 2 Places
    place_0 = Place(user_id=user.id, city_id=tulsa.id, name="South House")
    place_0.save()
    place_1 = Place(user_id=user.id, city_id=tulsa.id, name="Riverside House")
    place_1.save()
    place_2 = Place(user_id=user.id, city_id=austin.id, name="Midtown House")
    place_2.save()
    place_3 = Place(user_id=user.id, city_id=san_fran.id, name="Downtown loft")
    place_3.save()
    # creation of 3 various Amenity
    wifi = Amenity(name="wifi")
    wifi.save()
    tv = Amenity(name="tv")
    tv.save()
    patio = Amenity(name="patio")
    patio.save()
    food = Amenity(name="food")
    food.save()
    # link place_1 with 2 amenities
    from models.__init__ import storage_t
    if storage_t == "db":
        print("Storage: Database")
        place_0.amenities.append(wifi)
        place_0.amenities.append(food)
        place_0.amenities.append(patio)
        # link place_2 with 3 amenities
        place_1.amenities.append(food)

        place_2.amenities.append(patio)
        place_2.amenities.append(tv)

        place_3.amenities.append(wifi)
        place_3.amenities.append(tv)
    else:
        print("Storage: File storage")
    place_2.save()
    place_3.save()
    place_0.save()
    place_1.save()
    storage.save()
    print("Count method:\n\tAll objects: {}".format(storage.count()))
    print("\tState objects: {}".format(storage.count(State)))

    first_state_id = list(storage.all(State).values())[0].id
    print("Get Method:\n\tFirst state: {}".format(storage.get(State, first_state_id)))

if __name__ == "__main__":
    create_tables()
    print("Data created.")

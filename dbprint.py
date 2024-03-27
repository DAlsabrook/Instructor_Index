#!/usr/bin/python3
from models.engine.storage import DBStorage
from models.school import School

def print_tables():
    session = DBStorage()
    session.reload()

    # Assuming DBStorage session provides access to the ORM session
    orm_session = session.get_session()

    # fetching all schools instances
    schools = orm_session.query(School).all()
    print("Schools:")
    for school in schools:
        print(f"\t--{school.name}\n\t   Overall Rating: {school.overall}")
        print("\t\tInstructors:")
        for instructor in school.instructors:
            print(f"\t\t\t{instructor.first_name} {instructor.last_name} - overall: {instructor.overall}")
            print("\t\t\t\tApproachability\t\t Availability\t\t  Helpfulness")
            for rating in instructor.ratings:
                print(f"\t\t\t\t\t{rating.approachability}\
                      {rating.availability}\
                        {rating.helpfulness}")
        print()


if __name__ == "__main__":
    print_tables()

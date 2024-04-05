#!/usr/bin/python3
"""Module to create test data in database"""
from dbprint import print_tables

def create_tables():
    """Create data"""
    from models.school import School
    from models.instructor import Instructor
    from models.rating import Instructor_Rating, School_Rating
    import random

    # Number of rating to create per school
    ratings_per_school = 3
    # Number of instructors to create per school
    instructor_per_school = 6
    # Ratings per instructor
    rating_per_instructor = 3

    # CREATE SCHOOLS
    atlas = School(name="Atlas")
    atlas.save()

    ou = School(name="Oklahoma University")
    ou.save()

    osu = School(name="Oklahoma State University")
    osu.save()

    tcc = School(name="Tulsa Community College")
    tcc.save()

    schools = [atlas, ou, osu, tcc]
    first_names = [
        "Tim", "Olivia", "Ethan", "Sophia", "Mason", "Ava",
        "Charlotte", "Liam", "Isabella", "Noah", "Emma", "James",
        "Amelia", "Logan", "Mia", "Benjamin"
    ]

    last_names = [
        "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis",
        "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson",
        "White", "Harris", "Martin", "Thompson"
    ]
    school_text = ["This school is excellent in terms of facilities and student life.",
                   "School has it's positives and negatives but im about it",
                   "It is a school",
                   "Could be better",
                   "Love this school and everything they have to offer!",
                   "Life Changing"]
    instructor_text = ["This instructor is knowledgeable and engaging in their teaching.",
                       "They are a teachers teacher",
                       "I wouldnt want anyone else!",
                       "They reached out to me and really made an effort",
                       "LOVE!"]


    for school in schools:
        # Create ratings for each school
        for _ in range(ratings_per_school):
            rating = School_Rating(
                school_id=school.id,
                review=random.choice(school_text),
                facilities=random.randint(3, 5),
                parking=random.randint(3, 5),
                internet=random.randint(3, 5),
                social=random.randint(3, 5),
                happiness=random.randint(3, 5)
            )
            rating.save()

        # Create instructors for each school
        for i in range(instructor_per_school):
            instructor = Instructor(
                first_name=f"{random.choice(first_names)}",
                last_name=f"{random.choice(last_names)}",
                school_id=school.id
            )
            instructor.save()

            # Create ratings for each instructor
            for _ in range(rating_per_instructor):
                instructor_rating = Instructor_Rating(
                    instructor_id=instructor.id,
                    review=random.choice(instructor_text),
                    difficulty=random.randint(3, 5),
                    approachability=random.randint(3, 5),
                    availability=random.randint(3, 5),
                    helpfulness=random.randint(3, 5)
                )
                instructor_rating.save()

if __name__ == "__main__":
    create_tables()
    print_tables()

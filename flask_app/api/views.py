"""
Module to contain all views for api information
"""
from flask import jsonify, request
from . import api_views
from models import storage
from models.school import School
from models.instructor import Instructor


@api_views.route('/status')
def api_endpoint():
    data = {"message": "Hello from API",
            "statusCode": "200"}
    return jsonify(data)

# Schools routes
@api_views.route('/getSchoolData', methods=['POST'], strict_slashes=False)
def get_school_data():
    """For use in popup page to conatin all school data"""
    schoolName = request.form.get('schoolName')
    for school in storage.all(School).values():
        if school.name == schoolName:
            data = school.to_dict()
            data['overall'] = school.overall
            data['instructors'] = [instructor.to_dict() for instructor in school.instructors]
            data['ratings'] = [rating.to_dict() for rating in school.ratings]
            return jsonify(data)
    return jsonify({"statusText": "School not found in loop"}), 404


@api_views.route('/getschools')
def get_schools():
    """Get all schools or schools from a state and their ratings plus calculate averages"""
    schools = storage.all(School).values()
    state = request.args.get('schoolFilter')
    all_schools = schools
    # If a state is provided, filter the schools to only that state
    if state:
        states_schools = {}
        for school in schools:
            if school.state == state:
                states_schools[school.name] = school
        schools = states_schools
    if schools:
        # Calculate the average ratings for each schools ratings
        rating_types = ['facilities', 'happiness', 'internet', 'parking', 'social']

        for school in schools:
            for rating_type in rating_types:
                ratings = [getattr(rating, rating_type) for rating in school.ratings]
                if ratings:
                    avg = sum(ratings) / len(ratings)
                else:
                    avg = None
                setattr(school, f'{rating_type}_avg', round(avg, 1) if avg else None)
    data = []
    for school in schools:
        school_dict = school.to_dict()
        school_dict['ratings'] = [rating.to_dict() for rating in school.ratings]
        data.append(school_dict)
    return jsonify(data)


# Instructors routes
@api_views.route('/getInstructorData', methods=['POST'], strict_slashes=False)
def get_instructor_data():
    """For use in popup page to conatin all instructor reviews"""
    instructorId = request.form.get('instructorName')
    for instructor in storage.all(Instructor).values():
        if instructor.id == instructorId:
            # Use this loop to get all instructor information needed
            data = instructor.to_dict()
            return jsonify(data)
    return jsonify({"statusText": "Instructor not found"}), 404


@api_views.route('/getinstructors')
def get_instructors():
    """
    Used to get a list of all instructors and their
    ratings or instructors from a specific school
    """
    print('inside get_instructors')
    instructors = storage.all(Instructor).values()
    # If the ajax sent a school name to filter instructors. This is the "search" dropdown
    schoolId = request.args.get('instructorFilter')
    print(f"Request args schoolId: {schoolId}")
    if schoolId:
        # Get the school object from the name sent in query
        instructors = [instructor for instructor in instructors if instructor.school_id == schoolId]
        print(f"Found matching id {instructors}")
    # Calculate the average ratings for each ratings
    data = []
    for instructor in instructors:
        instructor_dict = instructor.to_dict()
        instructor_dict['ratings'] = [rating.to_dict() for rating in instructor.ratings]
        data.append(instructor_dict)
    print(f"Returning data from get_instructors")
    return jsonify(data)


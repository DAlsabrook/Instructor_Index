"""
Module to contain all views for api information
"""
from flask import jsonify, request, redirect, url_for
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

@api_views.route('/searchschools')
def search_schools():
    '''Search bar to find out what schools exist while user types
    returns the first school that contains the user input
    '''
    from collections import OrderedDict
    userInput = request.args.get('userInput')
    schools = storage.all(School)
    ordered_schools = OrderedDict(sorted(schools.items(), key=lambda item: item[1].name))
    data = []
    for school in ordered_schools.values():
        if userInput.lower() in school.name.lower():
            print(school.name)
            data.append(school.name)
    return jsonify(data)

@api_views.route('/getschools')
def get_schools():
    """Get all schools or schools from a state and their ratings plus calculate averages"""
    schools = storage.all(School).values()
    query = request.args.get('stateFilter')
    # If a query is provided, filter the schools
    if query != 'None':
        states_schools = {}
        for school in schools:
            # Checks if filter for school per state or if specific school
            if school.state == query or school.name.lower() == query.lower():
                states_schools[school.name] = school
        schools = states_schools.values()
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
    instructors = storage.all(Instructor).values()
    schoolId = request.args.get('schoolId')
    # If the ajax sent a school id to filter instructors. This is the "search" dropdown
    if schoolId != 'None':
        # Get the school object from the name sent in query
        instructors = [instructor for instructor in instructors if instructor.school_id == schoolId]
    # Calculate the average ratings for each ratings
    if instructors:
        rating_types = ['difficulty', 'approachability', 'availability', 'helpfulness']

        for instructor in instructors:
            for rating_type in rating_types:
                ratings = [getattr(rating, rating_type) for rating in instructor.ratings]
                if ratings:
                    avg = sum(ratings) / len(ratings)
                else:
                    avg = None
                setattr(instructor, f'{rating_type}_avg', round(avg, 1) if avg else None)
    data = []
    for instructor in instructors:
        instructor_dict = instructor.to_dict()
        instructor_dict['ratings'] = [rating.to_dict() for rating in instructor.ratings]
        data.append(instructor_dict)
    return jsonify(data)

@api_views.route('/search')
def search():
    '''
    This route is for the search bar for index.html to search schools in the database
    '''
    school = request.args.get('query')
    return redirect(url_for('web.schools', schoolFilter=school))

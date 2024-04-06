"""
Module to contain all views for api information
"""
from flask import jsonify, request
from . import api_views
from models import storage
from models.school import School

@api_views.route('/status')
def api_endpoint():
    data = {"message": "Hello from API",
            "statusCode": "200"}
    return jsonify(data)

@api_views.route('/getSchoolData', methods=['POST'], strict_slashes=False)
def get_school_data():
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
    schools = storage.all(School).values()
    state = request.args.get('schoolFilter')
    all_schools = schools
    # If a school name is provided, filter the schools
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

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

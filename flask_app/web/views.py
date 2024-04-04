"""
module used for all views to serve html pages
"""
from flask import request, redirect, render_template, jsonify
from flask_login import login_user, logout_user, login_required
from models import storage
from models.school import School
from . import web_views


@web_views.route('/', strict_slashes=False)
def home():
    return render_template('index.html')


@web_views.route('/login', methods=['POST'])
def login():
    input_username = request.form['username']
    input_password = request.form['password']
    user = storage.user(input_username, input_password)
    if user:
        login_user(user)
        return redirect(request.referrer)
    else:
        return 'Login Failed'


@web_views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(request.referrer)


@web_views.route('/signup', strict_slashes=False)
def signup():
    return render_template('signup.html')


@web_views.route('/schools', strict_slashes=False)
def schools():
    schools = storage.all(School)
    if schools:
        for school in schools.values():
            # Avg for facilities
            facilities_ratings = [rating.facilities for rating in school.ratings]
            if facilities_ratings:
                facilities_avg = sum(facilities_ratings) / len(facilities_ratings)
            else:
                facilities_avg = None
            school.facilities_avg = round(facilities_avg, 1)
            # Avg for happiness
            happiness_ratings = [rating.happiness for rating in school.ratings]
            if happiness_ratings:
                happiness_avg = sum(happiness_ratings) / len(happiness_ratings)
            else:
                happiness_avg = None
            school.happiness_avg = round(happiness_avg, 1)
            # Avg for internet
            internet_ratings = [rating.internet for rating in school.ratings]
            if internet_ratings:
                internet_avg = sum(internet_ratings) / len(internet_ratings)
            else:
                internet_avg = None
            school.internet_avg = round(internet_avg, 1)
            # Avg for parking
            parking_ratings = [rating.parking for rating in school.ratings]
            if parking_ratings:
                parking_avg = sum(parking_ratings) / len(parking_ratings)
            else:
                parking_avg = None
            school.parking_avg = round(parking_avg, 1)
            # Avg for social
            social_ratings = [rating.social for rating in school.ratings]
            if social_ratings:
                social_avg = sum(social_ratings) / len(social_ratings)
            else:
                social_avg = None
            school.social_avg = round(social_avg, 1)
        return render_template("school.html", schools=schools)
    else:
        exit(404)


@web_views.route('/instructors', strict_slashes=False)
def instructors():
    return render_template('instructor.html')

@web_views.route('/submit', methods = ['POST'])
def submit():
    # Get data sent from jquery click even
    data = request.get_json()
    # If submitting school rating
    if data['school']:
        from models.rating import School_Rating
        schoolName = data['school']
        facil = data['facilities']
        park = data['parking']
        inter = data['internet']
        soci = data['social']
        happ = data['happiness']
        schoolId = [school.id for school in storage.all(School).values() if school.name == schoolName]

            # Insert data into the database
        new_rating = School_Rating(school_id=schoolId[0],
                                   facilities=facil,
                                   parking=park,
                                   internet=inter,
                                   social=soci,
                                   happiness=happ)
        new_rating.save()
        if new_rating:
            return jsonify({'status': 'Success', 'message': 'Rating submitted successfully.'})
        else:
            return jsonify({'status': 'Error', 'message': 'Rating failed'})
    # If submitting instructor rating
    elif data['instructor']:
        from models.rating import Instructor_Rating
        return jsonify({'status': 'Success', 'message': 'Rating submitted successfully.'})

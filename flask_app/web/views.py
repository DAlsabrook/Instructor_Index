"""
module used for all views to serve html pages
"""
from flask import request, redirect, render_template, jsonify
from flask_login import login_user, logout_user, login_required
from models import storage
from models.school import School
from models.instructor import Instructor
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
    """Main schools page"""
    # Get list of all states that have schools for filter dropdown
    states = sorted(list(set([school.state for school in storage.all(School).values()])))
    stateFilter = request.args.get('schoolFilter') #query parameter for filtering states
    return render_template("school.html", states=states, stateFilter=stateFilter)

@web_views.route('/instructors', strict_slashes=False)
def instructors():
    """Main instructors page"""
    # Get list of all instructors
    instructors = storage.all(Instructor).values()
    # Find all schools from the instructors and sort them by name
    schools_dict = {instructor.school_id: storage.get(School, instructor.school_id) for instructor in instructors}
    schools = sorted(schools_dict.values(), key=lambda school: school.name)
    return render_template('instructor.html', schools=schools)

@web_views.route('/submit', methods = ['POST'])
def submit():
    # Get data sent from jquery click event
    data = request.get_json()
    print(data)
    # If submitting school rating
    if 'school' in data.keys():
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
    elif 'instructor' in data.keys():
        from models.rating import Instructor_Rating
        print(f'Successfully in Instructor if statment in /submit. Data= {data}')
        insName = data['instructor']
        difficulty = data['difficulty']
        approach = data['approachability']
        avail = data['availability']
        helpfulness = data['helpfulness']
        insId = [instructor.id for instructor in storage.all(Instructor).values() if instructor.name == insName]

        newRating = Instructor_Rating(instructor_id = insId[0],
                                      difficulty = difficulty,
                                      approachability = approach,
                                      availability = avail,
                                      helpfulness = helpfulness)
        newRating.save()
        if newRating:
            return jsonify({'status': 'Success', 'message': 'Rating submitted successfully.'})
        else:
            return jsonify({'status': 'Error', 'message': 'Rating failed'})

$(document).ready(() => {
    console.log('document ready');
    // Get from the user what schools have been rated
    const alreadyRated = localStorage.getItem("alreadyRated");
    // Get all schools from the database and build html for cards
    $.ajax({
        url: '/getschools',
        type: 'GET',
        data: { 'stateFilter': stateFilter },
        success: function (schools) {
            // Sort schools by name
            schools.sort(function (a, b) {
                var nameA = a.name.toUpperCase(); // Ignore case
                var nameB = b.name.toUpperCase(); // Ignore case
                if (nameA < nameB) {
                    return -1;
                }
                if (nameA > nameB) {
                    return 1;
                }
                return 0; // Names are equal
            });
            // Create a card for each school
            $.each(schools, function (index, school) {
                // FRONT OF SCHOOL CARD
                // Overall rating
                var overallH3 = $('<h3></h3>').addClass('mid_font').text('Overall: ' + school.overall);
                var overallRatingDiv = $('<div></div>').addClass('school_info_rating').append(overallH3);

                // Happiness rating
                var happinessH3 = $('<h3></h3>').addClass('mid_font').text('Happiness');
                var happinessImg = $('<img>').attr('src', 'static/images/happiness.bf5f7bd2.svg');
                var happinessLeft_content = $('<div></div>').addClass('left_content').append(happinessImg, happinessH3);
                var happinessScore = $('<h3></h3>').text(school.happiness_avg);
                var happinessRatingDiv = $('<div></div>').addClass('school_info_rating').append(happinessLeft_content, happinessScore);

                // Facilities rating
                var facilitiesH3 = $('<h3></h3>').addClass('mid_font').text('Facilities');
                var facilitiesImg = $('<img>').attr('src', 'static/images/facilities.1d6eadf9.svg');
                var facilitiesLeft_content = $('<div></div>').addClass('left_content').append(facilitiesImg, facilitiesH3);
                var facilitiesScore = $('<h3></h3>').text(school.facilities_avg);
                var facilitiesRatingDiv = $('<div></div>').addClass('school_info_rating').append(facilitiesLeft_content, facilitiesScore);

                // Internet rating
                var internetH3 = $('<h3></h3>').addClass('mid_font').text('Internet');
                var internetImg = $('<img>').attr('src', 'static/images/internet.30b903c3.svg');
                var internetLeft_content = $('<div></div>').addClass('left_content').append(internetImg, internetH3);
                var internetScore = $('<h3></h3>').text(school.internet_avg);
                var internetRatingDiv = $('<div></div>').addClass('school_info_rating').append(internetLeft_content, internetScore);

                // Parking rating
                var parkingH3 = $('<h3></h3>').addClass('mid_font').text('Parking');
                var parkingImg = $('<img>').attr('src', 'static/images/parking.jpeg');
                var parkingLeft_content = $('<div></div>').addClass('left_content').append(parkingImg, parkingH3);
                var parkingScore = $('<h3></h3>').text(school.parking_avg);
                var parkingRatingDiv = $('<div></div>').addClass('school_info_rating').append(parkingLeft_content, parkingScore);

                // Social rating div
                var socialH3 = $('<h3></h3>').addClass('mid_font').text('Social');
                var socialImg = $('<img>').attr('src', 'static/images/social.b8bb4cf6.svg');
                var socialLeft_content = $('<div></div>').addClass('left_content').append(socialImg, socialH3);
                var socialscore = $('<h3></h3>').text(school.social_avg);
                var socialRatingDiv = $('<div></div>').addClass('school_info_rating').append(socialLeft_content, socialscore);

                // Front of the cards bottom buttons
                var pageButton = $('<button></button>').addClass('pageButton').text('School Page');
                // Checking if user has already rated
                if (localStorage.getItem(toString(school.name))) {
                    var flipButton = $('<button></button>').addClass('noFlipButton').text('Already rated!');
                } else {
                    var flipButton = $('<button></button>').addClass('flipButton').text('Flip to rate');
                }

                var cardButtons = $('<div></div>').addClass('cardButtons').append(pageButton, flipButton);

                // School name div
                var schoolName = $('<h1></h1>').text(school.name);
                var schoolNameDiv = $('<div></div>').addClass('school_name bold_font').append(schoolName);

                // info container
                var schoolInfoContainer = $('<div></div>').addClass('school_info_container').append(overallRatingDiv, happinessRatingDiv, facilitiesRatingDiv, internetRatingDiv, parkingRatingDiv, socialRatingDiv, cardButtons);

                // content wrapper
                var contentWrapper = $('<div></div>').addClass('content_wrapper').append(schoolNameDiv, schoolInfoContainer);
                var front = $('<div></div>').addClass('front').append(contentWrapper);

                // BACK OF SCHOOL CARD
                // Create the backside divs
                var back = $('<div>').addClass('back');
                var contentWrapperDiv = $('<div>').addClass('content_wrapper');
                var slidersContainerDiv = $('<div>').addClass('sliders_container');
                var h1 = $('<h1>').text('Rate us!');
                var slidersDiv = $('<div>').addClass('sliders');

                // Create the sliders
                var ratings = ['happiness', 'facilities', 'internet', 'parking', 'social'];
                ratings.forEach(function (rating) {
                    var label = $('<label>').attr('for', 'slider_' + rating).text(rating.charAt(0).toUpperCase() + rating.slice(1) + ': ');
                    var span = $('<span>').attr('id', 'slider_' + rating + '_value').text('2');
                    label.append(span);
                    var input = $('<input>').attr({
                        type: 'range',
                        min: '0',
                        max: '5',
                        value: '2',
                        class: 'slider',
                        id: 'slider_' + rating
                    });
                    var div = $('<div>').append(label, input);
                    slidersDiv.append(div);
                });

                // Create backside buttons
                var button = $('<button>').addClass('purple_button').attr('id', 'slider_submit').text('Rate');
                var flipButton = $('<button>').addClass('flipButton').text('Front');

                // Append sliders and buttons to the back div
                slidersDiv.append(button);
                slidersContainerDiv.append(h1, slidersDiv, flipButton);
                contentWrapperDiv.append(slidersContainerDiv);
                back.append(contentWrapperDiv);

                // Append front and back to the school container and school container to section
                var schoolContainer = $('<div></div>').addClass('school_container').append(front, back);
                var scaleContainer = $('<div></div>').addClass('scale_container').append(schoolContainer);
                $('.school_ratings_section').append(scaleContainer);
            });
        },
        error: function (error) {
            console.error('Error:', error);
        }});

    // Flip card logic
    $(document).on('click', '.flipButton', function () {
        console.log('Flipping');
        //find the closest school container and flip it
        var flipper = $(this).closest('.scale_container').find('.school_container');
        flipper.toggleClass('flipped');
    });

    // Slider logic to update values while sliding
    $(document).on('input', '.slider', function () {
        var sliderId = $(this).attr('id');
        var value = $(this).val();
        var spanId = sliderId + '_value';
        var label = $(this).closest('.sliders').find('#' + spanId);
        label.text(value);
    });

    // Slider submit logic
    $(document).on('click', '#slider_submit', function () {
        console.log('Slider sumbit clicked');
        var flipper = $(this).closest('.scale_container').find('.school_container');
        flipper.toggleClass('flipped');
        var schoolName = flipper.find('.school_name h1').text();
        flipper.find('.school_info_container .flipButton').removeClass('flipButton').addClass('noFlipButton').text('Already Rated!');
        // Store the {schoolName(string), true(string)} to use for validation when creating cards on document load
        localStorage.setItem(schoolname, "true");

        var data = {
            school: schoolName,
            facilities: $(this).closest('.sliders_container').find('#slider_facilities').val(),
            parking: $(this).closest('.sliders_container').find('#slider_parking').val(),
            internet: $(this).closest('.sliders_container').find('#slider_internet').val(),
            social: $(this).closest('.sliders_container').find('#slider_social').val(),
            happiness: $(this).closest('.sliders_container').find('#slider_happiness').val()
        };
        $.ajax({
            url: '/submit',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function (response) {
                console.log('Success:', response);

            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    });
    // Popup page that contains a schools full information
    $(document).on('click', '.pageButton', function () {
        var search = $(this).closest('.content_wrapper').find('.school_name');
        var schoolName = search.find('h1').text();
        // Make an AJAX request to get data from api. Send schoolName for api to use
        $.ajax({
            url: '/getSchoolData', // The URL of server-side script
            type: 'POST',
            data: { schoolName: schoolName }, // Send the school name as data
            success: function (school) {
                var instructorsList = school.instructors;
                var section = $(".schoolPage").find('.schoolData');
                section.text(JSON.stringify(school.name));
                for (var i = 0; i < instructorsList.length; i++) {
                    var h3 = $('<h3></h3>').text(instructorsList[i].first_name);
                    section.append(h3);
                }
            },
            error: function (error) {
                console.error('Error:', error);
                $(".schoolPage").find('.schoolData').text(JSON.stringify(error.statusText));
            }
        });
        $(".schoolPage").addClass('show');
    });
    $(document).on('click', '.closeButton', function () {
        $(".schoolPage").removeClass('show');
    });
});

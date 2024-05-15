$(document).ready(() => {
    console.log('document ready');

    // Get all instructors from the database and build html for cards
    $.ajax({ // This is not getting query parameter from /instructors
        url: '/getinstructors',
        type: 'GET',
        success: function (instructors) {
            // Create a card for each instructor
            $.each(instructors, function (index, instructor) {
                // FRONT OF instructor CARD
                // Overall rating
                var overallH3 = $('<h3></h3>').addClass('mid_font').text('Overall: ' + instructor.overall);
                var overallRatingDiv = $('<div></div>').addClass('instructor_info_rating').append(overallH3);

                // Happiness rating
                // var happinessH3 = $('<h3></h3>').addClass('mid_font').text('Happiness');
                // var happinessImg = $('<img>').attr('src', 'static/images/happiness.bf5f7bd2.svg');
                // var happinessLeft_content = $('<div></div>').addClass('left_content').append(happinessImg, happinessH3);
                // var happinessScore = $('<h3></h3>').text(instructor.happiness_avg);
                // var happinessRatingDiv = $('<div></div>').addClass('instructor_info_rating').append(happinessLeft_content, happinessScore);

                // Front of the cards bottom buttons
                var pageButton = $('<button></button>').addClass('pageButton').text('instructor Page');
                var flipButton = $('<button></button>').addClass('flipButton').text('Flip to rate');
                var cardButtons = $('<div></div>').addClass('cardButtons').append(pageButton, flipButton);

                // instructor name div
                var instructorName = $('<h1></h1>').text(instructor.name);
                var instructorNameDiv = $('<div></div>').addClass('instructor_name bold_font').append(instructorName);

                // info container
                var instructorInfoContainer = $('<div></div>').addClass('instructor_info_container').append(overallRatingDiv, cardButtons);

                // content wrapper
                var contentWrapper = $('<div></div>').addClass('content_wrapper').append(instructorNameDiv, instructorInfoContainer);
                var front = $('<div></div>').addClass('front').append(contentWrapper);

                // BACK OF instructor CARD
                // Create the backside divs
                var back = $('<div>').addClass('back');
                var contentWrapperDiv = $('<div>').addClass('content_wrapper');
                var slidersContainerDiv = $('<div>').addClass('sliders_container');
                var h1 = $('<h1>').text('Rate me!');
                var slidersDiv = $('<div>').addClass('sliders');

                // Create the sliders
                var ratings = ['difficulty', 'approachability', 'availability', 'helpfulness'];
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

                // Append front and back to the instructor container and instructor container to section
                var instructorContainer = $('<div></div>').addClass('instructor_container').append(front, back);
                var scaleContainer = $('<div></div>').addClass('scale_container').append(instructorContainer);
                $('.instructor_ratings_section').append(scaleContainer);
            });
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });

    // Flip card logic
    $(document).on('click', '.flipButton', function () {
        //find the closest instructor container and flip it
        var flipper = $(this).closest('.scale_container').find('.instructor_container');
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
        var flipper = $(this).closest('.scale_container').find('.instructor_container');
        flipper.toggleClass('flipped');
        var instructorName = flipper.find('.instructor_name h1').text();
        flipper.find('.instructor_info_container .flipButton').removeClass('flipButton').addClass('noFlipButton').text('Already Rated!');

        var data = {
            instructor: instructorName,
            difficulty: $(this).closest('.sliders_container').find('#slider_difficulty').val(),
            approachability: $(this).closest('.sliders_container').find('#slider_approachability').val(),
            availability: $(this).closest('.sliders_container').find('#slider_availability').val(),
            helpfulness: $(this).closest('.sliders_container').find('#slider_helpfulness').val()
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
    // Popup page that contains a instructors full information
    $(document).on('click', '.pageButton', function () {
        var search = $(this).closest('.content_wrapper').find('.instructor_name');
        var instructorName = search.find('h1').text();
        // Make an AJAX request to get data from api. Send instructorName for api to use
        // $.ajax({
        //     url: '/getinstructorData', // The URL of your server-side script
        //     type: 'POST',
        //     data: { instructorName: instructorName }, // Send the instructor name as data
        //     success: function (instructor) {
        //         var instructorsList = instructor.instructors;
        //         var section = $(".instructorPage").find('.instructorData');
        //         section.text(JSON.stringify(instructor.name));
        //         for (var i = 0; i < instructorsList.length; i++) {
        //             var h3 = $('<h3></h3>').text(instructorsList[i].first_name);
        //             section.append(h3);
        //         }
        //     },
        //     error: function (error) {
        //         console.error('Error:', error);
        //         $(".instructorPage").find('.instructorData').text(JSON.stringify(error.statusText));
        //     }
        // });
        $(".instructorPage").addClass('show');
    });
    $(document).on('click', '.closeButton', function () {
        $(".instructorPage").removeClass('show');
    });
});

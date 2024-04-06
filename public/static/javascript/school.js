$(document).ready(() => {
    console.log('document ready');
    $(document).on('click', '.flipButton', function () {
        console.log('Flipping');
        var flipper = $(this).closest('.scale_container').find('.school_container');
        flipper.toggleClass('flipped');
    });
    $('.slider').on('input', function () {
        var sliderId = $(this).attr('id');
        var value = $(this).val();
        $(this).closest('.sliders_container').find('#' + sliderId + '_value').text(value);
    });
    $(document).on('click', '#slider_submit', function () {
        console.log('Slider sumbit clicked');
        var flipper = $(this).closest('.scale_container').find('.school_container');
        flipper.toggleClass('flipped');
        var schoolName = flipper.find('.school_name h1').text();
        flipper.find('.school_info_container .flipButton').removeClass('flipButton').addClass('noFlipButton').text('Already Rated!');

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
    $(document).on('click', '.pageButton', function () {
        var search = $(this).closest('.content_wrapper').find('.school_name');
        var schoolName = search.find('h1').text();
        // Make an AJAX request to get data from api. Send schoolName for api to use
        $.ajax({
            url: '/getSchoolData', // The URL of your server-side script
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

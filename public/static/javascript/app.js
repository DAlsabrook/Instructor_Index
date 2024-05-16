$(document).ready(() => {
    // SHARED
    // NAVIGATE to log-in.html
    $('#nav-link-log-in').on('click', () => {
        window.location.href = '/login';
    });
    // NAVIGATE to homepage
    $('#nav-home').on('click', () => {
        window.location.href = '/';
    });
    // NAVIGATE to schools.html
    $('#nav-schools').on('click', () => {
        window.location.href = '/schools';
    });
    // NAVIGATE to instructor.html
    $('#nav-instructors').on('click', () => {
        window.location.href = '/instructors';
    });
    // NAVIGATE to new-account.html
    $('#sign_up').on('click', () => {
        window.location.href = '/signup';
    });

    $('#up_btn').on('click', () => {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    });
    // When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function () { scrollFunction() };

    function scrollFunction() {
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            $('#up_btn').show();
        } else {
            $('#up_btn').hide();
        }
    }
    // All buttons change to pointer hand and grow on hover
    $(document).on({
        mouseenter: function () {
            // On mouse enter
            $(this).css({
                'transform': 'scale(1.1)',
                'transition': 'transform 0.7s ease',
                'box-sizing': 'border-box',
                'cursor': 'pointer'
            });
        },
        mouseleave: function () {
            // On mouse leave
            $(this).css({
                'transform': '',
                'transition': '',
                'box-sizing': ''
            });
        }
    }, 'button');
    function window.
});

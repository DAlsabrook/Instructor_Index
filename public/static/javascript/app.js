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
    // All buttons change to pointer hand on hover
    $('button').hover(function () {
        // On mouse enter
        $(this).css({
            'transform': 'scale(1.1)',
            'transition': 'transform 0.7s ease',
            'box-sizing': 'border-box',
            'cursor': 'pointer'
        });
    }, function () {
        // On mouse leave
        $(this).css({
            'transform': '',
            'transition': '',
            'box-sizing': ''
        });
    });
});

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
    $('button').mouseenter(function() {
        $(this).css('cursor', 'pointer');
        $(this).css('font-weight', '600')
    }).mouseleave(function () {
        $(this).css('cursor', '');
        $(this).css('font-weight', '');
    });
    $('#nav-schools, #nav-instructors, #nav-link-log-in').mouseenter(function () {
        $(this).css('background-color', 'white');
        $(this).css('color', 'black');
    }).mouseleave(function () {
        $(this).css('background', '');
        $(this).css('color', '');
    });
});

$(document).ready(() => {
    // SHARED
    // NAVIGATE to log-in.html
    $('#nav-link-log-in').on('click', () => {
        window.location.href = './log-in.html';
    });
    // NAVIGATE to homepage
    $('#nav-home').on('click', () => {
        window.location.href = './index.html';
    });
    // NAVIGATE to schools.html
    $('#nav-schools').on('click', () => {
        window.location.href = './school.html';
    });
    // NAVIGATE to instructor.html
    $('#nav-instructors').on('click', () => {
        window.location.href = './instructor.html';
    });
    // NAVIGATE to new-account.html
    $('#sign_up').on('click', () => {
        window.location.href = './new-account.html';
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

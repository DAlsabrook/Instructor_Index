$(document).ready(() => {
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
});

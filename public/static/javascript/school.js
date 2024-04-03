$(document).ready(() => {
    $('.flipButton').on('click', function () {
        var flipper = $(this).closest('.scale_container').find('.school_container');
        flipper.toggleClass('flipped');
    });
    $('#myRange').html(() => {
        return this.value;
    });
});

$(document).ready(() => {
    $('#search').on('input', function () {
        console.log('input is happening')
        $.ajax({
            url: '/searchschools',
            type: 'GET',
            data: { 'userInput': $(this).val() },
            success: function (schoolNames) {
                console.log(`Success: ${schoolNames}`)
                if (schoolNames !== '') {
                    // Clear the datalist
                    $('#school-list').empty();
                    // Add the found school as an option in the datalist
                    schoolNames.forEach(school => {
                        $('#school-list').append(`<option value="${school}">`);
                    });

                }
            }
        });
    });
});

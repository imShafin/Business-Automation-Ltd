$(document).ready(function() {
    $('#contactForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '/save_contact/',
            data: $('#contactForm').serialize(),
            success: function(response) {
                if (response.success) {
                    alert('Contact saved successfully');
                    location.reload();
                } else {
                    alert('Error saving contact');
                }
            }
        });
    });

    $('.download-btn').click(function() {
        var contactId = $(this).data('contact-id');
        window.location.href = '/download_pdf/' + contactId + '/';
    });
});

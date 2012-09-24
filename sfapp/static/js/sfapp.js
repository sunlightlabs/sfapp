$(document).ready(function() {

    $('#sfapp-subscribe-form').submit(function(ev) {

        var $form = $(this);

        var response_type = $form.find('input[name=response]').val();
        var email = $form.find('input[name=email]').val();
        var zipcode = $form.find('input[name=zipcode]').val();

        var params = {
            response: response_type,
            email: email,
            zipcode: zipcode
        };

        $.post('/subscribe/', params, function(resp) {
            var $p = $('<p>').text(resp.message).hide();
            $form.slideUp('fast', function() {
                $form.after($p);
                $p.slideDown();
            });
        });

        ev.preventDefault();

    });

});
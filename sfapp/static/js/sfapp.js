$(document).ready(function() {

    $('#sfapp-subscribe-form').submit(function(ev) {

        var $form = $(this);

        var response_type = $form.find('input[name=response]').val(),
            email = $form.find('input[name=email]').val(),
            zipcode = $form.find('input[name=zipcode]').val(),
            url = $form.attr('action') || '/subscribe/';

        var params = {
            response: response_type,
            email: email,
            zipcode: zipcode
        };

        $.post(url, params, function(resp) {
            var $p = $('<p>').text(resp.message).hide();
            $form.slideUp('fast', function() {
                $form.after($p);
                $p.slideDown();
            });
        });

        ev.preventDefault();

    });

});
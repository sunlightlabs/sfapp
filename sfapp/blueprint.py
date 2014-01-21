from flask import Blueprint, flash, json, redirect, render_template, request

from sfapp import mailinglist


sfapp = Blueprint('sfapp', __name__,
            static_folder='static',
            static_url_path='/static/',
            template_folder='templates')

@sfapp.route('/subscribe', methods=['POST'])
def subscribe():

    email = request.form.get("email", "")
    zipcode = request.form.get("zipcode", "")

    if email:

        response = mailinglist.subscribe(email, zipcode)

    if request.is_xhr:
        resp = {'message': mailinglist.SUCCESS_MESSAGE}
        return json.jsonify(**resp)

    flash(mailinglist.SUCCESS_MESSAGE)
    referrer = request.headers.get('Referer', None)

    return redirect(referrer or '/')

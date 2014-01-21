from flask import Blueprint, render_template

sfapp = Blueprint('sfapp', __name__,
            static_folder='static',
            static_url_path='/static/',
            template_folder='templates')

from flask import Blueprint, render_template

sfapp_page = Blueprint('sfapp_page', __name__,
                       static_folder='static',
                       template_folder='templates')


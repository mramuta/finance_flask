from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('high_volume', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

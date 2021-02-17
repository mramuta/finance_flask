from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('error_handlers', __name__)

@bp.app_errorhandler(404)
def handle404(e):
    return redirect('/')
from flask import current_app as app
from flask import redirect, render_template, request, session
from .models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)
from .check import app_view
from . import db

@app.route('/<int:id>')
def base(id):
    return app_view(id)

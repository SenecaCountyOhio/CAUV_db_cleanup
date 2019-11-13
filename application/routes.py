from flask import current_app as app
from flask import redirect, render_template, request, session
from .models import (
    CAUVapp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)
from .check import check

@app.route('/')
def base():
    table_views = []
    for x in range(0,4000):
        table_views.append(check(x))
    return table_views

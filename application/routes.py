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

@app.route('/<int:id>', methods = ['POST', 'GET'])
def base(id):
    if request.method == "POST":
        next_id = id + 1
        return redirect('/' + str(next_id))
    else:
        data = app_view(id)
        next_id = id + 1
        if data['ERRORS'] == {}:
            return redirect('/' + str(next_id))
        if 'NEVER_FILED' in data['ERRORS'].keys():
            return redirect('/' + str(next_id))
        return render_template(
            'index.html',
            appNum=id,
            data=data,
        )

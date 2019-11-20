from flask import current_app as app
from flask import redirect, render_template, request, session
from .models import (
    CAUVApp,
    AG_LAND,
    RECOMMENDED_CAUVApp,
)
from .CURRENT import current_app, current_app_sum
from .AG_LAND import (
    parcel_view,
    parcel_sum,
    land_view,
    land_sum,
)
from .ERRORS import compiled_errors

from .RECOMMENDATION import recommendation, recommendation_sum
from . import db

@app.route('/<int:id>', methods = ['POST', 'GET'])
def base(id):
    next_id = id + 1
    if request.method == "POST":
        return redirect('/' + str(next_id))
    else:
        app_select = CAUVApp.query.filter(CAUVApp.AG_APP == id).first()
        if app_select is None:
            return redirect('/' + str(next_id))
        else:
            current = current_app(app_select)
            current_sum = current_app_sum(app_select)
            AG_LAND_parcels = parcel_view(id)
            AG_LAND_parcel_sum = parcel_sum(AG_LAND_parcels)
            AG_LAND_land = land_view(id)
            AG_LAND_land_sum = land_sum(AG_LAND_land)
            errors_compiled = compiled_errors(
                app_select=app_select,
                parcel_sum=AG_LAND_parcel_sum,
                AG_LAND_land=AG_LAND_land,
                current_sum=current_sum,
            )
            app_recommendation = recommendation(
                app_select=app_select,
                AG_LAND_parcel=AG_LAND_parcels,
                AG_LAND_land=AG_LAND_land,
                errors=errors_compiled,
            )
            app_recommendation_sum = recommendation_sum(app_recommendation)
            recom_app_select = RECOMMENDED_CAUVApp.query.filter(RECOMMENDED_CAUVApp.AG_APP == id).first()
            recommendation_errors = compiled_errors(
                app_select=recom_app_select,
                parcel_sum=AG_LAND_parcel_sum,
                AG_LAND_land=AG_LAND_land,
                current_sum=app_recommendation_sum,
            )
            recommended = current_app(recom_app_select)
            if len(errors_compiled) == 0:
                return redirect('/' + str(next_id))
            if len(recommendation_errors) == 0:
                return redirect('/' + str(next_id))
            #if 'APPLICATION NEVER FILED' in errors_compiled:
            #    return redirect('/' + str(next_id))
            return render_template(
                'index.html',
                appNum=id,
                errors=errors_compiled,
                current=current,
                current_sum=current_sum,
                AG_LAND_parcels=AG_LAND_parcels,
                AG_LAND_parcel_sum=AG_LAND_parcel_sum,
                AG_LAND_land=AG_LAND_land,
                AG_LAND_land_sum=AG_LAND_land_sum,
                recommendation=app_recommendation,
                recommendation_sum=app_recommendation_sum,
                recommendation_errors=recommendation_errors,
                recommended=recommended,
            )

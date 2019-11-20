from application import db, create_app
from application.CURRENT import current_app, current_app_sum
from application.models import (
    CAUVApp,
    AG_LAND,
    RECOMMENDED_CAUVApp
)
from application.RECOMMENDATION import recommendation, recommendation_sum
from application.AG_LAND import (
    parcel_view,
    parcel_sum,
    land_view,
    land_sum,
)
from application.ERRORS import compiled_errors

app = create_app()
app.app_context().push()

all_apps = db.session.query(CAUVApp)

for each in all_apps:
    id = each.AG_APP
    current = current_app(each)
    current_sum = current_app_sum(each)
    AG_LAND_parcels = parcel_view(id)
    AG_LAND_parcel_sum = parcel_sum(AG_LAND_parcels)
    AG_LAND_land = land_view(id)
    AG_LAND_land_sum = land_sum(AG_LAND_land)
    current_errors = compiled_errors(
        app_select=each,
        parcel_sum=AG_LAND_parcel_sum,
        AG_LAND_land=AG_LAND_land,
        current_sum=current_sum,
    )
    app_recommendation = recommendation(
        app_select=each,
        AG_LAND_parcel=AG_LAND_parcels,
        AG_LAND_land=AG_LAND_land,
        errors=current_errors,
    )
    temp_app = RECOMMENDED_CAUVApp(
        AG_APP= each.AG_APP,
        Commodity_Acres=app_recommendation['Commodity_Acres'],
        Hay_Acres=app_recommendation['Hay_Acres'],
        Perm_Pasture_Acres=app_recommendation['Perm_Pasture_Acres'],
        Noncommercial_Wood_Acres=app_recommendation['Noncommercial_Wood_Acres'],
        Commerical_Wood_Acres=app_recommendation['Commerical_Wood_Acres'],
        Other_Crop_Acres=app_recommendation['Other_Crop_Acres'],
        Homesite_Acres=app_recommendation['Homesite_Acres'],
        Road_Waste_Pond_Acres=app_recommendation['Road_Waste_Pond_Acres'],
        CRP_Acres=app_recommendation['CRP_Acres'],
        Con25_Acres=app_recommendation['Con25_Acres'],
        Other_Use_Acres=app_recommendation['Other_Use_Acres'],
        Stated_Total_Acres=app_recommendation['Stated_Total_Acres'],
        Gross_Income_1=app_recommendation['Gross_Income_1'],
        Gross_Income_2=app_recommendation['Gross_Income_2'],
        Gross_Income_3=app_recommendation['Gross_Income_3'],
    )
    db.session.add(temp_app)
db.session.commit()

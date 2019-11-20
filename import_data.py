import csv
import os
from application import db, create_app
from application.models import (
    CAUVApp,
    AG_LAND,
    RECOMMENDED_CAUVApp
)
from application.CURRENT import current_app, current_app_sum
from application.RECOMMENDATION import recommendation, recommendation_sum
from application.AG_LAND import (
    parcel_view,
    parcel_sum,
    land_view,
    land_sum,
)
from application.ERRORS import compiled_errors


def import_to_model(directory):
    app = create_app()
    app.app_context().push()

    file_list = [
    'AG_LAND.csv',
    #'Parcels_AGAPP_Inquire.csv',
    #'CORRECTED_CAUVApps.csv',
    'CAUVApps.csv',
    #'Parcels.csv',
    #'Homesite.csv',
    #'CRP.csv',
    #'CON25.csv',
    #'ERRORS.csv',
    ]
    for file in os.listdir(directory):
        if str(file) in file_list:
            with open(directory + "\\" + str(file)) as f:
                reader = csv.reader(f)
                #skip the first row
                next(reader, None)
                print('importing ' + str(file))
                for row in reader:
                    if str(file) == 'CAUVApps.csv':
                        app = CAUVApp(
                            AG_APP=row[0],
                            Commodity_Acres=row[1],
                            Hay_Acres=row[2],
                            Perm_Pasture_Acres=row[3],
                            Noncommercial_Wood_Acres=row[4],
                            Commerical_Wood_Acres=row[5],
                            Other_Crop_Acres=row[6],
                            Homesite_Acres=row[7],
                            Road_Waste_Pond_Acres=row[8],
                            CRP_Acres=row[9],
                            Con25_Acres=row[10],
                            Other_Use_Acres=row[11],
                            Stated_Total_Acres=row[12],
                            Gross_Income_1=row[13],
                            Gross_Income_2=row[14],
                            Gross_Income_3=row[15],
                        )
                        #print('CAUVApp' + app.AG_APP)
                        db.session.add(app)

                    elif str(file) == 'AG_LAND.csv':
                        app = AG_LAND(
                            PARID=row[0],
                            AGAPPL=row[1],
                            PARCEL_ACREAGE=row[2],
                            LAND_USE_TYPE=row[3],
                            LAND_USE_ACRES=row[4],
                        )
                        db.session.add(app)
                    else:
                        pass
                        #print('NO MODEL FOR' + str(file))

                db.session.commit()


def build_recommendations():
    app = create_app()
    app.app_context().push()
    all_apps = db.session.query(CAUVApp)

    for each in all_apps:
        id = each.AG_APP
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
        print('calculating recommendation for ' + str(temp_app.AG_APP))
    db.session.commit()


import_to_model('B:\\Projects\\CAUV\\2020\\Database Cleanup\\automation app\\data')
build_recommendations()

from application import db, create_app
from application.check import app_view
from application.models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)

app = create_app()
app.app_context().push()

all_apps = db.session.query(CAUVApp)

#FIRST ADJUST HOMESITE, CRP, & CON25
for each in all_apps:
    app_num = each.AG_APP
    data = app_view(app_num)
    # SKIP IF APP NEVER FILED
    if 'NEVER_FILED' in data['ERRORS'].keys():
        continue
    if 'HOMESITE' in data['ERRORS'].keys():
        homesite_diff = data['GIS_VALUES']['HOMESITE'] - data['APP_VALUES']['Homesite_Acres']
        road_recommended = -1 * (homesite_diff) + data['APP_VALUES']['Road_Waste_Pond_Acres']
        if road_recommended >= 0:
            print("APPNUM: " + str(each.AG_APP) + " | " + "HOMESITE DIFF :" + str(homesite_diff))
            each.Homesite_Acres = data['GIS_VALUES']['HOMESITE']
            each.Road_Waste_Pond_Acres = round(road_recommended,3)
    if 'CRP' in data['ERRORS'].keys():
        CRP_diff = data['GIS_VALUES']['CRP'] - data['APP_VALUES']['CRP_Acres']
        road_recommended = -1 * (CRP_diff) + data['APP_VALUES']['Road_Waste_Pond_Acres']
        if road_recommended >= 0:
            print("APPNUM: " + str(each.AG_APP) + " | " + "CRP DIFF :" + str(CRP_diff))
            each.CRP_Acres = data['GIS_VALUES']['CRP']
            each.Road_Waste_Pond_Acres = round(road_recommended,3)
    if 'CON25' in data['ERRORS'].keys():
        CON25_diff = data['GIS_VALUES']['CON25'] - data['APP_VALUES']['Con25_Acres']
        road_recommended = -1 * (CON25_diff) + data['APP_VALUES']['Road_Waste_Pond_Acres']
        if road_recommended >= 0:
            print("APPNUM: " + str(each.AG_APP) + " | " + "CON25 DIFF :" + str(CON25_diff))
            each.Con25_Acres = data['GIS_VALUES']['CON25']
            each.Road_Waste_Pond_Acres = round(road_recommended,3)

db.session.commit()

#THEN RUN FOR DEED
for each in all_apps:
    app_num = each.AG_APP
    data = app_view(app_num)
    # SKIP IF APP NEVER FILED
    if 'NEVER_FILED' in data['ERRORS'].keys():
        continue
    if 'DEED' in data['ERRORS'].keys():
        DEED_diff = data['GIS_VALUES']['Parcels_Combined_Acres'] - data['APP_VALUES']['CALCULATED_ACRES']
        road_recommended = -1 * (DEED_diff) + data['APP_VALUES']['Road_Waste_Pond_Acres']
        if road_recommended >= 0:
            print("APPNUM: " + str(each.AG_APP) + " | " + "DEED DIFF :" + str(DEED_diff))
            each.Road_Waste_Pond_Acres = round(road_recommended,3)

db.session.commit()

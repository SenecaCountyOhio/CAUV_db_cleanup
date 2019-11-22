import csv
import os
import sys
from application import db, create_app
from application.models import (
    CAUVApp,
    RECOMMENDED_CAUVApp,
)
from application.AG_LAND import (
    parcel_view,
    parcel_sum,
    land_view,
    land_sum,
)
from application.ERRORS import compiled_errors
from application.RECOMMENDATION import recommendation, recommendation_sum
from application.CURRENT import current_app, current_app_sum


app = create_app()
app.app_context().push()

def export_to_csv(directory):
    with open(
        directory + "\\" + str(sys.argv[1]) + ".csv",
        'w',
        newline=""
    ) as f:
        all_apps = db.session.query(RECOMMENDED_CAUVApp)
        fieldnames = [
            'AG_APP',
            'TOTAL PARCEL ACRES',
            'TOTAL AGLAND ACRES',
            'Commodity_Acres',
            'Hay_Acres',
            'Perm_Pasture_Acres',
            'Noncommercial_Wood_Acres',
            'Commerical_Wood_Acres',
            'Other_Crop_Acres',
            'Homesite_Acres',
            'Road_Waste_Pond_Acres',
            'CRP_Acres',
            'Con25_Acres',
            'Other_Use_Acres',
            'Stated_Total_Acres',
            'Gross_Income_1',
            'Gross_Income_2',
            'Gross_Income_3',
            'NOTE',
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for each in all_apps:
            id = each.AG_APP
            parcel_list = parcel_view(id)
            parcel_list_sum = parcel_sum(parcel_list)
            land_list = land_view(id)
            land_list_sum = land_sum(land_list)
            errors_compiled = compiled_errors(
                app_select=each,
                parcel_sum=parcel_list_sum,
                AG_LAND_land=land_list,
                current_sum=current_app_sum(each)
            )
            writer.writerow(
                {
                    'AG_APP': each.AG_APP,
                    'TOTAL PARCEL ACRES': parcel_list_sum,
                    'TOTAL AGLAND ACRES': land_list_sum,
                    'Commodity_Acres': each.Commodity_Acres,
                    'Hay_Acres': each.Hay_Acres,
                    'Perm_Pasture_Acres': each.Perm_Pasture_Acres,
                    'Noncommercial_Wood_Acres': each.Noncommercial_Wood_Acres,
                    'Commerical_Wood_Acres': each.Commerical_Wood_Acres,
                    'Other_Crop_Acres': each.Other_Crop_Acres,
                    'Homesite_Acres': each.Homesite_Acres,
                    'Road_Waste_Pond_Acres': each.Road_Waste_Pond_Acres,
                    'CRP_Acres': each.CRP_Acres,
                    'Con25_Acres': each.Con25_Acres,
                    'Other_Use_Acres': each.Other_Use_Acres,
                    'Stated_Total_Acres': each.Stated_Total_Acres,
                    'Gross_Income_1': each.Gross_Income_1,
                    'Gross_Income_2': each.Gross_Income_2,
                    'Gross_Income_3': each.Gross_Income_3,
                    'NOTE': errors_compiled
                }
            )
            print(each.AG_APP)
        print("writing complete")

export_to_csv('B:\\Projects\\CAUV\\2020\\Database Cleanup\\automation app\\data')

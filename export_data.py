import csv
import os
from application.models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)
from application import db, create_app

app = create_app()
app.app_context().push()

def export_to_csv(directory):
    with open(
        directory + "\\" + "CORRECTED_CAUVApps.csv",
        'w',
        newline=""
    ) as f:
        all_apps = db.session.query(CAUVApp)
        fieldnames = [
            'AG_APP',
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
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for each in all_apps:
            writer.writerow(
                {
                    'AG_APP': each.AG_APP,
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
                }
            )
            print(each.AG_APP)
        print("writing complete")

export_to_csv('B:\\Projects\\CAUV\\2020\\Database Cleanup\\automation app\\data')

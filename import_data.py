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

file_list = [
    'CAUVApps.csv',
    'Parcels.csv',
    'Homesite.csv',
    'CRP.csv',
    'CON25.csv',
    'ERRORS.csv',
]

def import_to_model(directory):
    for file in os.listdir(directory):
        if str(file) in file_list:
            with open(str(file)) as f:
                reader = csv.reader(f)
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
                    elif str(file) == 'Parcels.csv':
                        app = Parcels(
                            PARID=row[2],
                            AG_APP=row[1],
                            DEED=row[4],
                            NAME1=row[5],
                            NAME2=row[6],
                        )
                    elif str(file) == 'Homesite.csv':
                        app = Homesite(
                            AG_APP=row[1],
                            HOMESITE=row[3],
                        )
                    elif str(file) == 'CRP.csv':
                        app = CRP(
                            AG_APP=row[1],
                            CRP=row[3],
                        )
                    elif str(file) == 'CON25.csv':
                        app = CON25(
                            AG_APP=row[1],
                            CON25=row[3],
                        )
                    elif str(file) == 'ERRORS.csv':
                        app = ERRORS(
                            AG_APP=row[0],
                            never_filed=row[1],
                            DEED=row[2],
                            STATED=row[3],
                            HOMESITE=row[6],
                            CRP=row[5],
                            CON25=row[4],
                            INCOME=row[7]
                        )
                    else:
                        return 'error'

                    db.session.add(app)
                    db.session.commit()

import_to_model('B:\\Projects\\CAUV\\2020\\Database Cleanup\\automation app\\data')

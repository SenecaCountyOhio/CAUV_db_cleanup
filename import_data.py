import csv
import os
from application.models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
    AG_LAND
)
from application import db, create_app


app = create_app()
app.app_context().push()

file_list = [
    'AG_LAND.csv',
    'Parcels_AGAPP_Inquire.csv',
    #'CORRECTED_CAUVApps.csv',
    'CAUVApps.csv',
    #'Parcels.csv',
    'Homesite.csv',
    'CRP.csv',
    'CON25.csv',
    #'ERRORS.csv',
]

def import_to_model(directory):
    for file in os.listdir(directory):
        print(str(file))
        if str(file) in file_list:
            with open(directory + "\\" + str(file)) as f:
                reader = csv.reader(f)
                #skip the first row
                next(reader, None)
                for row in reader:
                    if str(file) == 'CAUVApps.csv':
                        try:
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
                        except:
                            continue
                        #print('CAUVApp' + app.AG_APP)
                        db.session.add(app)
                    elif str(file) == 'Parcels_AGAPP_Inquire.csv':
                        app = Parcels(
                            PARID=row[0],
                            AG_APP=row[1],
                            DEED=row[2],
                        )
                        #print('Parcels' + app.AG_APP)
                        db.session.add(app)
                    elif str(file) == 'Homesite.csv':
                        app = Homesite(
                            AG_APP=row[1],
                            HOMESITE=row[3],
                        )
                        #print('HOMESITE' + app.AG_APP)
                        db.session.add(app)
                    elif str(file) == 'CRP.csv':
                        app = CRP(
                            AG_APP=row[1],
                            CRP=row[3],
                        )
                        #print('CRP' + app.AG_APP)
                        db.session.add(app)
                    elif str(file) == 'CON25.csv':
                        app = CON25(
                            AG_APP=row[1],
                            CON25=row[3],
                        )
                        #print('CON25' + app.AG_APP)
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

import_to_model('B:\\Projects\\CAUV\\2020\\Database Cleanup\\automation app\\data')

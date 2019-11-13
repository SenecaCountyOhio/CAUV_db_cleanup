# IF CAUV HOMESITE != GIS HOMESITE:
#   IF GIS HOMESITE IS NOT NONE


# HAS THE APPLICATION BEEN FILED
# IS THERE A HOMESITE ON APPLICATION
# IS THERE A HOMESITE IN GIS
# IF THE HOMESITE ON THE APPLICATION IS > THE HOMESITE
#   MAKE HOMESITE ON APPLICATION EQUAL HOMESITE IN GIS
# IS THERE ROAD/WASTE/POND ON APPLICATION


from .models import (
    CAUVapp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)

def check(x):
    model_CAUVApp = CAUVApp.query.filter(CAUVApp.AG_APP == x).first()
    model_Parcels = Parcels.query.filter(Parcels.AG_APP == x).all()
    model_Homesite = Homesite.query.filter(Homesite.AG_APP == x).first()
    model_CRP = CRP.query.filter(CRP.AG_APP == x).first()
    model_CON25 = CON25.query.filter(CON25.AG_APP == x).first()
    model_ERRORS = ERRORS.query.filter(ERRORS.AG_APP == x).first()

    parcel_acreage = []
    for parcel in model_Parcels:
        combined_acreage.append(int(parcel.DEED))
    total_parcel_acreage = sum(parcel_acreage)


    check_dict = {
        'APP_VALUES': {
            'Commodity_Acres': model_CAUVApp.Commodity_Acres,
            'Hay_Acres': model_CAUVApp.Hay_Acres,
            'Perm_Pasture_Acres': model_CAUVApp.Perm_Pasture_Acres,
            'Noncommercial_Wood_Acres': model_CAUVApp.Noncommercial_Wood_Acres,
            'Commerical_Wood_Acres': model_CAUVApp.Commodity_Acres,
            'Other_Crop_Acres': model_CAUVApp.Other_Crop_Acres,
            'Homesite_Acres': model_CAUVApp.Homesite_Acres,
            'Road_Waste_Pond_Acres': model_CAUVApp.Road_Waste_Pond_Acres,
            'CRP_Acres': model_CAUVApp.CRP_Acres,
            'Con25_Acres': model_CAUVApp.Con25_Acres,
            'Other_Use_Acres': model_CAUVApp.Other_Use_Acres,
            'Stated_Total_Acres': model_CAUVApp.Stated_Total_Acres,
            'Gross_Income_1': model_CAUVApp.Gross_Income_1,
            'Gross_Income_2': model_CAUVApp.Gross_Income_2,
            'Gross_Income_3': model_CAUVApp.Gross_Income_3,
        },
        'GIS_VALUES': {
            'Parcels_Combined_Acres': total_parcel_acreage,
            'Homesite': model_Homesite.HOMESITE,
            'CRP': model_CRP.CRP,
            'CON25': model_CON25.CON25
        },
        'ERRORS': {
            'never_filed': model_ERRORS.never_filed,
            'DEED': model_ERRORS.DEED,
            'STATED': model_ERRORS.STATED,
            'HOMESITE': model_ERRORS.HOMESITE,
            'CRP': model_ERRORS.CRP,
            'CON25': model_ERRORS.CON25,
        }
    }
    return check_dict

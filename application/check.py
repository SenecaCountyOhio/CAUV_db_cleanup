from .models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)

def check(x):
    check_dict = {
        'APP_VALUES': {
            'Commodity_Acres': None,
            'Hay_Acres': None,
            'Perm_Pasture_Acres': None,
            'Noncommercial_Wood_Acres': None,
            'Commerical_Wood_Acres': None,
            'Other_Crop_Acres': None,
            'Homesite_Acres': None,
            'Road_Waste_Pond_Acres': None,
            'CRP_Acres': None,
            'Con25_Acres': None,
            'Other_Use_Acres': None,
            'Stated_Total_Acres': None,
            'Gross_Income_1': None,
            'Gross_Income_2': None,
            'Gross_Income_3': None,
        },
        'GIS_VALUES': {
            'Parcels_Combined_Acres': None,
            'Homesite': None,
            'CRP': None,
            'CON25': None,
        },
        'ERRORS': {
            'never_filed': None,
            'DEED': None,
            'STATED': None,
            'HOMESITE': None,
            'CRP': None,
            'CON25': None,
            'INCOME': None,
        }
    }
    # QUERY MODELS
    model_CAUVApp = CAUVApp.query.filter(CAUVApp.AG_APP == x).first()
    model_Parcels = Parcels.query.filter(Parcels.AG_APP == x).all()
    model_Homesite = Homesite.query.filter(Homesite.AG_APP == x).first()
    model_CRP = CRP.query.filter(CRP.AG_APP == x).first()
    model_CON25 = CON25.query.filter(CON25.AG_APP == x).first()
    model_ERRORS = ERRORS.query.filter(ERRORS.AG_APP == x).first()


    # ADD CAUV APP VALUES TO DICT
    check_dict['APP_VALUES']['Commodity_Acres'] = model_CAUVApp.Commodity_Acres
    check_dict['APP_VALUES']['Hay_Acres'] = model_CAUVApp.Hay_Acres
    check_dict['APP_VALUES']['Perm_Pasture_Acres'] = model_CAUVApp.Perm_Pasture_Acres
    check_dict['APP_VALUES']['Noncommercial_Wood_Acres'] = model_CAUVApp.Noncommercial_Wood_Acres
    check_dict['APP_VALUES']['Commerical_Wood_Acres'] = model_CAUVApp.Commerical_Wood_Acres
    check_dict['APP_VALUES']['Other_Crop_Acres'] = model_CAUVApp.Other_Crop_Acres
    check_dict['APP_VALUES']['Homesite_Acres'] = model_CAUVApp.Homesite_Acres
    check_dict['APP_VALUES']['Road_Waste_Pond_Acres'] = model_CAUVApp.Road_Waste_Pond_Acres
    check_dict['APP_VALUES']['CRP_Acres'] = model_CAUVApp.CRP_Acres
    check_dict['APP_VALUES']['Con25_Acres'] = model_CAUVApp.Con25_Acres
    check_dict['APP_VALUES']['Other_Use_Acres'] = model_CAUVApp.Other_Use_Acres
    check_dict['APP_VALUES']['Stated_Total_Acres'] = model_CAUVApp.Stated_Total_Acres
    check_dict['APP_VALUES']['Gross_Income_1'] = model_CAUVApp.Gross_Income_1
    check_dict['APP_VALUES']['Gross_Income_2'] = model_CAUVApp.Gross_Income_2
    check_dict['APP_VALUES']['Gross_Income_3'] = model_CAUVApp.Gross_Income_3


    # ADD COMBINED ACREAGE VALUE TO DICT
    parcel_acreage = []
    for parcel in model_Parcels:
        try:
            parcel_acreage.append(float(parcel.DEED))
        except:
            parcel_acreage.append(0)
    check_dict['GIS_VALUES']['Parcels_Combined_Acres'] = sum(parcel_acreage)


    # ADD VARIOUS GIS ACREAGE VALUES TO DICT
    if model_Homesite is None:
        check_dict['GIS_VALUES']['Homesite'] = '0'
    else:
        check_dict['GIS_VALUES']['Homesite'] = model_Homesite.HOMESITE
    if model_CRP is None:
        check_dict['GIS_VALUES']['CRP'] = '0'
    else:
        check_dict['GIS_VALUES']['CRP'] = model_CRP.CRP
    if model_CON25 is None:
        check_dict['GIS_VALUES']['CON25'] = '0'
    else:
        check_dict['GIS_VALUES']['CON25'] = model_CON25.CON25


    # ADD ERROR INFO TO DICT
    if model_ERRORS is None:
        check_dict['ERRORS']['never_filed'] = 'FALSE'
        check_dict['ERRORS']['DEED'] = 'FALSE'
        check_dict['ERRORS']['STATED'] = 'FALSE'
        check_dict['ERRORS']['HOMESITE']= 'FALSE'
        check_dict['ERRORS']['CRP'] = 'FALSE'
        check_dict['ERRORS']['CON25'] = 'FALSE'
        check_dict['ERRORS']['INCOME'] = 'FALSE'
    else:
        check_dict['ERRORS']['never_filed'] = model_ERRORS.never_filed
        check_dict['ERRORS']['DEED'] = model_ERRORS.DEED
        check_dict['ERRORS']['STATED'] = model_ERRORS.STATED
        check_dict['ERRORS']['HOMESITE']= model_ERRORS.HOMESITE
        check_dict['ERRORS']['CRP'] = model_ERRORS.CRP
        check_dict['ERRORS']['CON25'] = model_ERRORS.CON25
        check_dict['ERRORS']['INCOME'] = model_ERRORS.INCOME

    return check_dict

from .models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)





def INCOME_check(dict):

    income_sum = dict['APP_VALUES']['Gross_Income_1'] + dict['APP_VALUES']['Gross_Income_2'] + dict['APP_VALUES']['Gross_Income_3']
    if income_sum <= 2500:
        if dict['APP_VALUES']['CALCULATED_ACRES'] < 10:
            return 'FLAG'
        else:
            return ""
    else:
        return ""


def NEVER_FILED_check(dict):
    if dict['APP_VALUES']['CALCULATED_ACRES'] == 0:
        return 'FLAG'
    else:
        return ""


def CALC_V_STATED_check(dict):
    if dict['APP_VALUES']['CALCULATED_ACRES'] != dict['APP_VALUES']['Stated_Total_Acres']:
        return 'FLAG'
    else:
        return ""


def CALC_V_DEED_check(dict):
    if dict['APP_VALUES']['CALCULATED_ACRES'] != dict['GIS_VALUES']['Parcels_Combined_Acres']:
        return 'FLAG'
    else:
        return ""



def STATED_V_DEED_check(dict):
    if dict['APP_VALUES']['Stated_Total_Acres'] != dict['GIS_VALUES']['Parcels_Combined_Acres']:
        return 'FLAG'
    else:
        return ""


def HOMESITE_check(dict):
    if dict['APP_VALUES']['Homesite_Acres'] != dict['GIS_VALUES']['HOMESITE']:
        return 'FLAG'
    else:
        return ""


def CON25_check(dict):
    if dict['APP_VALUES']['Con25_Acres'] != dict['GIS_VALUES']['CON25']:
        return 'FLAG'
    else:
        return ""


def CRP_check(dict):
    if dict['APP_VALUES']['CRP_Acres'] != dict['GIS_VALUES']['CRP']:
        return 'FLAG'
    else:
        return ""


def app_view(x):
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
            'HOMESITE': None,
            'CRP': None,
            'CON25': None,
        },
        'ERRORS': {
            'NEVER_FILED': None,
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

    app_types = [
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
    for each in app_types:
        if getattr(model_CAUVApp, each) == '':
            check_dict['APP_VALUES'][each] = 0
        else:
            try:
                check_dict['APP_VALUES'][each] = float(getattr(model_CAUVApp, each))
            except:
                check_dict['APP_VALUES'][each] = 0

    # CALCULATE TOTAL SUBMITTED ACRES IN APP
    land_values = [
        check_dict['APP_VALUES']['Commodity_Acres'],
        check_dict['APP_VALUES']['Hay_Acres'],
        check_dict['APP_VALUES']['Perm_Pasture_Acres'],
        check_dict['APP_VALUES']['Noncommercial_Wood_Acres'],
        check_dict['APP_VALUES']['Commerical_Wood_Acres'],
        check_dict['APP_VALUES']['Other_Crop_Acres'],
        check_dict['APP_VALUES']['Homesite_Acres'],
        check_dict['APP_VALUES']['Road_Waste_Pond_Acres'],
        check_dict['APP_VALUES']['CRP_Acres'],
        check_dict['APP_VALUES']['Con25_Acres'],
        check_dict['APP_VALUES']['Other_Use_Acres'],
    ]
    sum_app_total = []
    for each in land_values:
        try:
            sum_app_total.append(float(each))
        except:
            sum_app_total.append(0)
    check_dict['APP_VALUES']['CALCULATED_ACRES'] = sum(sum_app_total)


    # ADD COMBINED ACREAGE VALUE TO DICT
    parcel_acreage = []
    for parcel in model_Parcels:
        try:
            parcel_acreage.append(float(parcel.DEED))
        except:
            parcel_acreage.append(0)
    check_dict['GIS_VALUES']['Parcels_Combined_Acres'] = sum(parcel_acreage)


    # ADD VARIOUS GIS ACREAGE VALUES TO DICT
    GIS_types ={
        'HOMESITE': model_Homesite,
        'CRP': model_CRP,
        'CON25': model_CON25,
    }

    for each in GIS_types:
        try:
            check_dict['GIS_VALUES'][each] = float(getattr(GIS_types[each], each))
        except:
            check_dict['GIS_VALUES'][each] = 0

    # ADD ERROR INFO TO DICT

    check_dict['ERRORS']['NEVER_FILED'] = NEVER_FILED_check(check_dict)
    check_dict['ERRORS']['DEED'] = CALC_V_DEED_check(check_dict)
    check_dict['ERRORS']['STATED'] = CALC_V_STATED_check(check_dict)
    check_dict['ERRORS']['HOMESITE']= HOMESITE_check(check_dict)
    check_dict['ERRORS']['CRP'] = CRP_check(check_dict)
    check_dict['ERRORS']['CON25'] = CON25_check(check_dict)
    check_dict['ERRORS']['INCOME'] = INCOME_check(check_dict)

    return check_dict

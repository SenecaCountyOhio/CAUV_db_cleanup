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
    if abs(round(dict['APP_VALUES']['CALCULATED_ACRES'],1) - round(dict['APP_VALUES']['Stated_Total_Acres'],1)) >= 1:
        return 'FLAG'
    else:
        return ""

def CALC_V_DEED_check(dict):
    if abs(round(dict['APP_VALUES']['CALCULATED_ACRES'],1) - round(dict['GIS_VALUES']['Parcels_Combined_Acres'],1)) >= 1:
        return 'FLAG'
    else:
        return ""

def STATED_V_DEED_check(dict):
    if abs(round(dict['APP_VALUES']['Stated_Total_Acres'],1) - round(dict['GIS_VALUES']['Parcels_Combined_Acres'],1)) >= 1:
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

def NEVER_FILED_recommendation(dict):
    #if dict['ERRORS']['NEVER_FILED'] == 'FLAG':
    #   return 'APPLICATION NEVER FILED'
    #else:
    #   return ''
    pass

def recommendation(dict, type, adjust_list):
    dict['RECOMMENDATION'][type] = dict['APP_VALUES'][type]
    #HOMESITE
    try:
        if dict['ERRORS']['HOMESITE'] == 'FLAG':
            homesite_diff = (dict['APP_VALUES']['Homesite_Acres'] - dict['GIS_VALUES']['HOMESITE'])
            dict['RECOMMENDATION']['Homesite_Acres'] = dict['GIS_VALUES']['HOMESITE']
    except:
        homesite_diff = 0
        dict['RECOMMENDATION']['Homesite_Acres'] = dict['APP_VALUES']['Homesite_Acres']

    #CON25
    try:
        if dict['ERRORS']['CON25'] == 'FLAG':
            CON25_diff = (dict['APP_VALUES']['Con25_Acres'] - dict['GIS_VALUES']['CON25'])
            dict['RECOMMENDATION']['Con25_Acres'] = dict['GIS_VALUES']['CON25']
    except:
        CON25_diff = 0
        dict['RECOMMENDATION']['Con25_Acres'] = dict['APP_VALUES']['Con25_Acres']

    #CRP
    try:
        if dict['ERRORS']['CRP'] == 'FLAG':
            CRP_diff = (dict['APP_VALUES']['CRP_Acres'] - dict['GIS_VALUES']['CRP'])
            dict['RECOMMENDATION']['CRP_Acres'] = dict['GIS_VALUES']['CRP']
    except:
        CRP_diff = 0
        dict['RECOMMENDATION']['CRP_Acres'] = dict['APP_VALUES']['CRP_Acres']

    total_diff = homesite_diff + CON25_diff + CRP_diff
    dict['RECOMMENDATION']['Road_Waste_Pond_Acres'] = round(total_diff + dict['APP_VALUES']['Road_Waste_Pond_Acres'],3)

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
        'ERRORS': {},
        'RECOMMENDATION': {
            'NEVER_FILED': None,
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
        try:
            if getattr(model_CAUVApp, each) == '':
                check_dict['APP_VALUES'][each] = 0
            else:
                try:
                    check_dict['APP_VALUES'][each] = float(getattr(model_CAUVApp, each))
                except:
                    check_dict['APP_VALUES'][each] = 0
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
    check_dict['APP_VALUES']['CALCULATED_ACRES'] = round(sum(sum_app_total), 3)


    # ADD COMBINED ACREAGE VALUE TO DICT
    parcel_acreage = []
    for parcel in model_Parcels:
        try:
            parcel_acreage.append(float(parcel.DEED))
        except:
            parcel_acreage.append(0)
    check_dict['GIS_VALUES']['Parcels_Combined_Acres'] = round(sum(parcel_acreage),3)


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
    if NEVER_FILED_check(check_dict) != "":
        check_dict['ERRORS']['NEVER_FILED'] = NEVER_FILED_check(check_dict)

    if CALC_V_DEED_check(check_dict) != "":
        check_dict['ERRORS']['DEED'] = CALC_V_DEED_check(check_dict)

    if CALC_V_STATED_check(check_dict) != "":
        check_dict['ERRORS']['STATED'] = CALC_V_STATED_check(check_dict)

    if STATED_V_DEED_check(check_dict) != "":
        check_dict['ERRORS']['STATED_V_DEED'] = STATED_V_DEED_check(check_dict)

    if HOMESITE_check(check_dict) != "":
        check_dict['ERRORS']['HOMESITE'] = HOMESITE_check(check_dict)

    if CRP_check(check_dict) != "":
        check_dict['ERRORS']['CRP'] = CRP_check(check_dict)

    if CON25_check(check_dict) != "":
        check_dict['ERRORS']['CON25'] = CON25_check(check_dict)

    if INCOME_check(check_dict) != "":
        check_dict['ERRORS']['INCOME'] = INCOME_check(check_dict)

    # ADD RECOMMENDATIONS
    RECOMMENDATION_types = [
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
    adjust_list = [
        'Homesite_Acres',
        'CRP_Acres',
        'Con25_Acres',
        'Road_Waste_Pond_Acres'
    ]
    for each in RECOMMENDATION_types:
        recommendation(check_dict, each, adjust_list)

    # ADD TOTAL CALCULATED RECOMMENDED ACRES
    land_values = [
        check_dict['RECOMMENDATION']['Commodity_Acres'],
        check_dict['RECOMMENDATION']['Hay_Acres'],
        check_dict['RECOMMENDATION']['Perm_Pasture_Acres'],
        check_dict['RECOMMENDATION']['Noncommercial_Wood_Acres'],
        check_dict['RECOMMENDATION']['Commerical_Wood_Acres'],
        check_dict['RECOMMENDATION']['Other_Crop_Acres'],
        check_dict['RECOMMENDATION']['Homesite_Acres'],
        check_dict['RECOMMENDATION']['Road_Waste_Pond_Acres'],
        check_dict['RECOMMENDATION']['CRP_Acres'],
        check_dict['RECOMMENDATION']['Con25_Acres'],
        check_dict['RECOMMENDATION']['Other_Use_Acres'],
    ]
    sum_app_total = []
    for each in land_values:
        try:
            sum_app_total.append(float(each))
        except:
            sum_app_total.append(0)
    check_dict['RECOMMENDATION']['CALCULATED_ACRES'] = round(sum(sum_app_total),3)


    return check_dict

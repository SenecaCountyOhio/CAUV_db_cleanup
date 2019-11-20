from .models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)

def INCOME_check(app_select, parcel_sum):

    income_sum = (app_select.Gross_Income_1 +
        app_select.Gross_Income_2 +
        app_select.Gross_Income_3)
    if parcel_sum < 10:
        if income_sum <= 2500:
            return 'GROSS INCOME DOES NOT MEET $2500'
        else:
            return ""
    else:
        return ""

def NEVER_FILED_check(app_select, current_sum):
    if  current_sum == 0:
        return 'APPLICATION NEVER FILED'
    else:
        return ""

def CALC_V_STATED_check(app_select, current_sum):
    if abs(
        round(current_sum,1) -
        round(app_select.Stated_Total_Acres,1)
    ) >= 1:
        return 'CALCULATED DOES NOT EQUAL STATED'
    else:
        return ""

def CALC_V_DEED_check(parcel_sum, current_sum):
    if abs(
        round(current_sum,1) -
        round(parcel_sum,1)
    ) >= 1:
        return 'CALCULATED DOES NOT EQUAL DEED'
    else:
        return ""

def STATED_V_DEED_check(app_select, parcel_sum):
    if abs(
        round(app_select.Stated_Total_Acres,1) -
        round(parcel_sum,1)
    ) >= 1:
        return 'STATED ACREAGE DOES NOT EQUAL DEED'
    else:
        return ""

def HOMESITE_check(app_select, homesite_record):
    if app_select.Homesite_Acres != homesite_record:
        return 'HOMESITE DOES NOT EQUAL AG LAND'
    else:
        return ""

def CRP_check(app_select, CRP_record):
    if app_select.CRP_Acres != CRP_record:
        return 'CRP DOES NOT EQUAL AG LAND'
    else:
        return ""

def CON25_check(app_select, CON25_record):
    if app_select.Con25_Acres != CON25_record:
        return 'CON25 DOES NOT EQUAL AG LAND'
    else:
        return ""


def compiled_errors(app_num, parcel_sum, AG_LAND_land, current_sum):
    errors = []
    app_select = CAUVApp.query.filter(CAUVApp.AG_APP == app_num).first()

    if INCOME_check(app_select, parcel_sum) != "":
        errors.append(INCOME_check(app_select, parcel_sum))

    if NEVER_FILED_check(app_select, current_sum) != "":
        errors.append(NEVER_FILED_check(app_select, current_sum))

    if CALC_V_STATED_check(app_select, current_sum) != "":
        pass
        #errors.append(CALC_V_STATED_check(app_select, current_sum))

    if CALC_V_DEED_check(parcel_sum, current_sum) != "":
        errors.append(CALC_V_DEED_check(parcel_sum, current_sum))

    if STATED_V_DEED_check(app_select, parcel_sum) != "":
        pass
        #errors.append(STATED_V_DEED_check(app_select, parcel_sum))

    for each in AG_LAND_land:
        if each['LAND_USE_TYPE'] == 'HOME':
            if HOMESITE_check(app_select, each['LAND_USE_ACRES']) != "":
                errors.append(HOMESITE_check(app_select, each['LAND_USE_ACRES']))
        elif each['LAND_USE_TYPE'] == 'CONP':
            if CRP_check(app_select, each['LAND_USE_ACRES']) != "":
                errors.append(CRP_check(app_select, each['LAND_USE_ACRES']))
        elif each['LAND_USE_TYPE'] == 'CON25':
            if CON25_check(app_select, each['LAND_USE_ACRES']) != "":
                errors.append(CON25_check(app_select, each['LAND_USE_ACRES']))
        else:
            continue

    return errors

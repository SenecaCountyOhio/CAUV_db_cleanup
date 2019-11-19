from .models import (
    AG_LAND
)

def parcel_view(app_num):
    parcels= []
    parcels_dict_list = []
    app_select = AG_LAND.query.filter(AG_LAND.AGAPPL == app_num).all()
    #add all parcels to parcel list
    for row in app_select:
        if row.PARID in parcels:
            continue
        else:
            parcels.append(row.PARID)
    #for parcels in parcel list, get acreages and store in parcel dict, and then append to parcels_dict_list
    for parcel in parcels:
        parcels_dict ={
        "PARID": None,
        "PARCEL_ACREAGE": None,
        }
        parcels_dict['PARID'] = parcel
        parcel_query = AG_LAND.query.filter(
            AG_LAND.AGAPPL == app_num,
            AG_LAND.PARID == parcel
        ).first()
        parcels_dict['PARCEL_ACREAGE'] = round(parcel_query.PARCEL_ACREAGE,3)
        parcels_dict_list.append(parcels_dict)
    return parcels_dict_list

def parcel_sum(parcels_dict_list):
    parcels_sum = []
    for each in parcels_dict_list:
        parcels_sum.append(each['PARCEL_ACREAGE'])
    total_acres = round(sum(parcels_sum),3)
    return total_acres

def land_view(app_num):
    app_select = AG_LAND.query.filter(AG_LAND.AGAPPL == app_num).all()
    land = []
    land_dict_list = []
    #add all land types to land list
    for row in app_select:
        if row.LAND_USE_TYPE in land:
            continue
        else:
            land.append(row.LAND_USE_TYPE)

    #for land in land list, get acreage sum of each type and store in land_dict
    for type in land:
        land_dict = {
        "LAND_USE_TYPE": None,
        "LAND_USE_ACRES": None,
        }
        land_dict['LAND_USE_TYPE'] = type
        land_query = AG_LAND.query.filter(
            AG_LAND.AGAPPL == app_num,
            AG_LAND.LAND_USE_TYPE == type
        ).all()
        land_type_sum = []
        for each in land_query:
            land_type_sum.append(each.LAND_USE_ACRES)
        land_dict['LAND_USE_ACRES'] = round(sum(land_type_sum),3)
        land_dict_list.append(land_dict)
    return land_dict_list

def land_sum(land_dict_list):
    land_sum = []
    for each in land_dict_list:
        land_sum.append(each['LAND_USE_ACRES'])
    total_acres = round(sum(land_sum),3)
    return total_acres

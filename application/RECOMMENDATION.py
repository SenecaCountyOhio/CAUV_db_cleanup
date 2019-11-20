from .models import (
    CAUVApp,
    AG_LAND,
)



def recommendation(app_select, AG_LAND_parcel, AG_LAND_land, errors):
    # BASE DATA MODEL FOR RECOMMENDED VALUES
    recommendation_values = {
        'Commodity_Acres': app_select.Commodity_Acres,
        'Hay_Acres': app_select.Hay_Acres,
        'Perm_Pasture_Acres': app_select.Perm_Pasture_Acres,
        'Noncommercial_Wood_Acres': app_select.Noncommercial_Wood_Acres,
        'Commerical_Wood_Acres': app_select.Commerical_Wood_Acres,
        'Other_Crop_Acres': app_select.Other_Crop_Acres,
        'Homesite_Acres': app_select.Homesite_Acres,
        'Road_Waste_Pond_Acres': app_select.Road_Waste_Pond_Acres,
        'CRP_Acres': app_select.CRP_Acres,
        'Con25_Acres': app_select.Con25_Acres,
        'Other_Use_Acres': app_select.Other_Use_Acres,
        'Stated_Total_Acres': app_select.Stated_Total_Acres,
        'Gross_Income_1': app_select.Gross_Income_1,
        'Gross_Income_2': app_select.Gross_Income_2,
        'Gross_Income_3': app_select.Gross_Income_3,
    }
    # ADJUST HOME, CONP, CON25 IF NECESSARY
    temp_adjust = {
        'Commodity_Acres': app_select.Commodity_Acres,
        'Hay_Acres': app_select.Hay_Acres,
        'Perm_Pasture_Acres': app_select.Perm_Pasture_Acres,
        'Noncommercial_Wood_Acres': app_select.Noncommercial_Wood_Acres,
        'Commerical_Wood_Acres': app_select.Commerical_Wood_Acres,
        'Homesite_Acres': app_select.Homesite_Acres,
        'Other_Crop_Acres': app_select.Other_Crop_Acres,
        'Road_Waste_Pond_Acres': app_select.Road_Waste_Pond_Acres,
        'CRP_Acres': app_select.CRP_Acres,
        'Con25_Acres': app_select.Con25_Acres,
    }
    # FIRST ADJUST HOME, CRP, CON25
    road_final = []
    for each in AG_LAND_land:
        if each['LAND_USE_TYPE'] == 'HOME':
            temp_adjust['Homesite_Acres'] = each['LAND_USE_ACRES']

        elif each['LAND_USE_TYPE'] == 'CONP':
            temp_adjust['CRP_Acres'] = each['LAND_USE_ACRES']

        elif each['LAND_USE_TYPE'] == 'CON25':
            temp_adjust['Con25_Acres'] = each['LAND_USE_ACRES']

        elif each['LAND_USE_TYPE'] == 'CROP':
            temp_adjust['Commodity_Acres'] = (
                each['LAND_USE_ACRES'] -
                app_select.Hay_Acres -
                app_select.Perm_Pasture_Acres -
                app_select.Other_Crop_Acres
            )
        elif each['LAND_USE_TYPE'] == 'WOOD':
            temp_adjust['Noncommercial_Wood_Acres'] = (
                each['LAND_USE_ACRES'] -
                app_select.Commerical_Wood_Acres
            )
        elif each['LAND_USE_TYPE'] == 'ROW':
                road_final.append(each['LAND_USE_ACRES'])

        elif each['LAND_USE_TYPE'] == 'DTCH':
                road_final.append(each['LAND_USE_ACRES'])

        elif each['LAND_USE_TYPE'] == 'WSTE':
                road_final.append(each['LAND_USE_ACRES'])

        else:
            pass

    temp_adjust['Road_Waste_Pond_Acres'] = round(sum(road_final),3)
    recommendation_values['Commodity_Acres'] = temp_adjust['Commodity_Acres']
    recommendation_values['Hay_Acres'] = temp_adjust['Hay_Acres']
    recommendation_values['Perm_Pasture_Acres'] = temp_adjust['Perm_Pasture_Acres']
    recommendation_values['Noncommercial_Wood_Acres'] = temp_adjust['Noncommercial_Wood_Acres']
    recommendation_values['Commerical_Wood_Acres'] = temp_adjust['Commerical_Wood_Acres']
    recommendation_values['Other_Crop_Acres'] = temp_adjust['Other_Crop_Acres']
    recommendation_values['Road_Waste_Pond_Acres'] = temp_adjust['Road_Waste_Pond_Acres']
    recommendation_values['Homesite_Acres'] = temp_adjust['Homesite_Acres']
    recommendation_values['CRP_Acres'] = temp_adjust['CRP_Acres']
    recommendation_values['Con25_Acres'] = temp_adjust['Con25_Acres']
    return recommendation_values


def recommendation_sum(recommendation_values):
    app_select = recommendation_values
    app_sum = [
        app_select['Commodity_Acres'],
        app_select['Hay_Acres'],
        app_select['Noncommercial_Wood_Acres'],
        app_select['Perm_Pasture_Acres'],
        app_select['Commerical_Wood_Acres'],
        app_select['Other_Crop_Acres'],
        app_select['Homesite_Acres'],
        app_select['Road_Waste_Pond_Acres'],
        app_select['CRP_Acres'],
        app_select['Con25_Acres'],
        app_select['Other_Use_Acres'],
    ]
    return round(sum(app_sum),3)

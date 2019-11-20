from .models import (
    CAUVApp,
    AG_LAND,
)



def recommendation(app_num, AG_LAND_parcel, AG_LAND_land, errors):
    app_select = CAUVApp.query.filter(CAUVApp.AG_APP == app_num).first()
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
    diffs = []
    road_final = []
    temp_adjust = {
            'Homesite_Acres': app_select.Homesite_Acres,
            'Road_Waste_Pond_Acres': app_select.Road_Waste_Pond_Acres,
            'CRP_Acres': app_select.CRP_Acres,
            'Con25_Acres': app_select.Con25_Acres,
    }
    for each in AG_LAND_land:
        if each['LAND_USE_TYPE'] == 'HOME':
            if "HOMESITE DOES NOT EQUAL AG LAND" in errors:
                homesite_diff = app_select.Homesite_Acres - each['LAND_USE_ACRES']
                diffs.append(homesite_diff)
                temp_adjust['Homesite_Acres'] = each['LAND_USE_ACRES']
            else:
                pass

        elif each['LAND_USE_TYPE'] == 'CONP':
            if 'CRP DOES NOT EQUAL AG LAND' in errors:
                CRP_diff = app_select.CRP_Acres - each['LAND_USE_ACRES']
                diffs.append(CRP_diff)
                temp_adjust['CRP_Acres'] = each['LAND_USE_ACRES']
            else:
                pass

        elif each['LAND_USE_TYPE'] == 'CON25':
            if 'CON25 DOES NOT EQUAL AG LAND' in errors:
                CON25_diff = app_select.Con25_Acres - each['LAND_USE_ACRES']
                diffs.append(CON25_diff)
                temp_adjust['Con25_Acres'] = each['LAND_USE_ACRES']
            else:
                pass
        else:
            pass

    #if round(sum(road_final) - app_select.Road_Waste_Pond_Acres,3) >= 0:
    road_final = round(app_select.Road_Waste_Pond_Acres + sum(diffs),3)
    if road_final >= 0:
        recommendation_values['Road_Waste_Pond_Acres'] = road_final
        recommendation_values['Homesite_Acres'] = temp_adjust['Homesite_Acres']
        recommendation_values['CRP_Acres'] = temp_adjust['CRP_Acres']
        recommendation_values['Con25_Acres'] = temp_adjust['Con25_Acres']
    else:
        pass

    return recommendation_values



def recommendation_sum(recommendation_values):
    app_select = recommendation_values
    app_sum = [
        app_select['Commodity_Acres'],
        app_select['Hay_Acres'],
        app_select['Noncommercial_Wood_Acres'],
        app_select['Commerical_Wood_Acres'],
        app_select['Other_Crop_Acres'],
        app_select['Homesite_Acres'],
        app_select['Road_Waste_Pond_Acres'],
        app_select['CRP_Acres'],
        app_select['Con25_Acres'],
        app_select['Other_Use_Acres'],
    ]
    return round(sum(app_sum),3)

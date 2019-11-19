from .models import (
    CAUVApp,
    AG_LAND,
)



def recommendation(app_num, AG_LAND_parcel, AG_LAND_land, errors):
    app_select = CAUVApp.query.filter(CAUVApp.AG_APP == app_num).first()
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

    for each in AG_LAND_land:
        diffs = []
        if each['LAND_USE_TYPE'] == 'HOME':
            if "HOMESITE DOES NOT EQUAL AG LAND" in errors:
                homesite_diff = round(app_select.Homesite_Acres,3) - each['LAND_USE_ACRES']
                road_recommend = round(app_select.Road_Waste_Pond_Acres,3) + homesite_diff
                if road_recommend >= 0:
                    recommendation_values['Homesite_Acres'] = each['LAND_USE_ACRES']
                    recommendation_values['Road_Waste_Pond_Acres'] = road_recommend
                else:
                    pass
            else:
                pass

        elif each['LAND_USE_TYPE'] == 'CONP':
            if 'CRP DOES NOT EQUAL AG LAND' in errors:
                CRP_diff = round(app_select.CRP_Acres,3) - each['LAND_USE_ACRES']
                road_recommend = round(app_select.Road_Waste_Pond_Acres,3) + CRP_diff
                if road_recommend >= 0:
                    recommendation_values['CRP_Acres'] = each['LAND_USE_ACRES']
                    recommendation_values['Road_Waste_Pond_Acres'] = road_recommend
                else:
                    pass
            else:
                pass

        elif each['LAND_USE_TYPE'] == 'CON25':
            if 'CON25 DOES NOT EQUAL AG LAND' in errors:
                CON25_diff = round(app_select.Con25_Acres,3) - each['LAND_USE_ACRES']
                road_recommend = round(app_select.Road_Waste_Pond_Acres,3) + CON25_diff
                if road_recommend >= 0:
                    recommendation_values['Con25_Acres'] = each['LAND_USE_ACRES']
                    recommendation_values['Road_Waste_Pond_Acres'] = road_recommend
                else:
                    pass
            else:
                pass
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

from .models import (
    CAUVApp,
    Parcels,
    Homesite,
    CRP,
    CON25,
    ERRORS,
)

def current_app_sum(app_num):
    app_select = CAUVApp.query.filter(CAUVApp.AG_APP == app_num).first()
    app_sum = [
        app_select.Commodity_Acres,
        app_select.Hay_Acres,
        app_select.Noncommercial_Wood_Acres,
        app_select.Commerical_Wood_Acres,
        app_select.Other_Crop_Acres,
        app_select.Homesite_Acres,
        app_select.Road_Waste_Pond_Acres,
        app_select.CRP_Acres,
        app_select.Con25_Acres,
        app_select.Other_Use_Acres,
    ]
    return round(sum(app_sum),3)

def current_app(app_num):
    app_select = CAUVApp.query.filter(CAUVApp.AG_APP == app_num).first()
    check_dict = {
        'APP_VALUES': {
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
        },
        'GIS_VALUES': {
            'Parcels_Combined_Acres': None,
            'HOMESITE': None,
            'CRP': None,
            'CON25': None,
        }
    }

    return check_dict

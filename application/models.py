from . import db
from datetime import datetime


class CAUVApp(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    AG_APP = db.Column(
        type_=db.String(30),
        nullable=False
    )
    Commodity_Acres = db.Column(
        type_=db.Float(3),
    )
    Hay_Acres = db.Column(
        type_=db.Float(3),
    )
    Perm_Pasture_Acres = db.Column(
        type_=db.Float(3),
    )
    Noncommercial_Wood_Acres = db.Column(
        type_=db.Float(3),
    )
    Commerical_Wood_Acres = db.Column(
        type_=db.Float(3),
    )
    Other_Crop_Acres = db.Column(
        type_=db.Float(3),
    )
    Homesite_Acres = db.Column(
        type_=db.Float(3),
    )
    Road_Waste_Pond_Acres = db.Column(
        type_=db.Float(3),
    )
    CRP_Acres = db.Column(
        type_=db.Float(3),
    )
    Con25_Acres = db.Column(
        type_=db.Float(3),
    )
    Other_Use_Acres = db.Column(
        type_=db.Float(3),
    )
    Stated_Total_Acres = db.Column(
        type_=db.Float(3),
        nullable=False,
    )
    Gross_Income_1 = db.Column(
        type_=db.Float(2),
    )
    Gross_Income_2 = db.Column(
        type_=db.Float(2),
    )
    Gross_Income_3 = db.Column(
        type_=db.Float(2),
    )


class AG_LAND(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    PARID = db.Column(
        type_=db.String(30),
    )
    AGAPPL = db.Column(
        type_=db.String(30),
    )
    PARCEL_ACREAGE = db.Column(
        type_=db.Float(3),
    )
    LAND_USE_TYPE = db.Column(
        type_=db.String(30),
    )
    LAND_USE_ACRES = db.Column(
        type_=db.Float(3),
    )


class RECOMMENDED_CAUVApp(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    AG_APP = db.Column(
        type_=db.String(30),
        nullable=False
    )
    Commodity_Acres = db.Column(
        type_=db.Float(3),
    )
    Hay_Acres = db.Column(
        type_=db.Float(3),
    )
    Perm_Pasture_Acres = db.Column(
        type_=db.Float(3),
    )
    Noncommercial_Wood_Acres = db.Column(
        type_=db.Float(3),
    )
    Commerical_Wood_Acres = db.Column(
        type_=db.Float(3),
    )
    Other_Crop_Acres = db.Column(
        type_=db.Float(3),
    )
    Homesite_Acres = db.Column(
        type_=db.Float(3),
    )
    Road_Waste_Pond_Acres = db.Column(
        type_=db.Float(3),
    )
    CRP_Acres = db.Column(
        type_=db.Float(3),
    )
    Con25_Acres = db.Column(
        type_=db.Float(3),
    )
    Other_Use_Acres = db.Column(
        type_=db.Float(3),
    )
    Stated_Total_Acres = db.Column(
        type_=db.Float(3),
        nullable=False,
    )
    Gross_Income_1 = db.Column(
        type_=db.Float(2),
    )
    Gross_Income_2 = db.Column(
        type_=db.Float(2),
    )
    Gross_Income_3 = db.Column(
        type_=db.Float(2),
    )

from . import db
from datetime import datetime

class CAUVApp(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    user = db.Column(
        type_=db.String(30),
        nullable=False,
    )
    AG_APP = db.Column(
        type_=db.String(30),
        nullable=False
    )
    Parcel_Change_Check = db.Column(
        type_=db.String(4),
        nullable=False
    )
    Parcel_Change_Note = db.Column(
        type_=db.String(150),
        )
    Parcels_Combined_Acres = db.Column(
        type_=db.String(30),
        nullable=False,
    )
    Commodity_Acres = db.Column(
        type_=db.String(30),
    )
    Hay_Acres = db.Column(
        type_=db.String(30),
    )
    Perm_Pasture_Acres = db.Column(
        type_=db.String(30),
    )
    Noncommercial_Wood_Acres = db.Column(
        type_=db.String(30),
    )
    Commerical_Wood_Acres = db.Column(
        type_=db.String(30),
    )
    Other_Crop_Acres = db.Column(
        type_=db.String(30),
    )
    Homesite_Acres = db.Column(
        type_=db.String(30),
    )
    Road_Waste_Pond_Acres = db.Column(
        type_=db.String(30),
    )
    CRP_Acres = db.Column(
        type_=db.String(30),
    )
    Con25_Acres = db.Column(
        type_=db.String(30),
    )
    Other_Use_Acres = db.Column(
        type_=db.String(30),
    )
    Stated_Total_Acres = db.Column(
        type_=db.String(30),
        nullable=False,
    )
    Farmed_Acres_1 = db.Column(
        type_=db.String(30),
    )
    Farmed_Acres_2 = db.Column(
        type_=db.String(30),
    )
    Farmed_Acres_3 = db.Column(
        type_=db.String(30),
    )
    Use_of_Land_1 = db.Column(
        type_=db.String(30),
    )
    Use_of_Land_2 = db.Column(
        type_=db.String(30),
    )
    Use_of_Land_3 = db.Column(

        type_=db.String(30),
    )
    Units_Acre_1 = db.Column(
        type_=db.String(30),
    )
    Units_Acre_2 = db.Column(
        type_=db.String(30),
    )
    Units_Acre_3 = db.Column(
        type_=db.String(30),
    )
    Price_Unit_1 = db.Column(
        type_=db.String(30)
    )
    Price_Unit_2 = db.Column(
        type_=db.String(30),
    )
    Price_Unit_3 = db.Column(
        type_=db.String(30),
    )
    Gross_Income_1 = db.Column(
        type_=db.String(30),
    )
    Gross_Income_2 = db.Column(
        type_=db.String(30),
    )
    Gross_Income_3 = db.Column(
        type_=db.String(30),
    )
    date_added = db.Column(
        type_=db.DateTime,
        default=datetime.utcnow,
    )

class Parcels(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    PARID = db.Column(
        type_=db.String(30),
    )
    AGAPP = db.Column(
        type_=db.String(30),
    )
    DEED = db.Column(
        type_=db.String(30),
    )
    NAME1 = db.Column(
        type_=db.String(30),
    )
    NAME2 = db.Column(
        type_=db.String(30),
    )

class Homesite(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    AG_APP = db.Column()
    HOMESITE = db.Column()


class CRP(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    AG_APP = db.Column()
    CRP = db.Column()


class CON25(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    AG_APP = db.Column(
        type_=db.String(30),
    )
    CON25 = db.Column(
        type_=db.String(30),
    )

class ERRORS(db.Model):
    id = db.Column(
        type_=db.Integer,
        primary_key=True,
    )
    AG_APP = db.Column(
        type_=db.String(30),
    )
    never_filed = db.Column(
        type_=db.String(30),
    )
    DEED = db.Column(
        type_=db.String(30),
    )
    STATED = db.Column(
        type_=db.String(30),
    )
    HOMESITE = db.Column(
        type_=db.String(30),
    )
    CRP = db.Column(
        type_=db.String(30),
    )
    CON25 = db.Column(
        type_=db.String(30),
    )

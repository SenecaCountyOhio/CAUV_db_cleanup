import csv
import os
import sys
from application import db, create_app
from application.models import (
    CAUVApp,
    RECOMMENDED_CAUVApp,
)
from application.AG_LAND import (
    parcel_view,
    parcel_sum,
    land_view,
    land_sum,
)
from application.ERRORS import compiled_errors
from application.RECOMMENDATION import recommendation, recommendation_sum
from application.CURRENT import current_app, current_app_sum

app = create_app()
app.app_context().push()

all_apps = db.session.query(CAUVApp)


def return_list():
    query = []
    for each in all_apps:
        id = each.AG_APP
        parcel_list = parcel_view(id)
        parcel_list_sum = parcel_sum(parcel_list)
        land_list = land_view(id)
        land_list_sum = land_sum(land_list)
        if land_list_sum == parcel_list_sum:
            continue
        else:
            output1 = "|APP: " + id
            output2 = "|PARCEL: " + str(parcel_list_sum)
            output3 = "|AG LAND: " + str(land_list_sum)
            final_output = output1 + output2 + output3
            query.append(final_output)
    print(query)

return_list()

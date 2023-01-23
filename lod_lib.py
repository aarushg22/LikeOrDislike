from data_models import LocationData
from flask import jsonify, make_response
from utils import get_location


class LikeOrDislike:
    def getLocationsLODdata(self, get_data):
        location = get_location(get_data)
        if not location:
            return make_response(
                jsonify(
                    {"message": 'Location not found'}
                ),
                400,
            )
        else:
            return jsonify(location.to_json())

    def updateLocationsLODdata(self, location_lod_data: LocationData, liked: bool):
        print(location_lod_data)
        location_data = get_location(location_lod_data)
        if not location_data:
            return make_response(
                jsonify(
                    {"message": 'Location not found'}
                ),
                400,
            )
        else:
            if liked:
                location_data.update(inc__likes=1)
            else:
                location_data.update(inc__dislikes=1)
            location_data.save()
            return jsonify(location_data.to_json())

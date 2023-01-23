from data_models import LocationData


def get_location(location_json_data):
    continent = location_json_data['continent']
    country = location_json_data['country'] if \
        'country' in location_json_data else ''
    state = location_json_data['state'] if \
        'state' in location_json_data else ''
    city = location_json_data['city'] if \
        'city' in location_json_data else ''

    return LocationData.objects(continent=continent,
                                country=country,
                                state=state,
                                city=city).first()

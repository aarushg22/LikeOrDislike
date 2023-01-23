from config import LOCATIONS
from data_models import LocationData


def initDB():
    LocationData.drop_collection()
    print(f'Initializing with locations...')
    for location in LOCATIONS:
        locationData = LocationData(**{
            'continent': location,
            'country': "",
            'state': "",
            'city': "",
            'likes': 0,
            'dislikes': 0
        })
        locationData.save()
        print(location)

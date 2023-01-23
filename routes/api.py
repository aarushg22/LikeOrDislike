"""The Endpoints to manage the BOOK_REQUESTS"""
from flask import request, Blueprint

from lod_lib import LikeOrDislike

lod = LikeOrDislike()

# from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API


@REQUEST_API.route('/locations/fetch', methods=['POST'])
def get_records():
    return lod.getLocationsLODdata(request.get_json())


@REQUEST_API.route('/locations/like', methods=['POST'])
def post_like_records():
    return lod.updateLocationsLODdata(request.get_json(), True)


@REQUEST_API.route('/locations/dislike', methods=['POST'])
def post_dislike_records():
    return lod.updateLocationsLODdata(request.get_json(), False)

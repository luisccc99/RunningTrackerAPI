from flask import Blueprint
from flask_restful import Api
from resources.track import Track
from resources.tracks import TrackList
from resources.checkpoints import CheckpointList

tracks_bp = Blueprint('tracks', __name__)
api = Api(tracks_bp)

api.add_resource(Track, '/tracks/:id')
api.add_resource(TrackList, '/tracks')
api.add_resource(CheckpointList, '/tracks/:id/checkpoints')

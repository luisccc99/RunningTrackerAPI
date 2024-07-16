from flask_restful import Resource


class Track(Resource):

    def get(self, trackId):
        return {'message': 'hello world'}

    
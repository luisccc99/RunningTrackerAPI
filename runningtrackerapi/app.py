from flask import Flask
from flask_restful import Api
from blueprints.tracks import tracks_bp

app = Flask(__name__)

app.register_blueprint(tracks_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask , request , render_template
from flask_restx import Resource, Api ,fields
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)  # Flask に Flask-RESTX を導入
CORS(app)

resource_fields = api.model("Json Bodyです", {
    "latitude": fields.Float,
    "longitude": fields.Float
})

@api.route('/emergency' ,methods=['get'])
class emergency(Resource):

    def get(self):
        return {
            "status":"ok"
        }
    
@api.route('/emergency/no' ,methods=['get'])
class emergency(Resource):
    
    def get(self):
        return {
            "status":"no",
            "latitude":100.0,
            "longitude":70.0

        }

@api.route('/location', methods=['post'])
class Location(Resource):

    @api.doc(body=resource_fields)
    def post(self):    
        lat = request.json['latitude']
        lon = request.json['longitude']

        return {
            "status":"ok",
            "latitude":lat,
            "longitude":lon
        }

## おまじない
if __name__ == "__main__":
    app.run(debug=False)
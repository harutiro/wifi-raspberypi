from flask import Flask , request , render_template
from flask_restx import Resource, Api ,fields

app = Flask(__name__)
api = Api(app)  # Flask に Flask-RESTX を導入

resource_fields = api.model("Json Bodyです", {
    "latitude": fields.Float,
    "longitude": fields.Float
})


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
    app.run(debug=True)
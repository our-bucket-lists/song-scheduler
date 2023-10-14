from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('code', required=True, type=str)
parser.add_argument('group', required=True, type=str)





@api.route('/api/v1/request')
class Requests(Resource):
    @api.expect(parser)
    def get(self):
        result = []
        return jsonify(result)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class RegistUser(Resource):
    def post(self):
        return {'result': 'ok'}

api.add_resource(RegistUser, '/user')

if __name__ == "__main__":
    app.run()
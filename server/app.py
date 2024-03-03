#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        response = {"message": "Welcome to the Plants RESTful API"}
        return make_response(response, 200)
    
api.add_resource(Home, '/')

class Plants(Resource):
    def get(self):
        plants_dict_list = [plant.to_dict() for plant in Plant.query.all()]
        return make_response(plants_dict_list, 200)
    
    def post(self):
        new_plant = Plant(
            name = request.get_json().get("name"),
            image = request.get_json().get("image"),
            price = request.get_json().get("price")
        )
        db.session.add(new_plant)
        db.session.commit()

        return make_response(new_plant.to_dict(), 201)
        
api.add_resource(Plants, '/plants')
    
class PlantByID(Resource):
    def get(self, id):
        plant = Plant.query.filter_by(id=id).first().to_dict()
        return make_response(plant, 200)

api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

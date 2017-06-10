"""
The main file - this starts our web server and registers our resources.
The handlers are implemented here just as a way of making things easier and
our Permutator is used as a global, again just to keep things simple.
"""
import com.sirius.logging_config
import logging

logger = logging.getLogger(__name__)

from com.sirius.permutations.permutator import Permutator

from flask import Flask, request, abort
from flask_restful import Resource, Api
from com.sirius.permutations.permutator import Permutator
from com.sirius.permutations.notfoundexception import NotFoundException

app = Flask(__name__)
api = Api(app)
permutator = Permutator();

class AddEntity(Resource):
    def post(self):
        try :
            logger.info("Adding a new entity")
            json_data = request.get_json(force = True)
            permutator.register_set(json_data["entityId"], json_data["data"])
            return {"permutations" : permutator.get_permutations(json_data["entityId"])}, 201
        except:
            abort(500)


class SumEntity(Resource):
    def get(self, entityId):
        try :
            logger.info("Summing our permutations")
            return {"sum" : permutator.get_sum(entityId)}, 200
        except NotFoundException :
            abort(404)
        except:
            abort(500)

class UpdateEntity(Resource):
    def post(self):
        try :
            logger.info("Updating entity")
            json_data = request.get_json(force = True)
            return {"permutations" : permutator.adjust_permutation(json_data["entityId"], json_data["add"])}, 200
        except NotFoundException :
            abort(404)
        except:
            abort(500)


api.add_resource(AddEntity, '/addEntity')
api.add_resource(SumEntity, "/sumEntity/<entityId>")
api.add_resource(UpdateEntity, "/updateEntity")


if __name__ == '__main__':
     app.run()
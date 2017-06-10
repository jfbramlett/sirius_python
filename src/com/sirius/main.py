import numbers
print numbers.__file__

import com.sirius.logging_config
import logging

logger = logging.getLogger(__name__)

from com.sirius.permutations.permutator import Permutator

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Get_UUID(Resource):
    def get(self):
        return {"id" : "1"}


api.add_resource(Get_UUID, '/')

if __name__ == '__main__':
     app.run()
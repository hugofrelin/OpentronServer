from flask_restx import Api
from flask import Blueprint
from flask_cors import CORS

from .main.controllers.protocols_controller import api as protocols_ns
from .main.controllers.sessions_controller import api as sessions_ns
from .main.controllers.networks_controller import api as networks_ns


blueprint = Blueprint('api', __name__)
CORS(blueprint, supports_credentials=True)

api = Api(blueprint,
          title='OPENTRON CONTROLLER API',
          version='1.0',
          description='a server for controlling the Opentron Robots'
          )

api.add_namespace(protocols_ns, path='/protocol' )
api.add_namespace(sessions_ns, path='/session')
api.add_namespace(networks_ns, path='/network')

from flask import request
from flask_restx import Resource
from ..utils.dto import NetworksDto
from ..services.networks_service import scan_for_robots

api = NetworksDto.api

@api.route('/')
class Network(Resource):

    @api.doc('Scans the neteork for Robots')
    @api.marshal_with(NetworksDto.network_model)
    def get(self):
        ''' Scans the network to see if the hardcoded robots are available '''
        return scan_for_robots()

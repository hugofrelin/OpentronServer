from flask import request
from flask_restx import Resource
from ..utils.dto import ProtocolsDto
from ..services.protocols_service import delete_protocol, upload_protocol


api = ProtocolsDto.api


@api.route('/')
class Protocol(Resource):

    @api.doc('Uploads the protocol')
    @api.expect(ProtocolsDto.upload_protocol_parser, validate=True)
    @api.marshal_with(ProtocolsDto.protocol_id_model)
    def post(self):
        ''' Uploads protocol named filename to the
            Opentron Robot with IP Adress robot_ip '''

        data = ProtocolsDto.upload_protocol_parser.parse_args()
        print(data['protocol_file'].filename)
        return upload_protocol(data['robot_ip'], data['protocol_file'].stream)

    @api.doc('Deletes the protocol')
    @api.param('robot_ip', 'The IP Adress of the robot')
    @api.param('protocol_id', 'The ID of the protocol')
    @api.marshal_with(ProtocolsDto.response_model)
    def delete(self):
        ''' Deletes the protocol_id with ID protocol_id from
            Opentron Robot with IP Adress robot_ip '''

        robot_ip = request.args.get('robot_ip')
        protocol_id = request.args.get('protocol_id')
        return delete_protocol(robot_ip, protocol_id)

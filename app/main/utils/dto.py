import werkzeug
from flask_restx import Namespace, fields, reqparse


class SessionsDto:
    api = Namespace("Sessions", description="A session initiated on the Opentron")

    response_model = api.model("response_model", {
        "response": fields.String(example="<Response 200>")
    })

    current_state_model = api.model("current_state_model", {
        "current_state": fields.String(example="loading")
    })

    session_id_model = api.model("session_id_model", {
        "session_id": fields.String(example="27d6390-3d1f-4b20-8d9c-25bfe925657a")
    })

    session_and_robot_ip_model = api.model("session_and_robot_ip_model", {
        "session_id": fields.String(example="27d6390-3d1f-4b20-8d9c-25bfe925657a"),
        "robot_ip": fields.String(example="192.168.1.0"),
    })

    protocol_and_robot_ip_model = api.model("protocol_and_robot_ip_model", {
        "protocol_id": fields.String(example="protocol"),
        "robot_ip": fields.String(example="192.168.1.0"),
    })


class ProtocolsDto:
    api = Namespace("Protocols", description="A protocol that user wants to run on the Opentron")

    protocol_id_model = api.model("protocol_id_model", {
        "protocol_id": fields.String(example="protocol")
    })

    response_model = api.model("response_model", {
        "response": fields.String(example="<Response 200>")
    })

    upload_protocol_parser = reqparse.RequestParser()
    upload_protocol_parser.add_argument(
        "protocol_file",
        type=werkzeug.datastructures.FileStorage,
        location="files",
        required=True,
        help="This is a python file with the robot protocol"
    )
    upload_protocol_parser.add_argument(
        "robot_ip",
        type=str,
        location="form",
        required=True,
    )


class NetworksDto:
    api = Namespace("Networks", description="Used to find all the Opentrons available on the network")

    robot_model = api.model('RobotModel',{
        'IP': fields.String(example='192.168.1.0'),
        'Available': fields.String(example='YES')
    })

    network_model = api.model("network_model", {
        'VULCAN': fields.Nested(robot_model),
        'CERES': fields.Nested(robot_model),
        'HERCULES': fields.Nested(robot_model),
        'ISABELA': fields.Nested(robot_model),
        'MINERVA': fields.Nested(robot_model),
    })

from flask import request
from flask_restx import Resource
from ..utils.dto import SessionsDto
from ..services.sessions_service import (create_session, run,
        delete_session, pause, resume, cancel, get_current_state)

api = SessionsDto.api


@api.route('/')
class Session(Resource):

    @api.doc('Creates a session')
    @api.expect(SessionsDto.protocol_and_robot_ip_model, validate=True)
    @api.marshal_with(SessionsDto.session_id_model)
    def post(self):
        ''' Creates a session for the protocol with ID "protocol_id"
            Opentron Robot with IP Adress "robot_ip" '''

        data = request.json
        return create_session(data['robot_ip'], data['protocol_id'])

    @api.doc('Deletes the session')
    @api.param('robot_ip', 'The IP Adress of the robot')
    @api.param('session_id', 'The ID of the session')
    @api.marshal_with(SessionsDto.response_model)
    def delete(self):
        ''' Deletes the session with ID "session_id" on
            Opentron Robot with IP Adress "robot_ip" '''

        robot_ip = request.args.get('robot_ip')
        session_id = request.args.get('session_id')
        return delete_session(robot_ip, session_id)

@api.route('/runSession')
class RunSession(Resource):
    @api.doc('Runs the session')
    @api.expect(SessionsDto.session_and_robot_ip_model, validate=True)
    @api.marshal_with(SessionsDto.response_model)
    def post(self):
        ''' Runs the session with ID "session_id" on
            Opentron Robot with IP Adress "robot_ip" '''

        data = request.json
        return run(data['robot_ip'], data['session_id'])
#USE THIS TEMPLATE

@api.route('/pauseSession')
class PauseSession(Resource):
    @api.doc('Pauses the session')
    @api.expect(SessionsDto.session_and_robot_ip_model, validate=True)
    @api.marshal_with(SessionsDto.response_model)
    def post(self):
        ''' Pauses the session with ID "session_id" on
            Opentron Robot with IP Adress "robot_ip" '''

        data = request.json
        return pause(data['robot_ip'], data['session_id'])



@api.route('/resumeSession')
class ResumeSession(Resource):
    @api.doc('Resumes the session')
    @api.expect(SessionsDto.session_and_robot_ip_model, validate=True)
    @api.marshal_with(SessionsDto.response_model)
    def post(self):
        ''' Resumes the session with ID "session_id" on
            Opentron Robot with IP Adress "robot_ip" '''

        data = request.json
        return resume(data['robot_ip'], data['session_id'])


@api.route('/cancelSession')
class CancelSession(Resource):
    @api.doc('Cancels the session')
    @api.expect(SessionsDto.session_and_robot_ip_model, validate=True)
    @api.marshal_with(SessionsDto.response_model)
    def post(self):
        ''' Cancels the session with ID "session_id" on
            Opentron Robot with IP Adress "robot_ip" '''

        data = request.json
        return cancel(data['robot_ip'], data['session_id'])

@api.route('/getState')
class GetState(Resource):
    @api.doc('Gets the current state of the session')
    @api.param('robot_ip', 'The IP Adress of the robot')
    @api.param('session_id', 'The ID of the session')
    @api.marshal_with(SessionsDto.current_state_model)
    def get(self):
        ''' Gets the statis of the session with ID "session_id" on
            Opentron Robot with IP Adress "robot_ip" '''

        robot_ip = request.args.get('robot_ip')
        session_id = request.args.get('session_id')
        return get_current_state(robot_ip, session_id)

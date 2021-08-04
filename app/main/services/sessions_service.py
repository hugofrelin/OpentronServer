import requests
import time
import os


def create_session(robot_ip, protocol_id):
    response = requests.post(
        url=f"http://{robot_ip}:31950/sessions",
        headers={"Opentrons-Version": "2"},
        json={
            "data": {
                "sessionType": "protocol",
                "createParams": {
                    "protocolId": protocol_id
                }
            }
        }
    )

    session_id_dictionary = {
        "session_id": response.json()['data']['id']
    }

    return session_id_dictionary



def run(robot_ip, session_id):
    while True:
        # Sleep for 1/2 a second. It does this to make sure the protocol is uploaded
        # before it runs the session
        time.sleep(.5)

        response = requests.get(
            url=f"http://{robot_ip}:31950/sessions/{session_id}",
            headers={"Opentrons-Version": "2"},
        )

        current_state = response.json()['data']['details']['currentState']
        if current_state == 'loaded':
            break
        elif current_state == 'error':
            raise RuntimeError(f"Error encountered {response.json()}")

    # Send a command to begin a protocol run
    response = requests.post(
        url=f"http://{robot_ip}:31950/sessions/{session_id}/commands/execute",
        headers={"Opentrons-Version": "2"},
        json={"data": {"command": "protocol.startRun", "data": {}}}
    )

    #If else statements think about it

    response_dictionary = {
        "response":str(response)
    }
    return response_dictionary


def delete_session(robot_ip, session_id):
    response = requests.delete(
        url=f"http://{robot_ip}:31950/sessions/{session_id}",
        headers={"Opentrons-Version": "2"},
    )

    response_dictionary = {
        "response":str(response)
    }

    return response_dictionary



def pause(robot_ip, session_id):
    response = requests.post(
        url=f"http://{robot_ip}:31950/sessions/{session_id}/commands/execute",
        headers={"Opentrons-Version": "2"},
        json={"data": {"command": "protocol.pause", "data": {}}}
    )

    response_dictionary = {
        "response":str(response)
    }

    return response_dictionary


def resume(robot_ip, session_id):
    response = requests.post(
        url=f"http://{robot_ip}:31950/sessions/{session_id}/commands/execute",
        headers={"Opentrons-Version": "2"},
        json={"data": {"command": "protocol.resume", "data": {}}}
    )

    response_dictionary = {
        "response":str(response)
    }

    return response_dictionary


def cancel(robot_ip, session_id):
    response = requests.post(
        url=f"http://{robot_ip}:31950/sessions/{session_id}/commands/execute",
        headers={"Opentrons-Version": "2"},
        json={"data": {"command": "protocol.cancel", "data": {}}}
    )

    response_dictionary = {
        "response":str(response)
    }

    return response_dictionary


def get_current_state(robot_ip, session_id):
    response = requests.get(
        url=f"http://{robot_ip}:31950/sessions/{session_id}",
        headers={"Opentrons-Version": "2"},
    )

    current_state_dictionary = {
        "current_state": response.json()['data']['details']['currentState'],
    }
    return current_state_dictionary

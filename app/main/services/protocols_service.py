import requests
import time
import os

def upload_protocol(robot_ip, protocol_file):
    response = requests.post(
        url=f"http://{robot_ip}:31950/protocols",
        headers={"Opentrons-Version": "2"},
        files=[("protocolFile", protocol_file),]
    )
    protocol_id_dictionary = {
        "protocol_id": response.json()['data']['id'],
    }

    return protocol_id_dictionary

def delete_protocol(robot_ip, protocol_id):
    response = requests.delete(
        url=f"http://{robot_ip}:31950/protocols/{protocol_id}",
        headers={"Opentrons-Version": "2"},
    )

    response_dictionary = {
        "response":str(response)
    }

    return response_dictionary

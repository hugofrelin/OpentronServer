from icmplib import multiping

def scan_for_robots():
    ip_dict = {
        '192.0.2.0': 'ROBOT1',
        '192.0.2.0': 'ROBOT2',
        '192.0.2.0': 'ROBOT3',
        '192.0.2.0': 'ROBOT4',
        '192.0.2.0': 'ROBOT5'
    }
    robot_dict = {
        'ROBOT1': {'IP': '192.0.2.0', 'Available': 'unknown'},
        'ROBOT2': {'IP': '192.0.2.0', 'Available': 'unknown'},
        'ROBOT3': {'IP': '192.0.2.0', 'Available': 'unknown'},
        'ROBOT4': {'IP': '192.0.2.0', 'Available': 'unknown'},
        'ROBOT5': {'IP': '192.0.2.0', 'Available': 'unknown'}
    }
    ip_dictionary = []

    for key in robot_dict.keys():
        ip_dictionary.append(robot_dict[key]['IP'])

    hosts = multiping(ip_dictionary)

    for host in hosts:
        robot_name = ip_dict[host.address]
        if host.is_alive:
            robot_dict[robot_name]['Available'] = 'YES'
        else:
            robot_dict[robot_name]['Available'] = 'NO'

    return robot_dict

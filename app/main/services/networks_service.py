from icmplib import multiping

def scan_for_robots():
    ip_dict = {
        '192.168.100.209': 'VULCAN',
        '192.168.100.94': 'CERES',
        '192.168.100.200': 'HERCULES',
        '192.168.100.137': 'ISABELA',
        '192.168.100.179': 'MINERVA'
    }
    robot_dict = {
        'VULCAN': {'IP': '192.168.100.209', 'Available': 'unknown'},
        'CERES': {'IP': '192.168.100.94', 'Available': 'unknown'},
        'HERCULES': {'IP': '192.168.100.200', 'Available': 'unknown'},
        'ISABELA': {'IP': '192.168.100.137', 'Available': 'unknown'},
        'MINERVA': {'IP': '192.168.100.179', 'Available': 'unknown'}
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

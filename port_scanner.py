import socket

def port_scanner(ip, max_ports):
    ports = []
    for port in range(24, max_ports):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout = 1
        result = s.connect_ex((ip, port))
        if result == 0:
            ports.append(port)
        s.close()
    return ports
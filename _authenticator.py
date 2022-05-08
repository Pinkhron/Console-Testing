import socket
import json

server = {
    "ip": "34.199.131.42",
    "port": 25500
}

def auth():
    # Server Connection
    s = socket.socket()
    s.connect((server["ip"], server["port"]))

    # Send Token
    _cfg = open("config.json")
    cfg = json.load(_cfg)
    token = cfg["token"]
    s.sendall(token)

    s.close()
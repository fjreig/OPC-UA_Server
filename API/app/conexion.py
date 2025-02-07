from opcua import Client, ua
import time

def cliente_opc_create():
    url = "opc.tcp://10.116.0.2:4840"
    client = Client(url)
    client.session_timeout = 30000
    client.connect()
    print(f"Connected: {url}")
    return(client)
from socket import *
from fib import fib

# fibinocci program exposed as a microservice

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Received connection from ", addr)
        fib_handler(client)


def fib_handler(client):
    while True :
        req = client.recv(100)
        if not req:
            break

        n = int(req)
        res = fib(n)
        resp = str(res).encode('ascii') + '\n'
        client.send(resp)

    print("Closed...")

    
    
        
fib_server(('',25000))
        


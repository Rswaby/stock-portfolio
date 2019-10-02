import socket                                         
import time



def test():
    # echo_server.py
    import socket

    host = ''        # Symbolic name meaning all available interfaces
    port = 12345     # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("got to here")
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
    print("connection Closed")
    conn.close()
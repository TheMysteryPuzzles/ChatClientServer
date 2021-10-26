from socket import socket
from threading import Thread

def main():

    class ClientSideThread(Thread):

        def __init__(self, client):
            super().__init__()
            self._client = client

        def run(self):
            while running:
                data = self._client.recv(1024)
                print(data.decode('utf-8'))

        nickname = input('Enter Username')
        myclient = socket()
        myclient.connect(('0.0.0.0', 12345))
        running = True
        ClientSideThread(myclient).start()
        while  running:
            content = input('Enter Message: ')
            if content = 'Logout'
                myclient.send(content.encode('utf-8'))
                running = False
            else:
                msg = nickname + ': ' + content
                myclient.send(msg.encode('utf-8'))

if __name__ == '__main__':
    main()
    

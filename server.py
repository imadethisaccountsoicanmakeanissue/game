import socketserver
import socket

# Open up the server.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.0.116', 8080))
def main():
    server.listen(1)
    # Let's wait until a check is sent.
    client, addr = server.accept()
    # If the client is saying 'Do you have an updated version?' then we'll inform the client the current version.
    ver = 1.1
    # send the version to the client.
    client.send(str(ver).encode())
    if client.recv(1024) == b'Lemme update.':
        print('Client is requesting an update.')
        # Get the download link.
        link = "https://raw.githubusercontent.com/imadethisaccountsoicanmakeanissue/game/main/game.py"
        # Send the link to the client.
        client.send(link.encode())
        # Disconnect the client as no more data sending is needed.
        client.close()
        # Go back to detecting for clients.
        main()
main()
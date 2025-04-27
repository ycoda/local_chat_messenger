import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    # ファイルが存在しない場合は何もしません。
    pass

print('starting up on {}'.format(server_address))

sock.bind(server_address)

while True:
    print('\nwaiting to receive message')

    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data.decode())

    response_messasge = input('Enter the response message: ')
    if response_messasge:
        sent = sock.sendto(response_messasge.encode(), address)
        print('sent {} bytes back to {}'.format(sent, address))
import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/tmp/udp_socket_file'
client_address = '/tmp/udp_client_socket_file'

try:
    os.unlink(client_address)
except FileNotFoundError:
    # ファイルが存在しない場合は何もしません。
    pass


sock.bind(client_address)
faker = Faker('ja_JP')
print(faker.name() + 'さん')

try:
    while True:
        message = input('Enter the message to send: ')
        if not message:
            break

        print('sending {!r}'.format(message))
        sent = sock.sendto(message.encode(), server_address)

        print('waiting to receive')
        data, server = sock.recvfrom(4096)

        print('received {!r}'.format(data.decode()))

finally:
    print('closing socket')
    sock.close()
    os.unlink(client_address)
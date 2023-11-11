from socket import socket, AF_INET, SOCK_STREAM


def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)

    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()


def echo_server(address):
    # 创建 socket 对象
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    # 获取本地主机名
    # host = socket.gethostname()
    # sock.bind((host, port))
    # 设置最大连接数，超过后排队
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg = '欢迎访问菜鸟教程！' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

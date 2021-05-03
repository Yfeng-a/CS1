import threading
import socket

def tcp_link(sock,addr):
    #连接成功后打印客户端消息
    print('Accept new connection from {}:{}' .format(*addr))
    # 服务器使用套接字的 send 方法发送数据给客户端
    #注意消息须以字节码的格式传递，使用字符串的encode方法转换
    sock.send('Welcome!'.encode())
    while True:
        #套接字的recv方法为阻塞运行，直到客户端发来消息
        #收到的消息也是字节码，使用 decode方法转换为字符串
        data = sock.recv(1024).decode()
        #如果消息为‘exit‘或者消息为空，退出while循环
        if data == 'exit' or not data:
            break
        sock.send ('Hello, {}'.format (data).encode())
         #关闭临时套接字
    sock.close()
    print('Connection from {}:{}closed.'.format(*addr))

def main():
    #socket 的 gethostname 方法顾名思义可以获取系统的主机名
    #主机名是一个字符串，完全可以用‘localhost’来代替
    #该元祖为地址-接口号元组，将作为套接字的 bind 方法的参数
    #端口号选择大于 1024 小于65536 且未被占用的任何数值
    ADDR = (socket.gethostname(),11231)
    #创建 TCP 服务器套接字
    tcp_server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定地址和端口号
    tcp_server_sock.bind(ADDR)
    #启动监听，监听未来客户端发送的连接请求
    tcp_server_sock.listen()
    print('Waiting for connection')
    #无限循环可以使得服务器套接字接收多个客户端的请求
    while True:
        #套接字的 accept 方法为阻塞运行，直到客户端发来连接请求
        #该方法的返回值为临时套接字和客户端地址的二元元组
        sock.addr = tcp_server_sock.accept()
        #连接成功后创建子线程并启动，处理后续工作
        #然后进入下一个循环，等待其他客户端的连接请求
        t = threading.Thread(target=tcp_link,args=(sock,addr))
        t,start()
    tcp_server_sock.close()

if __name__ == '__main__':
    main()




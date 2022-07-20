# -*- coding:utf-8 -*-
# @Time : 2022/7/20 8:39 下午
# @Author : Bin Bin Xue
# @File : project7_netchatprogram
# @Project : python_basic

'''
    创建一个简单的聊天程序 - 模拟服务器和客户端之间通信
'''
import socket
import argparse

HOST = '127.0.0.1'
PORT = 8080

def listen_socket(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((host,port))
    sock.listen(100)
    return sock

def receive_msg(sock):
    data = bytearray()
    msg = ' '
    while not msg:
        recv = sock.recv(4096)
        if not recv:
            raise ConnectionError()
        data = data + recv
        if b'\0' in recv:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

def prep_msg(msg):
    msg += '\0'
    return msg.encode('utf-8')

def send_msg(sock,msg):
    data = prep_msg(msg)
    sock.sendall(data)

def handle_client(sock,addr):
    try:
        msg = receive_msg(sock)
        print('{}:{}'.format(addr,msg))
        send_msg(sock,msg)
    except (ConnectionError, BrokenPipeError):
        print('Socket错误')
    finally:
        print('与{}连接关闭'.format(addr))
        sock.close()

def server():
    listen_sock = listen_socket(HOST,PORT)
    addr = listen_sock.getsockname()
    print('正在监听：{}'.format(addr))
    while True:
        client_sock, addr=listen_sock.accept()
        print('连接来自：{}'.format(addr))
        handle_client(client_sock,addr)

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))
    while True:
        try:
            print('\n已经连接{}:{}'.format(HOST,PORT))
            print("输入信息，按'enter'发送，'q'键取消")
            msg = input()
            if msg == 'q': break
            send_msg(sock,msg)
            print('发送信息：{}'.format(HOST,PORT))
            msg = receive_msg(sock)
            print('收到回复：'+msg)
        except ConnectionError:
            print('Socket错误')
            break

        finally:
            sock.close()
            print('关闭连接\n')

if __name__ == '__main__':
    choices = {'client': client,'server':server}
    parser = argparse.ArgumentParser(description='聊天小应用')
    parser.add_argument('role',choices=choices,help='选择角色：client或server')
    args = parser.parse_args()
    execute = choices[args.role]
    execute()




# @Time : 2020/12/15 16:11
# @Author : fank
# @Function : details
import socket

from client import Client

if __name__ == '__main__':
    client = Client()
    # client.mset('k1', 'v1', 'k2', ['v2-0', 1, 'v2-2'], 'k3', 'v3')
    # client.mset('k1', 'v1', 'k2', ['v2-0', 1, 'v2-2'], 'k3', 'v3')
    client.set('kx', {'vx': 3})
    print client.get('kx')
    print client.mget('k3', 'k1')

#!/usr/bin/env python3


# author: tcneko <tcneko@outlook.com>
# start from: 2022.02
# last test environment: ubuntu 20.04
# description:


# import
import math
import sys
import time
import ipaddress


# variable
v4_route_size = 1000000
v4_step = int(math.pow(2, 8))

v6_route_size = 200000
v6_step = int(math.pow(2, 80))


# function
def create_v4_route():
    v4_route_list = []
    ix = 0
    while ix < v4_route_size:
        try:
            v4_network = str(ipaddress.IPv4Network(
                str(ipaddress.IPv4Address(v4_step*ix))+"/24"))
            v4_route_list.append(v4_network)
        except:
            pass
        ix = ix + 1
    return v4_route_list


def create_v6_route():
    v6_route_list = []
    ix = 0
    while ix < v6_route_size:
        try:
            v6_network = str(ipaddress.IPv6Network(
                str(ipaddress.IPv6Address(v6_step*ix))+"/48"))
            v6_route_list.append(v6_network)
        except:
            pass
        ix = ix + 1
    return v6_route_list


def main():
    v4_route_list = create_v4_route()
    v6_route_list = create_v6_route()

    message_list = [
        "announce attributes next-hop self nlri {}".format(
            " ".join(v4_route_list)),
        "announce attributes next-hop self nlri {}".format(
            " ".join(v6_route_list))
    ]

    for message in message_list:
        sys.stdout.write(message + '\n')
        sys.stdout.flush()

    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()

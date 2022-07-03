#!/usr/bin/env python3


# author: tcneko <tcneko@outlook.com>
# start from: 2022.02
# last test environment: ubuntu 20.04
# description:


# import
import typer
import math
import time
import ipaddress


# function
def create_v4_route(v4_route_size, v4_mask_length):
    v4_route_list = []
    v4_route_step = int(math.pow(2, 32 - v4_mask_length))
    ix = 0
    while ix < v4_route_size:
        try:
            v4_network = str(ipaddress.IPv4Network(
                str(ipaddress.IPv4Address(v4_route_step * ix)) + "/" + str(v4_mask_length)))
            v4_route_list.append(v4_network)
        except:
            pass
        ix = ix + 1
    return v4_route_list


def create_v6_route(v6_route_size, v6_mask_length):
    v6_route_list = []
    v6_route_step = int(math.pow(2, 128 - v6_mask_length))
    ix = 0
    while ix < v6_route_size:
        try:
            v6_network = str(ipaddress.IPv6Network(
                str(ipaddress.IPv6Address(v6_route_step * ix)) + "/" + str(v6_mask_length)))
            v6_route_list.append(v6_network)
        except:
            pass
        ix = ix + 1
    return v6_route_list


def main(v4_route_size: int = typer.Option(1000000, help="IPv4 route size"),
         v4_mask_length: int = typer.Option(24, help="IPv4 mask length"),
         v6_route_size: int = typer.Option(200000, help="IPv6 route size"),
         v6_mask_length: int = typer.Option(48, help="IPv6 mask length"),
         advertise_v4: bool = typer.Option(
             False, help="Advertise IPv4 routes"),
         advertise_v6: bool = typer.Option(
             False, help="Advertise IPv6 routes")):

    message_list = []

    if advertise_v4:
        v4_route_list = create_v4_route(v4_route_size, v4_mask_length)
        message_list.append(
            "announce attributes next-hop self nlri {}".format(
                " ".join(v4_route_list)))

    if advertise_v6:
        v6_route_list = create_v6_route(v6_route_size, v6_mask_length)
        message_list.append(
            "announce attributes next-hop self nlri {}".format(
                " ".join(v6_route_list)))

    for message in message_list:
        typer.echo(message + '\n')

    while True:
        time.sleep(1)


if __name__ == '__main__':
    typer.run(main)

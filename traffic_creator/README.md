## Traffic Creator

Create traffic using iperf



### How to use

* Build docker image

```bash
cd .../traffic_creator
docker build -t traffic_creator:1.0.0 .
```

* Prepare docker network

```bash
# iperf server network
docker network create \
-d macvlan \
--subnet=192.168.0.0/30 \
--gateway=192.168.0.1 \
-o parent=ae0.10 \
macvlan_ae0_vlan10

# iperf client network
docker network create \
-d macvlan \
--subnet=192.168.0.4/30 \
--gateway=192.168.0.5 \
-o parent=ae0.20 \
macvlan_ae0_vlan20
```

* Run the docker container

```bash
# iperf server container
docker run --rm -it \
--network=macvlan_ae0_vlan10 \
--ip=192.168.0.2 \
--cap-add=NET_ADMIN \
traffic_creator:1.0.0

# iperf client container
docker run --rm -it \
--network=macvlan_ae0_vlan20 \
--ip=192.168.0.6 \
--cap-add=NET_ADMIN \
traffic_creator:1.0.0
```

* Run the test

```bash
# iperf server container
iperf3 -i 10 -p 10001 -s &
iperf3 -i 10 -p 10002 -s &

# iperf client container
iperf3 -i 10 -t 60 -p 10001 -c 192.168.0.2 &
iperf3 -i 10 -t 60 -p 10002 -c 192.168.0.2 &
```


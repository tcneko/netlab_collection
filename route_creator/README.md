## Route Creator

Create BGP routes and send to neighbors using exabgp



### How to use

* Build docker image

```bash
cd netlab_collection/route_creator
docker build -t route_creator:1.0.0 .
```

* Prepare configuration for exabgp

```bash
mkdir -p /opt/route_creator
cp -r .../netlab_collection/route_creator/volume /opt/route_creator
cd /opt/route_creator/volume/opt/route_creator
cp exabgp.conf.j2 exabgp.conf
vim exabgp.conf
```

* Prepare docker network

```
docker network create \
-d macvlan \
--ipv6 \
--subnet=192.168.0.0/30 \
--gateway=192.168.0.1 \
--subnet=fd00::/126 \
--gateway=fd00::1 \
-o parent=ae0.100 \
macvlan_ae0_vlan100
```

* Run the docker container

```bash
# run directly
docker run --rm -it \
--network=macvlan_ae0_vlan100 \
--ip=192.168.0.2 \
--ip6=fd00::2 \
--volume=/opt/route_creator/volume/opt/route_creator:/opt/route_creator \
--cap-add=NET_ADMIN \
-e "exabgp.log.level=WARNING" \
-e "exabgp.api.cli=false" \
-e "exabgp.daemon.user=root" \
-e "exabgp.api.ack=false" \
route_creator:1.0.0 exabgp.conf

# or use docker compose
mkdir -p /opt/route_creator/docker
cp .../netlab_collection/route_creator/docker-compose.yaml.j2 /opt/route_creator/docker
cd /opt/route_creator/docker
cp docker-compose.yaml.j2 docker-compose.yaml
vim docker-compose.yaml
docker-compose up -d
```




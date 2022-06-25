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

# If you want to use ripe rrc monitoring data to create routes
apt-get install mrtparse
bash ./rrc_route_creator.sh

# Or you want to create a specified number of routes
cp sim_route_creator.py route_creator.py
vim route_creator.py
```

* Prepare configuration for docker

```bash
mkdir -p /opt/route_creator/docker
cp .../netlab_collection/route_creator/docker-compose.yaml.j2 /opt/route_creator/docker
cd /opt/route_creator/docker
cp docker-compose.yaml.j2 docker-compose.yaml
vim docker-compose.yaml
```

* Run the docker container

```bash
docker-compose up -d
```


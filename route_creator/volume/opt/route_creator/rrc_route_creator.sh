#!/bin/bash

# author: tcneko <tcneko@outlook.com>
# start from: 2022.06
# last test environment: ubuntu 20.04
# description:

export PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin

# variables
mrtdata_url="http://data.ris.ripe.net/rrc16/latest-bview.gz"

# function
gen_route_creator() {
  if [[ -r latest-bview.gz ]]
  then
    rm -f latest-bview.gz
  fi
  curl -Lo latest-bview.gz ${mrtdata_url}
  mrt2exabgp -G -P ./latest-bview.gz > route_creator.py
  sed -i -E "s/(next-hop ).+( nlri)/\1self\2/g" route_creator.py
}

# main
gen_route_creator

exit 0

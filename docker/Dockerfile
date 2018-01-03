from ubuntu:16.04
run echo "deb http://download.rethinkdb.com/apt xenial main" > /etc/apt/sources.list.d/rethinkdb.list
run apt-get update
run apt-get install -y wget

#install rethinkdb
#run wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -
run apt-get install -y python2.7 python-pip rethinkdb --allow-unauthenticated
run pip install rethinkdb

workdir /acsc
cmd ./firstrun.sh
expose 28015 8080
copy configure_rethink.py configure_rethink.py
copy firstrun.sh firstrun.sh
copy start_services.sh start_services.sh

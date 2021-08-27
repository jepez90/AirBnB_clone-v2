#!/usr/bin/env bash
# install and configure the web server for deploiment web static

apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "It is Working!!!" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data

# configure nginx to serve static content from /hbtn_static/
old_config="listen 80 default_server;"
new_congig="${old_config}\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}\n"
sed -i "s/$old_config/$new_congig/" /etc/nginx/sites-available/default

service nginx restart

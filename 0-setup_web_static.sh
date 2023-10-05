#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
# run script on both web servers.
# checks if Nginx is not installed or not executable

if ! [ -x "$(command -v nginx)" ]; then
	sudo apt update
	sudo apt install nginx
	sudo service nginx start
fi

  # Create necessary folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

sudo chown -R ubuntu:ubuntu /data/

echo " Holberton School" > /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
# check if existd =>remove and recreate
if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
fi

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration to serve /data/web_static/current/ at /hbnb_static
echo "server {
    listen 80;
    server_name example.com ;
	 root /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
		index.html;
    }
    location / {
        # Your other configuration directives, if any
    }
}" > /etc/nginx/sites-available/default

# sudo nginx -t
sudo service nginx restart


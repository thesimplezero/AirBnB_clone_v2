#!/usr/bin/env bash

# Install Nginx if not already installed and create necessary folders
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/{shared,releases/test}


# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

# Create & recreate a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update Nginx config to serve /data/web_static/current at /hbnb_static/
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
#!/usr/bin/env bash
# Install nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML page for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

# Specify source and target directories
source_dir="/data/web_static/releases/test/"
target_dir="/data/web_static/current"

# Check if the symbolic link already exists
if [ -L "$target_dir" ]; then
    sudo rm "$target_dir"
fi

# Create a new symbolic link
sudo ln -s "$source_dir" "$target_dir"


# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# update Nginx config to serve /data/web_static/current at /hbnb_static/
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
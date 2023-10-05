#!/bin/bash

# Constants for directories and config file
WEB_ROOT="/data/web_static"
SHARED_DIR="$WEB_ROOT/shared"
RELEASES_DIR="$WEB_ROOT/releases/test"
NGINX_CONFIG_FILE="/etc/nginx/sites-available/default"

# Function to create a directory if it doesn't exist
create_directory() {
    if [ ! -d "$1" ]; then
        sudo mkdir -p "$1"
    fi
}

# Function to add or update Nginx configuration
update_nginx_config() {
    config_content="location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }"

    if grep -q "location /hbnb_static/" "$NGINX_CONFIG_FILE"; then
        sudo sed -i "/location \/hbnb_static\//c\\$config_content" "$NGINX_CONFIG_FILE"
    else
        sudo sed -i "26i \\\t$config_content" "$NGINX_CONFIG_FILE"
    fi
}

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    echo "Installing Nginx..."
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create required directories
echo "Creating directories if they don't exist..."
create_directory "$SHARED_DIR"
create_directory "$RELEASES_DIR"

# Ensure proper ownership
echo "Setting ownership..."
sudo chown -R ubuntu:ubuntu "$WEB_ROOT"

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee "$RELEASES_DIR/index.html" >/dev/null

# Create and recreate a symbolic link
echo "Creating or recreating symbolic link..."
sudo ln -sf "$RELEASES_DIR" /data/web_static/current

# Update Nginx configuration
echo "Updating Nginx configuration..."
update_nginx_config

# Restart Nginx to apply changes
echo "Restarting Nginx..."
sudo service nginx restart

# Exit with success
echo "Script execution completed successfully."
exit 0

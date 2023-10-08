#!/usr/bin/python3
"""
This module provides a function to deploy a web_static archive to web servers.
"""

from fabric.api import *
import os

# Set the host IP addresses for web-01 and web-02
hosts = ['54.208.71.253', '100.25.144.89']
user = "ubuntu"


def do_deploy(archive_path):
    """
    Deploy an archive to the web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract variables from the archive path
        archive_name = os.path.basename(archive_path)
        archive_folder = "/tmp/" + archive_name.split('.')[0]
        remote_path = "/data/web_static/releases/"

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, archive_folder)

        # Uncompress the archive to the folder in /data/web_static/releases/
        run("mkdir -p {}".format(remote_path + archive_name.split('.')[0]))
        run("tar -xzf {}/{} -C {}".format(archive_folder,
                                          archive_name, remote_path +
                                          archive_name.split('.')[0]))

        # Delete the archive from the web server
        run("rm -f {}/{}".format(archive_folder, archive_name))

        # Move the contents to the appropriate folder and delete web_static
        run("mv {}/{}/web_static/* {}/{}".format(
            remote_path, archive_name.split('.')[0],
            remote_path, archive_name.split('.')[0]))
        run("rm -rf {}/{}".format(remote_path, archive_name.split('.')[0]))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link to the deployed version
        run("ln -s {}/{} /data/web_static/current".format(
            remote_path, archive_name.split('.')[0]))

        return True

    except Exception as e:
        print("Error:", str(e))
        return False

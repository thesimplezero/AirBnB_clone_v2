#!/usr/bin/python3
"""
This fabfile manages the distribution of web_static files to web servers.
"""

import os
from fabric.api import *
from datetime import datetime

# Set the host IP addresses for web-01 and web-02
env.hosts = ['18.234.105.167', '100.25.222.179']
env.user = "ubuntu"


def do_pack():
    """
    Create a tar.gz archive of the web_static directory.
    """
    # Get the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the path where the archive will be saved
    archive_path = f"versions/web_static_{now}.tgz"

    # Create the 'versions' directory if it doesn't exist
    local("mkdir -p versions")

    # Use the 'tar' command to create a compressed archive
    archived = local(f"tar -czvf {archive_path} web_static")

    # Check the archive creation status
    return archive_path if archived.return_code == 0 else None


def do_deploy(archive_path):
    """
    Deploy an archive to the web servers.
    """
    if os.path.exists(archive_path):
        archive = os.path.basename(archive_path)
        a_path = f"/tmp/{archive}"
        folder = os.path.splitext(archive)[0]
        f_path = f"/data/web_static/releases/{folder}/"

        put(archive_path, a_path)
        run(f"mkdir -p {f_path}")
        run(f"tar -xzf {a_path} -C {f_path}")
        run(f"rm {a_path}")
        run(f"mv -f {f_path}web_static/* {f_path}")
        run(f"rm -rf {f_path}web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {f_path} /data/web_static/current")

        return True

    return False


def deploy():
    """
    Create an archive and deploy it to the web servers.
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)

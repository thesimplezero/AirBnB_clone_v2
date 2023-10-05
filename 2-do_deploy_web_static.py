#!/usr/bin/python3
"""
This fabfile manages the distribution of web_static files to web servers.
"""

import os
from fabric.api import *
from datetime import datetime

# Set the host IP addresses for web-01 && web-02
env.hosts = ['54.208.71.253', '100.25.144.89']
env.user = "ubuntu"


def do_pack():
    """Create a tar.gz archive of web_static."""

    # Obtain the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Construct the path where the archive will be saved
    archive_path = f"versions/web_static_{now}.tgz"

    # Create the 'versions' directory if it doesn't exist
    local("mkdir -p versions")

    # Use the 'tar' command to create a compressed archive
    result = local(f"tar -czvf {archive_path} web_static")

    return archive_path if result.succeeded else None


def do_deploy(archive_path):
    """Deploy an archive to the web servers."""

    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = f"/tmp/{archive}"
        folder = archive.split('.')[0]
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

#!/usr/bin/python3
"""Fabric script to deploy web static archives."""

import os
from fabric.api import *
from datetime import datetime

env.hosts = ['3.236.119.223', '54.234.28.162']
env.user = 'ubuntu' 
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
    """Generate a .tgz archive from web_static/."""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        arch_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(arch_name))
        return arch_name
    except:
        return None

def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    if not os.path.exists(archive_path):
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file_n, no_ext))
        run("rm /tmp/{}".format(file_n))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(no_ext))
        print("New version deployed!")
        return True
    except:
        return False

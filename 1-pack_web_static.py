#!/usr/bin/python3
"""
This module provides a function to create a .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # capture the current date and time
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the path where the archive will be stored
    archive_path = f"versions/web_static_{now}.tgz"

    # Create the 'versions' directory if it doesn't exist
    local("mkdir -p versions")

    # Use the 'tar' command to create a compressed archive
    result = local(f"tar -czvf {archive_path} web_static")

    # Return the archive path if the command succeeded, otherwise return None
    return archive_path if result.succeeded else None

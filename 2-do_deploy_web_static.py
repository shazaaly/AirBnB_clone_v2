#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy"""

from fabric.api import put, run, env
import os.path

env.hosts = ["35.168.7.107", "100.25.140.120"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.isfile(archive_path):
        return False

    # Extract the filename and folder name without extension
    file_name = os.path.basename(archive_path)
    folder_name = file_name.split(".")[0]

    # Upload the archive to /tmp/ directory on the web servers
    if put(archive_path, "/tmp/{}".format(file_name)).failed:
        return False

    # Create the target release directory
    if run("mkdir -p /data/web_static/releases/{}".format(folder_name)).failed:
        return False

    # Uncompress the archive into the release directory
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
           .format(file_name, folder_name)).failed:
        return False

    # Delete the archive from /tmp/
    if run("rm /tmp/{}".format(file_name)).failed:
        return False

    # Remove the current symlink if it exists
    if run("rm -f /data/web_static/current").failed:
        return False

    # Create a new symbolic link
    if run("ln -s /data/web_static/releases/{} /data/web_static/current"
           .format(folder_name)).failed:
        return False

    return True

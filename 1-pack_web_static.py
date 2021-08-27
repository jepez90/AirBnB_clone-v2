#!/usr/bin/python3
""".tgz file obtained from web_static dir"""

from datetime import datetime
from fabric.operations import local


def do_pack():
    """ generates a .tgz fiile with the content of the wen_static folder"""
    folder_name = "versions"
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")

    # creates if not exist, the folder verdions
    local("mkdir -p {}".format(folder_name))

    # creates the packed file
    path = "{}/web_static_{}.tgz".format(folder_name, time)
    r = local("tar -czf {} web_static".format(path), capture=True)
    if r.failed:
        return None
    return r

#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """ pack files into .tgz archive """
    # tar -czvf file.tar.gz directory
    time = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    path = "versions/web_static_{}.tgz".format(time)
    cmd = "tar -cvzf {} web_static".format(path)
    local("mkdir -p  versions")
    local(cmd)
    if os.path.exists(path):
        return (path)
    else:
        None

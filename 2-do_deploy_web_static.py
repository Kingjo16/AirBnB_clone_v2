#!/usr/bin/python3
"""A Fabric Ecript that distributes an archive to the web server."""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['100.26.172.250', '35.153.16.242']


def do_deploy(archive_path):
    """Function theta desploye to the web server."""
    if exists(archive_path) is False:
        return False
    try:
        name_f = archive_path.split("/")[-1]
        exits = name_f.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, exits))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name_f, path, exits))
        run('rm /tmp/{}'.format(name_f))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, exits))
        run('rm -rf {}{}/web_static'.format(path, exits))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, exits))
        return True
    except:
        return False

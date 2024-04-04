#!/usr/bin/python3
"""A Fabric Srcipt Class."""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['100.26.172.250', '35.153.16.242']


def do_pack():
    """Get and generate an tgz."""
    try:
        giv_date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        name_fil = "versions/web_static_{}.tgz".format(giv_date)
        local("tar -cvzf {} web_static".format(name_fil))
        return name_fil
    except:
        return None


def do_deploy(archive_path):
    """Web server archiver distributer."""
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


def deploy():
    """Distributes and Creata an archive."""
    arc = do_pack()
    if arc is None:
        return False
    return do_deploy(arc)

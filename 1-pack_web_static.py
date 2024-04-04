#!/usr/bin/python3
"""Fabric Script that will generate an exc fab web_sta."""

from datetime import datetime
from fabric.api import *


def do_pack():
    """Archive on the we_static."""

    gi_time = datetime.now()
    arc = 'web_static_' + gi_time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    maker = local('tar -cvzf versions/{} web_static'.format(arc))
    if maker is not None:
        return arc
    else:
        return None

#!/usr/bin/python3
"""An archive delater."""

import os
from fabric.api import *

env.hosts = ['100.26.172.250', '35.153.16.242']


def do_clean(number=0):
    """Delete an archive which is out of date."""
    number = 1 if int(number) == 0 else int(number)

    arc = sorted(os.listdir("versions"))
    [arc.pop() for m in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in arc]

    with cd("/data/web_static/releases"):
        arc = run("ls -tr").split()
        arc = [a for a in arc if "web_static_" in a]
        [arc.pop() for m in range(number)]
        [run("rm -rf ./{}".format(a)) for a in arc]

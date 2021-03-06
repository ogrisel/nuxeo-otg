#!/usr/bin/env python

import time

import os
import ConfigParser

from notg.storage import Storage
from notg.client import LocalClient, RemoteClient
from notg.synchronizer import Synchronizer


def main():
    home = os.path.join(os.environ['HOME'], ".nuxeo")
    config = ConfigParser.ConfigParser()
    config.read(os.path.join(home, "config.cfg"))

    server = config.get("global", "server")
    username = config.get("global", "username")
    password = config.get("global", "password")
    interval = config.getint("global", "interval")

    local_root = config.get("bindings", "local")
    remote_root = config.get("bindings", "remote")

    storage = Storage(os.path.join(home, "nuxeo.db"))
    local_client = LocalClient(local_root)
    remote_client = RemoteClient(server, username, password, remote_root)

    synchronizer = Synchronizer(storage, local_client, remote_client)

    synchronizer.update_local_info()
    synchronizer.update_remote_info()
    synchronizer.update_local_info()

    while True:
        synchronizer.synchronize_all()
        time.sleep(interval)
        synchronizer.update_remote_info()
        synchronizer.update_local_info()

if __name__ == '__main__':
    main()

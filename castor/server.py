"""
This module defines the Castor server, that consumes the Docker events from
a given host. This module can be run as a command line script or get imported
by another Python script.
"""
from settings import SETTINGS
import docker
import tasks


DOCKER_SETTINGS = SETTINGS.get('docker', {})
DOCKER_CLIENT_KWARGS = {}

for setting in DOCKER_SETTINGS:
    DOCKER_CLIENT_KWARGS[setting] = DOCKER_SETTINGS[setting]

# Customize the Docker client according to settings in `settings.json`
DOCKER_CLIENT = docker.Client(**DOCKER_CLIENT_KWARGS)


def consume():
    """
    Starts consuming Docker events accoding to the already defined settings.
    """
    print 'Start consuming events from %s' % DOCKER_SETTINGS['base_url']
    for event in DOCKER_CLIENT.events():
        tasks.dispatch_event.delay(event)


if __name__ == '__main__':
    try:
        consume()
    except KeyboardInterrupt:
        # Do not display ugly exception if stopped with Ctrl + C
        print '\rBye.'

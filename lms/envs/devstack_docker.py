"""
Left over environment file from before the transition of devstack from
vagrant to docker was complete.

This file should no longer be used, and is only around in case something
still refers to it.
"""

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import


ELASTIC_SEARCH_CONFIG = [
    {
        'use_ssl': False,
        'host': 'elasticsearch7.devstack.edx',
        'port': 9200
    }
]

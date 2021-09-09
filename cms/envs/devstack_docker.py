""" Overrides for Docker-based devstack. """

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import


ELASTIC_SEARCH_CONFIG = [
    {
        'use_ssl': False,
        'host': 'elasticsearch7.devstack.edx',
        'port': 9200
    }
]

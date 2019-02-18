# Copyright 2017 Palantir Technologies, Inc.
""" py.test configuration"""
import logging
from upyls.__main__ import LOG_FORMAT

logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


pytest_plugins = [
    'test.fixtures'
]

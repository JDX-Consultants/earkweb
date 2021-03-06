#!/usr/bin/env python
# coding=UTF-8
import requests

__author__ = "Sven Schlarb"
__copyright__ = "Copyright 2016, The E-ARK Project"
__license__ = "GPL"
__version__ = "0.0.1"

def service_available(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return False
    except Exception:
        return False
    return True

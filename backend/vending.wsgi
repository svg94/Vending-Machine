#! /usr/bin/env python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/bojan/Vending-Machine/backend/')
from vending import app as application
application.secret_key = 'anything you wish'

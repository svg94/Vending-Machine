#! /usr/bin/env python3

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/Vending-Machine')
from vending import app as application
application.secret_key = 'anything you wish'

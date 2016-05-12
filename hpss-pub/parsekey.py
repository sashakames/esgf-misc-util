#!/usr/bin/env python

import sys, json

j = json.loads(sys.stdin.read())

print j['key']

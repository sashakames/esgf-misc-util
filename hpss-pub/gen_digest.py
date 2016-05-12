#!/usr/bin/env python

import hmac, hashlib, sys

f =open("/esg/config/esgf_basejump_publish_key")

key = f.read().strip()


path = sys.argv[1].strip()

digest = hmac.new(key, path, hashlib.sha256).hexdigest()

print digest

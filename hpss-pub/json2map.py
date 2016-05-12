#!/usr/bin/env python

import sys, json

d = json.loads(sys.stdin.read())
# argv1 is the dataset id

print sys.argv[2], '|', sys.argv[1]+ "/" + d["key"], '|', str(d["size"]), '|', "mod_time=" + str(d["modified"]) , '|', "checksum=" + d["hash"], '|', "checksum_type=" + d["hash_function"]


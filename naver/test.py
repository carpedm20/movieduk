import sys
import json

f = open(sys.argv[1], 'r')
r = f.read()
j = json.loads(r)

#!/usr/bin/python

# author: Evangelia Lypiridi
# Data preprocessing for English corpus 

import sys

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	
	if "# ::snt" in line:
		#line = line.replace(".","")
		linesnt = line.split("# ::snt",1)[-1]
		print linesnt


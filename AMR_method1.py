#!/usr/bin/python

# author: Evangelia Lypiridi
# Data preprocessing for AMR corpus. This script linearizes the AMR graph into a string (Method 1)

import sys
import re

initial = True

for line in sys.stdin:
	if not line.startswith("#"):
                if re.match(r'^\s*$', line) and not initial:
                    print ""
                first_time = False
                line = line.lower().strip()
		print line,
            

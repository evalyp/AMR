#!/usr/bin/python

# author: Evangelia Lypiridi
# Data preprocessing for AMR corpus (Method 2)
import sys

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	if line.startswith("# ::id"):
		print ""
	if "(" and "/" in line:
		if "#"  not in line:
			if "multi-sentence" not in line:
				if ":name ("  not in line:
					if ":time" not in line:
						if "-of" not in line:
							if ":quant" not in line:
								if ":polarity" not in line:
									line6 = line.split("(",1)[0]
									line = line.split("/",1)[-1]
									line = line.split("-",1)[0]
									print line6,
									print line.split(")",1)[0],
								else:
									
									line = line.split("/",1)[-1]
									print line.split(")",1)[0],
							else:
								line = line.split("/",1)[-1]
								print line.split(")",1)[0],
						else:
							line1 = line.split("/",1)[-1]
							line2 = line1.split("-",1)[0]
							line3 = line.split("(",1)[0]
							print line3.split(")",1)[0],
							print line2.split(")",1)[0],
					else:
						if "/ date-entity" in line:
							line = line.split("/ date-entity",1)[-1]
							print line.split(")",1)[0],
						else:
							line = line.split("/",1)[-1]
							print line.split(")",1)[0],
				else:
					line4 = line.split("/ name",1)[-1]
					line5 = line.split("(",1)[0]
					print line5,
					print line4.split(")",1)[0],
					

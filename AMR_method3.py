#!/usr/bin/python

# author: Evangelia Lypiridi
# Data preprocessing for AMR corpus. Method 3.
''' 
    This script creates a parallel corpus consisting of English 
    Sentences and AMR strings.
'''

import sys

count_of = 0

for line in sys.stdin:
	line = line.strip()
	line = line.lower()
	
	if line.startswith("# ::id"):
		print ""
	if "(" and "/" in line:
		if not line.startswith(":name ("):
			if "-of (" and "date-entity" not in line:
				if "-quantity" not in line:
					line_new = line.split("/",1)[-1]
					line_n = line_new.split(")",1)[0]
					line_1 = line_n.split('"',1)[-1]
					#line_n1 = line_1.split("-",1)[0]
					line_n2 = line_1.split(":",1)[0]
					line_n3 = line_n2.replace(":op2","")
					line_n4 = line_n3.replace('"',"")
					line_n5 = line_n4.replace("multi","")
					print line_n5.lstrip(),	
					if "date-entity :century" in line:
						line_c = line.split(":century",1)[-1]
						line_c1 = line_c.split(":",1)[0]
						print line_c1.split(")",1)[0],
					if "date-entity :decade" in line:
					 	line_dec = line.split("date-entity :decade",1)[-1]
					 	line_dec1 = line_dec.split(")",1)[0]
					 	print line_dec1,
					if "percentage-entity :value" in line:
						line_per = line.split("percentage-entity :value",1)[-1]
						line_per1 = line_per.split(")",1)[0]
						print line_per1,	
					if line.startswith(":mod"):
						if ":op2" in line:
							line_m = line.split("op2",1)[-1]
							line_m1 = line_m.split('"',1)[-1]
							line_m2 = line_m1.split('"',1)[0]
							print line_m2.split('")',1)[0],
						elif ":op1" and ':op2 "' in line:
							line_el = line.split(':op2 "',1)[-1]
							line_el2 = line_el.split('" :',1)[0]
							print line_el2.split('")',1)[0],
						elif ":op1" and ':op2 "' and ':op3 "' in line:
							line_op = line.split(':op3 "',1)[-1]
							line_op1 = line_op.split('" :',1)[0]
							print line_op1.split('")',1)[0],
						elif ":op1" and ':op2 "' and ":op3" and ':op4 "' in line:
							line_5 = line.split(':op4 "',1)[-1]
							line_6 = line_5.split('" :',1)[0]
							print line_6.split('")',1)[0],
						elif ":op1" and ':op2 "' and ":op3" and ':op4 "' and ':op5 "' in line:
							line_7 = line.split(':op5 "',1)[-1]
							line_8 = line_7.split('" :',1)[0]
							print line_8.split('")',1)[0],
						elif ":op1" and ':op2 "' and ":op3" and ':op4 "' and ':op5 "' and ':op6 "' in line:
							line_9 = line.split(':op6 "',1)[-1]
							line_10 = line_9.split('" :',1)[0]
							print line_10.split('")',1)[0],
						elif ":op1" and ':op2 "' and ":op3" and ':op4 "' and ':op5 "' and ':op6 "' and ':op7 "'in line:
							line_11 = line.split(':op7 "',1)[-1]
							line_12 = line_11.split('")',1)[0]
							print line_12.split('")',1)[0],
					if not line.startswith(':mod'):
						if not line.startswith(':op1'):
							if not line.startswith(':quant'):
								if ":quant" in line:
									if ":name" not in line:
						
										line_q = line.split(":quant",1)[-1]
										#print line_q.split(")",1)[0],
	
	if "temporal-quantity :quant" in line:
		print line.split("temporal-quantity :quant",1)[-1],
	if  "monetary-quantity :quant" in line:	
		print line.split("monetary-quantity :quant",1)[-1],
	if line.startswith("quant"):
		if "approximate :" in line:
			line = line.split("/",1)[-1]
			liner1 = line.split(":",1)[0]
			print liner1,
			liner2 = line.split(":op1",1)[-1]
			print liner2.split(")",1)[0],

	if line.startswith(':op1') and not "("  in line:
		if '"' in line:
			line_o1 = line.split(':op1 "',1)[-1]
			line_o2 = line_o1.split('"',1)[0]
			print line_o2.split('")',1)[0],
	if line.startswith(':op2') and not "(" in line:
		if '"' in line:
			line_o3 = line.split(':op2 "',1)[-1]
			line_o4 = line_o3.split('")',1)[0]
			print line_o4.split('"',1)[0],
	if line.startswith(':op3') and not "("  in line:
		if '"' in line:
			line_o5 = line.split(':op3 "',1)[-1]
			line_o6 = line_o5.split('"',1)[0]
			print line_o6.split('")',1)[0],
	if line.startswith(':op4') and not "(" in line:
		if '"' in line:
			line_o7 = line.split(':op4 "',1)[-1]
			line_o8 = line_o7.split('")',1)[0]
			print line_o8.split('"',1)[0],
	if line.startswith(':op5') and not "("  in line:
		if '"' in line:
			line_o10 = line.split(':op5 "',1)[-1]
			line_o11 = line_o10.split('"',1)[0]
			print line_o11.split('"',1)[0],
	if line.startswith(':op6') and not "(" in line:
		if '"' in line:
			line_o12 = line.split(':op6 "',1)[-1]
			line_o13 = line_o12.split('")',1)[0]
			print line_o13.split('"',1)[0],
	if line.startswith(":quant") and "("  not in line:
		if ")" not in line:
			linequant = line.split(":quant",1)[-1]
			print linequant.split('"',1)[0],
	if line.startswith(":quant") and ")" in line:
		if "/" not in line:
			linequant1 = line.split(":quant",1)[-1]
			print linequant1.split(')',1)[0],
	
	if not line.startswith(":mod"):
		if not line.startswith(":op"):
			if ":name (" in line:
				if ":op1" and "op2" in line:			
					linename = line.split(':op2 "',1)[-1]
					linename1 = linename.split('" :op3',1)[0]			
					print linename1.split('")',1)[0],
					
				if ":op2" and ":op3" in line:
					linename3 = line.split(':op3 "',1)[-1]
					linename4 = linename3.split('" :op4',1)[0]
					print linename4.split('")',1)[0],

				if ":op3" and "op4" in line:
				
					linename5 = line.split(':op4 "',1)[-1]
					linename6 = linename5.split('" :op5',1)[0]
					print linename6.split('")',1)[0],

				if ":op4" and "op5" in line:
					linename7 = line.split(':op5 "',1)[-1]
					linename8 = linename7.split('" :op6',1)[0]
					print linename8.split('")',1)[0],
				if ":op5" and "op6" in line:
					linename20 = line.split(':op6 "',1)[-1]
					linename21 = linename20.split('" :op7',1)[0]
					print linename21.split('")',1)[0],
				
				if ":op6" and "op7" in line:
					linename9 = line.split(':op7 "',1)[-1]
					linename10 = linename9.split('" :op8',1)[0]
					print linename10.split('")',1)[0],
				
				if ":op7" and "op8" in line:
					linename11 = line.split(':op8 "',1)[-1]
					linename12 = linename11.split('" :op9',1)[0]
					print linename12.split('")',1)[0],
				if ":op8" and "op9" in line:
					linename13 = line.split(':op9 "',1)[-1]
					linename14 = linename13.split('" :op10',1)[0]
					print linename14.split('")',1)[0],
				if ":op9" and "op10" in line:
					linename15 = line.split(':op10 "',1)[-1]
					linename16 = linename15.split('" :op11',1)[0]
					print linename16.split('")',1)[0],
					
	if "-of (" in line:
		count_of+=1
		if count_of == 1:
			print "of",

	if ":month 1 " in line:
		print "january",
	if  line.startswith(":month 5"):
		print "may", 
	if line.startswith(":month ") and ")" not in line:
		linemonth = line.split(":month ",1)[-1]
		print linemonth.split('"',1)[0],
	if line.startswith(":year ") and ")" not in line:
		lineyear = line.split(":year ",1)[-1]
		print lineyear.split('"',1)[0],
	if line.startswith(":day "):
		lineday = line.split(":day ",1)[-1]
		print lineday.split(')',1)[0],

	if  "/ date-entity :" in line:
		x = line.split("date-entity",1)[-1]
		x = x.split(")",1)[0]
		y=''
		array = []
		array = x.split()	
		for i in range(1,len(array),2):
			y = y+ " " +array[i]
		print y,		
		
	if line.startswith(":year ") and ")" in line:
		lineyear4 = line.split(":year ",1)[-1]
		print lineyear4.split(")",1)[0],
	
	if ":month 4)" in line:
		print "april",
	elif ":month 11)" in line:
		print "november",
	# Uncomment if you want to create a parallel corpus
	'''
	if "# ::snt" in line:
		line = line.lstrip()	
		line = line.lower()
		line = line.replace(",","")
		line = line.replace(";","")
		line = line.replace("(","")
		line = line.replace(")","")
		line = line.replace("?","")
		line = line.replace('"',"")
		line = line.replace('-'," ")
		#line = line.replace('1.',"")
		#line = line.replace('2.',"")
		#line = line.replace('3.',"")
		linesnt = line.split("# ::snt",1)[-1]
		linesn = linesnt.replace(":","")
		print linesn.lstrip(), 
		print "|||", 
	'''

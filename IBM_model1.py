#!/usr/bin/env python

#author: Evangelia Lypiridi

#Implementation of EM for IBM model 1 - Creates word to word translation probabilities and the alignnments (default:10 iterations)
#Before running, create the folder 'alignmentReverse_consensus' to store the alignments 

import optparse
import sys
import math
import operator
from collections import defaultdict

optparser = optparse.OptionParser()
optparser.add_option("-i", "--iterations", dest="iterations", default=10, help="Number of iterations for EM (default 10)")
optparser.add_option("-b", "--bitext", dest="bitext", default="parallel_consensus.txt", help="Parallel corpus AMR")
optparser.add_option("-n", "--num_sentences", dest="num_sents", default=sys.maxint, type="int", help="Number of sentences to use for training and alignment")
optparser.add_option("-r", "--reverse", dest="reverse", default=True, help="Whether the translation should be done in reverse order")
(opts, _) = optparser.parse_args()

# Probabilities
p = defaultdict( lambda :defaultdict(float)) 

def re_bitext():
	return [[sentence.strip().split() for sentence in pair.split(' ||| ')] for pair in open(opts.bitext)][:opts.num_sents]

def initialize( ):
	sys.stderr.write("Initializing translation probabilities")
	global p
	counta = defaultdict(float)
	counte = defaultdict( lambda :defaultdict(float))
	for (n, (am, e)) in enumerate(bitext):
		for a_am in am:
			for e_j in e:
				counta[a_am,e_j]+=1
				counte[e_j][a_am] = True
	for a_am,e_j in counta:
		p[a_am][e_j] = counta[a_am,e_j] / len(counte[e_j])
		if n % 100 == 0:
			sys.stderr.write(".")

def align(am,e):
    #find optimal alignments
    al =[]
    for i, a_am in enumerate(am):
        best_prob = 0.0
        best_j = 0
        for j, e_j in enumerate(e):
            if p[a_am][e_j] > best_prob:
                best_prob = p[a_am][e_j]
                best_j = j
		al.append((i, best_j))
	return al

def get( it ):
    global bitext
    i = 0
    for am,e in bitext:
        yield align( am,e)
        if i >= it:
            break
        i += 1

	


def get_align():
	global bitext
	for am, e in bitext:
		return align(am, e )

bitext = re_bitext()
# EM
# iterations
k = 0

if opts.reverse:
    for s in bitext:
        s.reverse()

initialize( )
while k < opts.iterations:
	k+= 1
	sys.stderr.write("\nTraining coefficients, iteration %i..." % k)
	apairs = defaultdict( float )
	engCounts = defaultdict( float )
	c = defaultdict( float )
	c2 = defaultdict( float )
	for (n, (am, e)) in enumerate(bitext):
		for a_am in am:
			Z = 0.0
			for e_j in e:
				# word to word translation probabilities
				#print "p("+a_am+"|"+e_j+")=",
				#print p[a_am][e_j]
				Z += p[a_am][e_j]
			for e_j in e:
				c = p[a_am][e_j] / Z
				c2[n, a_am, e_j] = c
				apairs[a_am, e_j] += c
				engCounts[e_j] += c
		if n % 500 == 0:
			sys.stderr.write(".")
	for a_am, e_j in apairs.iterkeys():
		p[a_am][e_j] = apairs[a_am, e_j] / engCounts[e_j]

        likelihood = 0
        for (n, (am, e)) in enumerate(bitext):
        	for a_am in am:
            		for e_j in e:
                		likelihood +=  c2[n, a_am, e_j] * math.log( p[a_am][e_j] )
    	print 'likelihood = ' + str(likelihood)

        if opts.reverse:
		f = open( 'alignmentReverse_consensus/alignments'+str(k), 'w' )
	for n in get( 300 ):
		for i, j in n:
		    f.write("%i-%i " % (i,j))
		f.write("\n")
	f.close()

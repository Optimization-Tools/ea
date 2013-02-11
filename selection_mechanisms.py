from math import sqrt
import random
from operator import itemgetter
from __future__ import division

def roulette(touples, n):
	total = sum((k for i,k in touples))
	touples.sort(reverse=True, key=itemgetter(1))
	
	previous = touples[0]
	previous[1] = previous[1]/sum
	for touple in touples[1:]:
		touple[1] = touple[1]/sum + previous[1]
		previous = touple
		
	cummulative = [k for i,k in touples]
	
	return [touples[bisect_left(cummulative, random.random()][0] for i in range(n)]
	

def fitness_proportionate(parents, n):
	return roulette([(parent, parent.fitness()) for parent in parents], n)
	
def stochastic_uniform(parents, n):
	return roulette([(parent, 1) for parent in parents], n)
	
def sigma_scaling(parents, n):
	parents = [(parent, parent.fitness()) for parent in parents]
	total = sum(k for i,k in parents)
	average = total/len(parents)
	sigma = sqrt(sum((fitness - average)**2 for parent, fitness in parents)/len(parents))
	return roulette([(parent, (value-average)/(2*sigma)) for parent, value in parents])
	
def tournament(parents, n, k, e):
	parents = [(parent, parent.fitness()) for parent in parents]
	out = []
	for i in range(n):
		selection = random.sample(parents, k)
		if random.random() < 0.9:
			out += max(selection, key=itemgetter(1))[0]
		else:
			out += random.sample(selection, 1)[0]
	return out
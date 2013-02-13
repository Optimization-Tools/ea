from __future__ import division
from math import sqrt
import random
from operator import itemgetter
from bisect import bisect_left


def roulette(touples, n):
	total = sum((k for i,k in touples))
	touples.sort(reverse=True, key=itemgetter(1))
	
	previous = touples[0]
	previous[1] = previous[1]/total
	for touple in touples[1:]:
		touple[1] = touple[1]/total + previous[1]
		previous = touple
		
	cummulative = [k for i,k in touples]
	
	return [touples[bisect_left(cummulative[:-1], random.random())][0] for i in range(n)]

class selection_mechanism(object):
	n = None
	def __init__(this, n):
		this.n = n
	
class fitness_proportionate(selection_mechanism):
	def __init__(this, n):
		super(fitness_proportionate, this).__init__(n)
	def select(this, parents):
		return roulette([[parent, parent.fitness] for parent in parents.get_individuals()], this.n)
	
class stochastic_uniform(selection_mechanism):
	def __init__(this, n):
		super(stochastic_uniform, this).__init__(n)
	def select(this, parents):
		return roulette([[parent, 1] for parent in parents.get_individuals()], this.n)
	
class sigma_scaling(selection_mechanism):
	def __init__(this, n):
		super(sigma_scaling, this).__init__(n)
	def select(this, parents):
		parents = [(parent, parent.fitness) for parent in parents.get_individuals()]
		total = sum(k for i,k in parents)
		average = total/len(parents)
		sigma = sqrt(sum((fitness - average)**2 for parent, fitness in parents)/len(parents))
		if sigma:
			return roulette([[parent, 1 + (value-average)/(2*sigma)] for parent, value in parents], this.n)
		else:
			return roulette([[parent, 1] for parent, value in parents], this.n)
	
class tournament(selection_mechanism):
	k = None
	e = None
	def __init__(this, n):
		super(tournament, this).__init__(n)
		this.k = input("Select tournament size: ")
		this.e = input("Select probability of random winner of tournament: ")
	def select(this, parents):
		parents = [(parent, parent.fitness) for parent in parents.get_individuals()]
		out = []
		for i in range(this.n):
			selection = random.sample(parents, this.k)
			if random.random() < this.e:
				out += [max(selection, key=itemgetter(1))[0]]
			else:
				out += [random.sample(selection, 1)[0]]
		return out
		
mechanisms = {"fitness_proportionate":fitness_proportionate, "stochastic_uniform":stochastic_uniform, "sigma_scaling":sigma_scaling, "tournament":tournament}

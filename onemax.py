from __future__ import division
import binary_gtype
import evoalg
from pylab import *

class onemax_ptype(binary_gtype.binary_genotype):
	fitness = None

	def calc_fitness(this, pop_list):
		for pheno in pop_list:
			pheno.fitness = sum([pheno.gene[i] == target[i] for i in xrange(problem_size)])/problem_size

	def __init__(this, gene=None):
		super(onemax_ptype, this).__init__(gene)
		if this.gene == None:
			this.generate_gene(problem_size)
		
problem = raw_input("Input problem to solve (matching/onemax): ")
if problem == "matching":
	target = [int(c) for c in raw_input("Input a bit string: ")]
	problem_size = len(target)
else:
	problem_size = int(input("Input problem size: "))
	target = [1 for i in xrange(problem_size)]

population_list = evoalg.main(onemax_ptype)

best = [pop.max_fitness() for pop in population_list]
average = [pop.average_fitness() for pop in population_list]
std_dev = [pop.fitness_standard_deviation() for pop in population_list]

print "Plotting..."
plot(range(len(best)), best)
plot(range(len(best)), average)
plot(range(len(best)), std_dev)

show()

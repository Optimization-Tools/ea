from __future__ import division
import binary_gtype
import evoalg
from pylab import *

class onemax_ptype(binary_gtype.binary_genotype):
	def fitness(this):
		return sum(this.gene)/len(this.gene)

	def __init__(this, gene=None):
		super(onemax_ptype, this).__init__(gene)
		if this.gene == None:
			this.generate_gene(problem_size)
		

problem_size = int(input("Input problem size: "))
population_list = evoalg.main(onemax_ptype)

best = [pop.max_fitness() for pop in population_list]
average = [pop.average_fitness() for pop in population_list]
std_dev = [pop.fitness_standard_deviation() for pop in population_list]

print "Plotting..."
plot(range(len(best)), best)
plot(range(len(best)), average)
plot(range(len(best)), std_dev)

show()

from __future__ import division
import binary_gtype
import evoalg
from math import log
from pylab import plot, show

class blotto_ptype(binary_gtype.binary_genotype):
	phenotype = None
	fitness = 0
	morale = 1.
	
	def battle(this, that):
		for i in xrange(problem_size):
			diff = this.phenotype[i] - that.phenotype[i]
			if diff > 0:
				this.fitness += 2
				that.morale *= (1-lf)
				if i < problem_size-1:
					distribute = diff*rf/(problem_size-i+1)
					for j in xrange(i+1, problem_size):
						this.phenotype[j] += distribute
			elif diff < 0:
				that.fitness += 2
				this.morale *= (1-lf)
				if i < problem_size-1:
					distribute = -diff*rf/(problem_size-i+1)
					for j in xrange(i+1, problem_size):
						that.phenotype[j] += distribute
			else:
				this.fitness += 1
				that.fitness += 1
	
	def calc_fitness(this, lords):
		for i in range(len(lords)):
			for lord in lords[i+1:]:
				lords[i].battle(lord)
		
	def generate_phenotype(this):
		this.phenotype = this.develop_intlist(4)
		total = sum(this.phenotype)
		this.phenotype = [battle/total for battle in this.phenotype]

	def __init__(this, gene=None):
		super(blotto_ptype, this).__init__(gene)
		if this.gene == None:
			this.generate_gene(problem_size*4)
		
		this.generate_phenotype()
		
def calc_entropy(pop):
	return -sum(strategy.fitness*log(strategy.fitness, 2) for strategy in pop.get_individuals())
		

problem_size = int(input("Input number of battles: "))
rf = float(input("Input reployment fraction: "))
lf = float(input("Input \"morale reduction from loss\"-fraction: "))
population_list = evoalg.main(blotto_ptype)

entropy = [calc_entropy(pop) for pop in population_list]

plot(range(len(entropy)), entropy)
show()
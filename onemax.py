from __future__ import division
import binary_gtype
import evoalg

class onemax_ptype(binary_gtype.binary_genotype):
	def fitness(this):
		return sum(this.gene)/len(this.gene)

	def __init__(this, gene=None):
		super(onemax_ptype, this).__init__(gene)
		if this.gene == None:
			this.generate_gene(problem_size)
		

problem_size = int(input("Input problem size: "))
population_list = evoalg.main(onemax_ptype)

from __future__ import division
import binary_gtype
import evoalg

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
				if i < problem_size-1
					distribute = diff*rf/(problem_size-i+1)
					for battle in this.phenotype[i+1:]:
						battle += distribute
			elif diff < 0:
				that.fitness += 2
				this.morale *= (1-lf)
				if i < problem_size-1:
					distribute = -diff*rf/(problem_size-i+1)
					for battle in that.phenotype[i+1:]:
						battle += distribute
			else:
				this.fitness += 1
				that.fitness += 1
	
	def calc_fitness(this, lords):
		for i in range(len(lords)):
			individuals[i].battle(lord) for lord in lords[i+1:]
		
	def generate_phenotype(this):
		this.phenotype = gene.develop_intlist(4)
		total = sum(this.phenotype)
		phenotype = [battle/total for battle in phenotype]

	def __init__(this, gene=None):
		super(blotto_ptype, this).__init__(gene)
		if this.gene == None:
			this.generate_gene(problem_size*4)
		
		this.generate_phenotype()
		

problem_size = int(input("Input number of battles: "))
rf = float(imput("Input reployment fraction: "))
lf = float(input("Input \"morale reduction from loss\"-fraction: "))
population_list = evoalg.main(blotto_ptype)
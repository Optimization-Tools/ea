from __future__ import division

class population:
	individuals = None
		
	def __init__(this, individuals):
		this.individuals = individuals
		
	def set_individuals(this, individuals):
		this.individuals = individuals
		
	def get_individuals(this):
		return this.individuals
		
	def size(this):
		return len(this.individuals)
		   
	def get_most_fit(this, number):
		this.individuals.sort(key=lambda pheno: (pheno.fitness()), reverse=True) # Sort individuals from most to least fit
		return population(this.individuals[0:min(number, len(this.individuals))])
		
	def combine(this, that):
		return population(this.individuals + that.individuals)
		
	def average_fitness(this):
		return sum([pheno.fitness() for pheno in this.individuals])/this.size()
		
	def max_fitness(this):
		return max([pheno.fitness() for pheno in this.individuals])

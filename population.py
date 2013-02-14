from __future__ import division
from operator import attrgetter

class population:
	individuals = None
		
	def __init__(this, individuals):
		this.individuals = individuals
		this.individuals[0].calc_fitness(individuals)

	def get_individuals(this):
		return this.individuals
		
	def size(this):
		return len(this.individuals)
		   
	def get_most_fit(this, number):
		this.individuals.sort(key=lambda pheno: (pheno.fitness), reverse=True) # Sort individuals from most to least fit
		return population(this.individuals[0:min(number, len(this.individuals))])
		
	def combine(this, that):
		return population(this.individuals + that.individuals)
		
	def average_fitness(this):
		return sum(pheno.fitness for pheno in this.individuals)/this.size()
		
	def max_fitness(this):
		return max(pheno.fitness for pheno in this.individuals)
		
	def min_fitness(this):
		return min(pheno.fitness for pheno in this.individuals)

	def fitness_standard_deviation(this):
		average = this.average_fitness()
		return (sum([(pheno.fitness - average) ** 2 for pheno in this.individuals])/this.size()) ** 0.5
		
	def sort(this):
		this.individuals.sort(reverse=True, key=lambda pheno: pheno.fitness)

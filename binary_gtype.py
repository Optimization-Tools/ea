import random

class binary_genotype():
	gene = None
	mutate = None
	
	def __init__(this, length):
		this.gene = [random.randint(0,1) for i in xrange(length)]
		this.mutate = mutate_bitwise
	
	def generate_gene(this, length):
		this.gene = [random.randint(0,1) for i in xrange(length)]
	
	def set_gene(this, gene):
		this.gene = gene
		
	def set_mutation_strategy(this, function)
		this.mutate = function
		
	def crossover(this, that, num_points):
		points = [random.randint(1, len(this.gene) - 1) for i in xrange(num_points)] + [len(this.gene)]
		points.sort()
		genomes = [this, that]
		start = 0
		result = []
		phase = 0
		for point in points:
			stop = point
			result += genomes[phase].gene[start:stop]
			start = point
			phase = (phase + 1) % 2
		return result
	
	def mutate_bitwise(this, prob):
		for i in xrange(len(this.gene)):
			if random.random() < prob:
				this.gene[i] = 0 if this.gene[i] == 1 else 1
		
	def mutate_genewise(this, prob):
		if random.random() < prob:
			i = random.randint(0, len(this.gene) - 1)
			this.gene[i] = 0 if this.gene[i] == 1 else 1
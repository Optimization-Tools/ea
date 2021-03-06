import random

class binary_genotype(object):
	gene = None
	
	def __init__(this, gene):
		this.gene = gene
		
	def generate_gene(this, length):
		this.set_gene([random.randint(0,1) for i in xrange(length)])
	
	def set_gene(this, gene):
		this.gene = gene
		
	def crossover(this, that, num_points, prob):
		points = random.sample(xrange(1, len(this.gene) - 1), num_points) + [len(this.gene)]
		points.sort()
		genomes = [this, that]
		start = 0
		result1, result2 = [], []
		phase = 0
		for point in points:
			stop = point
			result1 += genomes[phase].gene[start:stop]
			result2 += genomes[(phase+1)%2].gene[start:stop]
			start = point
			if random.random() < prob:
				phase = (phase + 1) % 2
		return [binary_genotype(result1), binary_genotype(result2)]
	
	def mutate_bitwise(this, prob):
		for i in xrange(len(this.gene)):
			if random.random() < prob:
				this.gene[i] = 0 if this.gene[i] == 1 else 1
	
	def mutate_genewise(this, prob):
		if random.random() < prob:
			i = random.randint(0, len(this.gene) - 1)
			this.gene[i] = 0 if this.gene[i] == 1 else 1
		
	def develop_intlist(this, bits):
		result = []
		for i in xrange(0, len(this.gene), bits):
			substr = this.gene[i: i + bits]
			val = 1
			integer = 0
			for bit in substr[::-1]:
				integer += bit * val
				val *= 2
			result += [integer]
		return result

	mutationtypes = {"bitwise":mutate_bitwise, "genewise":mutate_genewise}

import random

class integer_genotype(object):
	gene = None
	max_int = 1
	
	def __init__(this, max_int=1, gene=None):
		this.max_int = max_int
		this.gene = gene

	def generate_random(this, length):
		this.gene = [random.randint(0, this.max_int) for i in xrange(length)]
		
	def generate_distinct(this):
		this.gene = range(this.max_int+1)
		random.shuffle(this.gene)	
			
	def crossover_naive(this, that, num_points, prob):
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
		return [integer_genotype(this.max_int, result1), integer_genotype(this.max_int, result2)]
		
	def crossover_distinct(this, that, num_points, prob):
		#Only supports one crossover (yet)
		if random.random() < prob:
			point = random.randint(1, len(this.gene)-1)
		else:
			point = len(this.gene)
		print point
		result1, result2, rest = [], [], []
		result1 += this.gene[:point]
		rest += this.gene[point:]
		result2 += that.gene
		for k in range(len(result2) - len(rest)):
			while result2[k] in rest:
				result1 += [result2.pop(k)]
		result2 += rest
		return [integer_genotype(this.max_int, result1), integer_genotype(this.max_int, result2)]
			
		
	def mutate_bitwise(this, prob):
		for i in xrange(len(this.gene)):
			if random.random() < prob:
				this.gene[i] = (this.gene[i] + random.randint(1, this.max_int)) % (this.max_int + 1)

	def mutate_genewise(this, prob):
		if random.random() < prob:
			i = random.randint(0, len(this.gene) - 1)
			this.gene[i] = (this.gene[i] + random.randint(1, this.max_int)) % (this.max_int + 1)
			
	def mutate_swap(this, prob):
		if random.random() < prob:
			i, k = random.sample(range(len(this.gene)), 2)
			this.gene[i], this.gene[k] = this.gene[k], this.gene[i]
			
	mutationtypes = {"bitwise":mutate_bitwise, "genewise":mutate_genewise, "swa":mutate_swap}
	crossovertypes = {"naive":crossover_naive, "distinct":crossover_distinct}
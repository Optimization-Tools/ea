import random

class binary_genotype():
	gene = None
	
	def __init__(this, length):
		this.gene = [random.randint(0,1) for i in xrange(length)]
	
	def generate_gene(this, length):
		this.gene = [random.randint(0,1) for i in xrange(length)]
	
	def set_gene(this, gene):
		this.gene = gene
		
class population:
	individuals = None
	
	def __init__(this):
		this.individuals = None
		
	def set_individuals(this, individuals):
		this.individuals = individuals
		
	def get_individuals(this):
		return this.individuals
		
	def size(this):
		return len(this.individuals)
		
	def get_most_fit(this, number):
		individuals.sort(key=lambda genotype: (-genotype.fitness())) # Sort individuals from most to least fit
		return individuals[0:min(number, len(individuals))]
		
	def combine(this, that):
		combined = population()
		combined.set_individuals(this.individuals + that.individuals)
		return combined
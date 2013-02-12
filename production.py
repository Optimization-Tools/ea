import random
import population

class production:
	mutation_type = None
	mutation_rate = None
	crossover_rate = None
	crossover_points = None
	ptype_class = None
	
	def __init__(this, ptype_class):
		this.ptype_class = ptype_class
		this.mutation_type = ptype_class.mutationtypes[raw_input("Select mutation type (" + "/".join(ptype_class.mutationtypes.keys()) + "): ")]
		this.mutation_rate = int(input("Input mutation rate: "))
		this.crossover_points = int(input("Input maximum crossover points: "))
		this.crossover_rate = int(input("Input per-point crossover chance: "))

	def produce(this, parents):
		pairs = [(parents[i], parents[i+1]) for i in xrange(0, len(parents), 2)]
		litter = []
		for mom, dad in pairs:
			child1, child2 = mom.crossover(dad, this.crossover_points, this.crossover_rate)
			this.mutation_type(child1, this.mutation_rate)
			this.mutation_type(child2, this.mutation_rate)
			litter += [this.ptype_class(child1.gene), this.ptype_class(child2.gene)]
		return population.population(litter)

import random
import population

class production:
	mutation_type = None
	mutation_rate = None
	crossover_rate = None
	crossover_points = None
	
	def __init__(this, g_type_class):
		this.mutation_type = g_type_class.mutationtypes[raw_input("Select mutation type (" + "/".join(g_type_class.mutationtypes.keys()) + "): ")]
		this.mutation_rate = int(input("Input mutation rate: "))
		this.crossover_points = int(input("Input maximum crossover points: "))
		this.crossover_rate = int(input("Input per-point crossover chance: "))

	def produce(this, parents):
		pairs = [(parents[i], parents[i+1]) for i in xrange(0, len(parents), 2)]
		litter = []
		for mom, dad in pairs:
			child1, child2 = mom.crossover(dad, this.crossover_points, this.crossover_rate)
			child1.mutation_type(this.mutation_rate)
			child2.mutation_type(this.mutation_rate)
			litter += [child1, child2]
		return population(litter)

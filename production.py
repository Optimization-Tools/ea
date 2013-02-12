import random

class production:
	mutation_type = None
    mutation_rate = None
    crossover_rate = None
    crossover_points = None


	
    def __init__(this, mutation_rate, g_type_class):
		this.mutation_type = g_type_class.mutationtypes[input("Select mutationtype (" + "/".join(g_type_class.mutationtypes.keys()) + ")")]
        this.mutation_rate = mutation_rate
        this.crossover_points = int(input("Input maximum crossover points"))
        this.crossover_rate = int(input("Input per-point crossover chance"))

    def produce(this, parents):
        pairs = [(parents[i], parents[i+1]) for i in xrange(0, len(parents), 2)]
        litter = []
        for pair in pairs:
            child1, child2 = pair[0].crossover(pair[1], this.crossover_points, this.crossover_rate)
            child1.mutation_type(this.mutation_rate)
			child2.mutation_type(this.mutation_rate)
            litter += [child1, child2]
        return litter

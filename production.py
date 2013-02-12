import random

class production:
    mutation_rate = None
    crossover_rate = None
    crossover_points = None


    def __init__(this, mutation_rate):
        this.mutation_rate = mutation_rate
        this.crossover_points = int(input("Input maximum crossover points"))
        this.crossover_rate = int(input("Input per-point crossover chance"))

    def produce(this, parents):
        pairs = [(parents[i], parents[i+1]) for i in xrange(0, len(parents), 2)]
        litter = []
        for pair in pairs:
            child = pair[0].crossover(pair[1], this.crossover_points, this.crossover_rate)
            child.mutate()
            litter += [child]
        return litter

import production
import adult_selection
import selection_mechanisms
import population

def main(phenotype_class):
	popsize = int(input("Input population size: "))
	babymaker = production.production(phenotype_class)
	generations = int(input("Input number of generations: "))
	goal = float(input("Input fitness goal, 0 if not applicable: "))
	protocol = adult_selection.protocols[raw_input("Input the wanted selection protocol (" + "/".join(adult_selection.protocols.keys()) + "): ")](popsize)
	mechanism = selection_mechanisms.mechanisms[raw_input("Input the wanted selection mechanism (" + "/".join(selection_mechanisms.mechanisms.keys()) + "): ")](protocol.litter_size)

	pop = population.population([phenotype_class() for i in range(popsize)])
	
	best = [pop.max_fitness()]
	average = [pop.average_fitness()]
	std_dev = [pop.fitness_standard_deviation()]
	
	generation = 0
	while generation <= generations and goal != 0 and best[-1] < goal:
		parents = mechanism.select(pop)
		litter = babymaker.produce(parents)
		pop = protocol.select(pop, litter)
		best += [pop.max_fitness()]
		average = [pop.average_fitness()]
		std_dev = [pop.fitness_standard_deviation()]
		
		
	print best
	print average
	print std_dev

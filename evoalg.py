import production
import adult_selection
import selection_mechanisms
import population
from sys import stdout

def main(phenotype_class):
	popsize = int(input("Input population size: "))
	babymaker = production.production(phenotype_class)
	generations = int(input("Input number of generations: "))
	goal = float(input("Input fitness goal, 0 if not applicable: "))
	protocol = adult_selection.protocols[raw_input("Input the wanted selection protocol (" + "/".join(adult_selection.protocols.keys()) + "): ")](popsize)
	mechanism = selection_mechanisms.mechanisms[raw_input("Input the wanted selection mechanism (" + "/".join(selection_mechanisms.mechanisms.keys()) + "): ")](protocol.litter_size)

	pop = population.population([phenotype_class() for i in range(popsize)])
	
	population_list = [pop]
	
	stdout.write("Progress: generation \n")
	
	generation = 0
	while generation <= generations and goal != 0 and population_list[-1].max_fitness() < goal:
		parents = mechanism.select(pop)
		litter = babymaker.produce(parents)
		pop = protocol.select(pop, litter)
		
		population_list += [pop]
		generation += 1
		
		
	return population_list

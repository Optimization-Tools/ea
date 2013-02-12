import production
import adult_selection
import selecton_mechanism

def main(phenotype_class):
	popsize = int(input("Input population size: "))
	babymaker = production.production(phenotype_class)
	generations = int(input("Input number of generations: "))
	goal = float(input("Input fitness goal: "))
	protocol = adult_selection.protocols[raw_input("Input the wanted selection protocol (" + "/".join(adult_selection.protocols.keys() + "): ")](popsize)
	mechanism = selection_mechanism.mechanisms[raw_input("Input the wanted selection mechanism (" + "/".join(selection_mechanisms.mechanisms.keys() + "): ")](protocol.litter_size)
	
	best = []
	average = []
	std_dev = []
	
	generation = 0
	while generation < generations and goal != 0 and best[-1] < goal:

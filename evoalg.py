import production
import adult_selection

def main(phenotype_class):
    popsize = int(input("Input population size: "))
    babymaker = production.production(phenotype_class)
    generations = int(input("Input number of generations: "))
    goal = float(input("Input fitness goal: "))
    protocol = adult_selection.protocols[input()](popsize)

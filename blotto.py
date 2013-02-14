from __future__ import division
import binary_gtype
import evoalg
from math import log
from pylab import plot, show, figure, fill_between, xlabel, ylabel, title, legend
from copy import deepcopy

class blotto_ptype(binary_gtype.binary_genotype):
	phenotype = None
	fitness = 0
	morale = 1.
	
	def battle(this, that):
		this_wins = 0
		that_wins = 0
		this.morale = 1.
		that.morale = 1.
		this_ptype = deepcopy(this.phenotype)
		that_ptype = deepcopy(that.phenotype)
		for i in xrange(problem_size):
			diff = this.morale*this_ptype[i] - that.morale*that_ptype[i]
			if diff > 0:
				this_wins += 1
				that.morale *= (1-lf)
				if rf != 0 and i < problem_size-1:
					distribute = diff*rf/(problem_size-i+1)
					for j in xrange(i+1, problem_size):
						this_ptype[j] += distribute
			elif diff < 0:
				that_wins += 1
				this.morale *= (1-lf)
				if rf != 0 and i < problem_size-1:
					distribute = -diff*rf/(problem_size-i+1)
					for j in xrange(i+1, problem_size):
						that_ptype[j] += distribute
		if this_wins > that_wins:
			this.fitness += 2
		elif that_wins > this_wins:
			that.fitness += 2
		else:
			this.fitness += 1
			that.fitness += 1
	
	def calc_fitness(this, lords):
		for i in xrange(len(lords)):
			lords[i].fitness = 0
		for i in xrange(len(lords)):
			for lord in lords[i+1:]:
				lords[i].battle(lord)
		
	def generate_phenotype(this):
		this.phenotype = this.develop_intlist(4)
		total = sum(this.phenotype)
		if total:
			this.phenotype = [battle/total for battle in this.phenotype]
		else:
			this.phenotype = [0 for battle in this.phenotype]

	def __init__(this, gene=None):
		super(blotto_ptype, this).__init__(gene)
		if this.gene == None:
			this.generate_gene(problem_size*4)
		
		this.generate_phenotype()
		
	def calc_entropy(this):
		return -sum((battle*log(battle, 2) if battle != 0 else 0) for battle in this.phenotype)
		

problem_size = int(input("Input number of battles: "))
rf = float(input("Input reployment fraction: "))
lf = float(input("Input \"morale reduction from loss\"-fraction: "))
population_list = evoalg.main(blotto_ptype)

for pop in population_list:
	pop.sort()

average_entropy = [sum(strategy.calc_entropy() for strategy in pop.get_individuals())/problem_size for pop in population_list]
best_entropy = [pop.get_individuals()[0].calc_entropy() for pop in population_list]
best = [pop.max_fitness() for pop in population_list]
average = [pop.average_fitness() for pop in population_list]
std_dev = [pop.fitness_standard_deviation() for pop in population_list]
worst = [pop.min_fitness() for pop in population_list]

topline = [average[i] + std_dev[i] for i in xrange(len(population_list))]
bottomline = [average[i] - std_dev[i] for i in xrange(len(population_list))]

figure(1)
plot(range(len(average_entropy)), average_entropy, color='b', label="Average entropy")
#plot(range(len(best_entropy)), best_entropy, color='r')
title("Average strategy entropy in the population")
xlabel("Generation")
ylabel("Entropy")
legend()

figure(2)
fill_between(range(len(population_list)), topline, bottomline, alpha=0.2, color='b')
plot(range(len(population_list)), best, color='r', label="Best")
plot(range(len(population_list)), worst, color='k', label="Worst")
plot(range(len(population_list)), average, color='b', label="Average with std. dev.")
title("Fitness plot for Blotto strategies")
xlabel("Generation")
ylabel("Fitness")
legend(loc="lower center", ncol=3)


colors = ['b', 'g', 'r', 'c', 'm', 'y', 'w']
def strategy_plot(index):
	bottomlist = [0]*len(population_list)
	toplist = [pop.get_individuals()[index].phenotype[0] for pop in population_list]
	for i in xrange(1, problem_size):
		fill_between(range(len(population_list)), toplist, bottomlist, alpha=1, color=str(i/problem_size))
		for k in range(len(toplist)):
			bottomlist[k] = toplist[k]
			toplist[k] += population_list[k].get_individuals()[index].phenotype[i]
	fill_between(range(len(population_list)), toplist, bottomlist, alpha=1, color=str(i/problem_size))
	#plot(range(len(population_list)), [pop.get_individuals()[index].fitness/(2*len(pop.get_individuals())	) for pop in population_list], color='k')


figure(3)
strategy_plot(0)
#figure(4)
#strategy_plot(-1)
		

show()

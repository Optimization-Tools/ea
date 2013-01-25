import genotypes
import population
import evoalg

class onemax_ptype(genotypes.binary_genotype):
    def fitness(self):
        return sum(self.gene)



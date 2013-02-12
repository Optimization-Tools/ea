import binary_gtype
import evoalg
from __future__ import division

class onemax_ptype(binary_gtype.binary_genotype):
    def fitness(self):
        return sum(self.gene)/len(self.gene)

    def __init__(self, args):
        super(onemax_ptype, self).__init__(problem_size)

problem_size = int(input("Input problem size: "))
evoalg.main(onemax_ptype)

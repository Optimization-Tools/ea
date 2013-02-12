import binary_gtype
import evoalg

class onemax_ptype(binary_gtype.binary_genotype):
    def fitness(self):
        return sum(self.gene)

evoalg.main(onemax_ptype)
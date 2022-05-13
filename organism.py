import random

Genome = list[tuple[str, str]]

class Organism:
    genome: Genome

    def __init__(self, genome):
        self.genome = genome

    def __repr__(self) -> str:
        return ''.join(map(''.join, self.genome))

    def __mul__(self, other):
        possible_offspring = []

        for i in range(2):
            for j in range(2):
                possible_offspring.append([
                    (self.genome[num_genes][i], other.genome[num_genes][j]) for num_genes in range(len(self.genome))
                ])

        return Organism(random.choice(possible_offspring))

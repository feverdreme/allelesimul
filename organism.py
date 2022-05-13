import random

class Organism:
    alleles: tuple[str, str]

    def __init__(self, alleles):
        self.alleles = alleles

    def __repr__(self) -> str:
        return ''.join(self.alleles)

    # crossing over
    def __mul__(self, other):
        possible_offspring = []

        for i in range(2):
            for j in range(2):
                possible_offspring.append((self.alleles[i], other.alleles[j]))

        return Organism(random.choice(possible_offspring))

    def self_is_red(self) -> bool:
        return 'A' in self.alleles

    @staticmethod
    def is_red(org) -> bool:
        return org.self_is_red()

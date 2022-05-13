import random
from organism import Organism, Genome

PARENT_SIZE: int = 4
GENERATIONS: int = 3
KNOWN_GENES: str = "AB"

class Generation:
    population: list[Organism]

    def __init__(self, population = []):
        self.population = population

    def add_organism(self, org):
        self.population.append(org)

    def breed(self):
        next_generation = []

        for o1 in gens[-1].population:
            for o2 in gens[-1].population:
                next_generation.append(o1 * o2)

        return Generation(next_generation)
    
    # def stats(self):
    #     judged = list(map(Organism.is_red, self.population))
    #     return {
    #         "#Red": judged.count(True),
    #         "#Yellow": judged.count(False)
    #     }

P = Generation()
for _ in range(PARENT_SIZE):
    P.add_organism(Organism(['Aa', 'Bb']))

gens: list[Generation] = [P]

for _ in range(GENERATIONS):
    gens.append(gens[-1].breed())

for g in gens:
    print(g.population)

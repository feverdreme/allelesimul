import random
from organism import Organism

PARENT_SIZE: int = 4
GENERATIONS: int = 3

def random_allele(gene: str, times: int = 1):
    possible_genes = (gene, gene.upper())
    
    return [random.choice(possible_genes) for _ in range(times)]

class Generation:
    population: list[Organism]

    def __init__(self, population = []):
        self.population = population

    def add_organism(self, org):
        self.population.append(org)
    
    def stats(self):
        judged = list(map(Organism.is_red, self.population))
        return {
            "#Red": judged.count(True),
            "#Yellow": judged.count(False)
        }

P = Generation()
for _ in range(PARENT_SIZE):
    P.add_organism(Organism(random_allele('a', 2)))

gens: list[Generation] = [P]

for _ in range(GENERATIONS):
    current_generation = []

    for o1 in gens[-1].population:
        for o2 in gens[-1].population:
            current_generation.append(o1 * o2)
    
    gens.append(Generation(current_generation))

for g in gens:
    print(g.stats())
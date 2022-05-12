import random as rand

PARENT_SIZE: int = 4
GENERATIONS: int = 5

class Organism:
    alleles: tuple[str, str]

    def __init__(self, *als):
        self.alleles = als
    
    def __repr__(self) -> str:
        return ''.join(self.alleles)
    
    def __mul__(self, other):
        possible_offspring = []

        for i in range(2):
            for j in range(2):
                possible_offspring.append((self.alleles[i], other.alleles[j]))
        
        return Organism(*rand.choice(possible_offspring))
    
    def self_is_red(self) -> bool:
        return 'A' in self.alleles
    
    @staticmethod
    def is_red(org) -> bool:
        return org.self_is_red()

class Generation:
    population: list[Organism]

    def __init__(self, pop = []):
        self.population = pop

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
    P.add_organism(Organism(
        rand.choice(('A', 'a')),
        rand.choice(('A', 'a'))
    ))

gens: list[Generation] = []
gens.append(P)

for _ in range(GENERATIONS):
    current_generation = []

    for o1 in gens[-1].population:
        for o2 in gens[-1].population:
            current_generation.append(o1 * o2)
    
    gens.append(Generation(current_generation))

for g in gens:
    print(g.stats())
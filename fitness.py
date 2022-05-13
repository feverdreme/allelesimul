def fitness(genome):
    fitarray = []
    for i in range(len(genome)):
        fitness = 0
        genes = list(genome[i])
        for g in range(len(genes)):
            if genes[g] == 'A':
                fitness = 1
        fitarray.append(fitness)
    fitscore = sum(fitarray)/100
    return fitscore
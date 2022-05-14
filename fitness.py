import phenotype

phenotype.setFitness()
phenotype.setDominance()

def fitness(genome):
    
    fitarray = []

    #loop through genome
    for i in range(len(genome)):
        
        fitness = 0

        #searches through phenotype dictionary to find fitness score
        fitness = phenotype.findFitness(genome[i])

        #append result of fitness into array
        fitarray.append(fitness)

    #add together the fitnesses of every allele to get the organisms total fitness
    
    fitscore = sum(fitarray)

    return fitscore



# theoretically the final solution would be a list generated before the simulation where fitness of each phenotype is decided randomly. This function would then just check the phenotype agains the list and retrive its fitness score
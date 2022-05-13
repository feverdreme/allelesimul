def fitness(genome):
    fitarray = []

    #loop through genome
    for i in range(len(genome)):
        fitness = 0

        #get each allele from genome
        allele = list(genome[i])

        #loop through allele
        for g in range(len(allele)):

            #if presence of positive fitness gene is detected, add one to fittnes. 
            #+= wouldnt work because AA would return a fitness of 2 instead of 1. Having two copies of positive fitness train does not actually increase the overall fitness
            if allele[g] == 'A':
                fitness = 1
        #append result of fitness into array
        fitarray.append(fitness)

    #add together the fitnesses of every allele to get the organisms total fitness
    fitscore = sum(fitarray)
    return fitscore


# theoretically the final solution would be a list generated before the simulation where fitness of each phenotype is decided randomly. This function would then just check the phenotype agains the list and retrive its fitness score
import random

#dictionaries
red = {
    "trait": "Red Color",
    "allele": [],
    "dominance": True,
    "fitness": 0
}


yellow = {
    "trait": "Yellow Color",
    "allele": [],
    'dominance': True,
    "fitness": 0
}


#applies a random number 0 to 99 to each phenotype's fitness
def setFitness():

    yellow["fitness"] = random.randint(0,99)

    red["fitness"] = random.randint(0,99)


#randomly chooses either 0 or 1, if one is selected, yellow is set to dominant trait, if 0 is selected red is set to dominant
def setDominance():

    num = random.randint(0,1)
    
    if num == 1:
        
        yellow["allele"] = ["AA", "Aa", "aA"]
        
        red["allele"] = ["aa"]
    
    else:
        
        red["allele"] = ["AA", "Aa", "aA"]
        
        yellow["allele"] = ["aa"]   


#setFitness and setDominance should be run at the begining of every simulation and run only once


#can only currently take in args of AA, Aa, or aA (im not sure if the proccess you are doing would generate a ration of 1 AA : 2 Aa : 1 aa or 1 AA : 1 Aa : 1 aA : 1 aa)
def findFitness(input):

    #loops through the range of yellow's possible alleles and checks if the input allele defines the phenotype
        for i in range(len(yellow["allele"])):

            #if input matches a definition of the phenotype's allele(s), return the fitness score
            if input == yellow["allele"][i]:
                
                return yellow['fitness']
        
        for g in range(len(red["allele"])):
            
            if input == red["allele"][g]:
                
                return red['fitness']






# COMP131 Homework4: Genetic Algorithm
# Kerem San and Xingyi Han
# Purpose: Implementation of a knapsack problem using genetic algorithm

# Reference: https://en.wikipedia.org/wiki/Knapsack_problem

import sys
from random import random

# constants
MAX = 120
BOX_WEIGHT = [20, 30, 60, 90, 50, 70, 30]
IMPORTANCE = [6, 5, 8, 7, 6, 9, 4]
'''
# Return an array of 8 random individual
def initial():
    pop = [None] * 8
    for i in range(8):
        genome = [None] * 7
        for j in range(7):
            num = random()
            if num > 0.5:
                genome[j] = True
            else:
                genome[j] = False
        pop[i] = genome
    return pop
'''

# fake initial function to help us test the code
def initial():
    pop = []

    genome1 = [True,  True,  True,  True,  True,  True,   True]
    pop.append(genome1)
    genome2 = [False, False, False, False, False, False, False]
    pop.append(genome2)
    genome3 = [True,  True,  True,  False, False, False, False]
    pop.append(genome3)
    genome4 = [False, False, False, True,  False, False,  True]
    pop.append(genome4)
    genome5 = [True,  False, False, False, False, False,  True]
    pop.append(genome5)
    genome6 = [False, False, True,  False, False, True,  False]
    pop.append(genome6)
    genome7 = [False, True,  True,  False, False, False,  True]
    pop.append(genome7)
    genome8 = [True,  True, False,  False, True,  False, False]
    pop.append(genome8)

    return pop

# Takes a genome
# Returns the sum of importance, returns 0 if the weight is greater than max weight
def fitness(genome):
    # total weight
    sum_weight = 0
    # total importance
    sum_imp = 0
    for i in range(7):
        if genome[i] == True:
            sum_weight = sum_weight + BOX_WEIGHT[i]
            sum_imp = sum_imp + IMPORTANCE[i]
    if sum_weight > 120:
        sum_imp = 0
    return sum_imp



# Takes a population
# Returns a population with half size of the original population
def random_select(population):
    # record population who survivel from cull
    cull = []

    # an array of survival probability for each genome in population
    survival_rate = []
    # sum importance of all the genomes in population
    sum_val = 0
    for genome in population:
        sum_val = sum_val + fitness(genome)
    # calculate survival rate based on fitness function
    for i in range(8):
        survival_rate.append(round(fitness(population[i])/sum_val, 4)) 

    # choose 4 qualified genome and cull the rest of them
    for times in range(4):
        # print ("the survival probabilities are:")
        # print (survival_rate)
        #calculate cumulative probability, simulate roulette
        cml = 0
        cumul_rate = [None] * 8
        for i in range(8):
            if survival_rate[i] > 0:
                cumul_rate[i] = survival_rate[i] + cml
                cml += survival_rate[i]
            elif survival_rate[i] == 0:
                # Even if the genome's value is 0 its genome still has a small probability to survive
                # This is good for keep the variety of our gene pool 
                cumul_rate[i] = 0.00001
            elif survival_rate[i] == -1:
                # the genome is already chosed
                cumul_rate[i] = 0
        # print ("the cumulative probabilites are:")
        # print (cumul_rate)

        # throw the ball to the roulette and choose the survivor
        choice = random()
        # print ("the lucky numeber is:")
        # print (choice)
        for i in range(8):
            if choice < cumul_rate[i]:
                # print ("the genome we chose is:")
                # print_genome(population[i])
                cull.append(population[i])
                # Once we choose this genome, set genome survival rate to -1, 
                # so it won't take part in further election
                survival_rate[i] = -1 
                break
        #reset survival rate
        sum_val = 0
        for rate in survival_rate:
            if rate != -1:
                sum_val += rate
        for i in range(8):
            if survival_rate[i] != -1:
                survival_rate[i] = round(survival_rate[i]/sum_val, 4)

    # end of half cull

    for genome in cull:
        print_genome(genome)

    return cull



'''
# Takes two genomes
# Returns a cross-over result of parents
# cross-over the genome 
def reproduce(mom, dad):
'''

# Takes a genome
# Returns the mutation of it
def mutate(genome):
    pos = int(ranodm() * 7)
    genome[pos] = not genome[pos]
    return genome

'''
# Returns true if fit enough or enough time has elapsed
def enough()

# Takes a population and return the best one of them
def best(population):
'''
# Takes a genome
# Print out what box we take based on the assignment in genome
def print_genome(genome):
    print ("The boxes we have chosen are:" + "(BoxID: weight(importance))")
    for i in range(7):
        if genome[i] == True :
            print ("No." + str(i+1) + " " + str(BOX_WEIGHT[i]) + "(" + str(IMPORTANCE[i]) + ")", end = ' ')
    print ("\n")

# generates and search the best solution using genetic algorithm
def ga(population):

    while(not enough()):
        new_population = []
        for i in range(8):
            x = random_selection(population)
            y = random_selection(population)
            # result of the cross-over
            child = reproduce(x, y)
            num = random()
            if num <= 0.1:
                child = mutate(child)
                new_population.append(child)
        population = new_population

    return best(population)


#run program
print ("Maximum weight of the Backpack: 120")
print ("Weight(Importance) of Boxes we can choose")
print ("20(6) 30(5) 60(8) 90(7) 50(6) 70(9) 30(4)")
print ("finding the best solution using genetic algorithm...")

# generate initial population
population = initial()

#for genome in population:
#    print_genome (genome)



best_population = ga(population)
#print_genome(best_population)


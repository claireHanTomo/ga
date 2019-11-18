# COMP131 Homework4: Genetic Algorithm
# Kerem San and Xingyi Han
# Purpose: Implementation of a knapsack problem using genetic algorithm

# Reference: https://en.wikipedia.org/wiki/Knapsack_problem

import sys, random

# constants
MAX = 120
BOX_WEIGHT = [20, 30, 60, 90, 50, 70, 30]
IMPORTANCE = [6, 5, 8, 7, 6, 9, 4]

# Return an array of 10 random individual
def initial():

# Takes a genome
# Returns the sum of importance, returns 0 if the weight is greater than max weight
def fitness(population):

# Takes a population
# Returns a population with half size of the original population
def random_select(population)

# Takes two genomes
# Returns a cross-over result of parents
r cross-over the genome 
def reproduce(mom, dad):


# Takes an array of genome
# Returns an array after mutation
def mutate(population):

# Returns true if fit enough or enough time has elapsed
def enough()

# Takes a population and return the best one of them
def best(population):

# Takes a genome
# Print out what box we take based on the assignment in genome
def print_best(genome):


# generates and search the best solution using genetic algorithm
def ga(population, fitness):

    while(!enough()):
        new_population = [None] * 8
        for i in range(8):
            x = random_selection(population)
            y = random_selection(population)
            # result of the cross-over
            child = reproduce(x, y)
            num = random()
            if num < 0.1:
                child = mutate(child)
                new_population.push(child)
        population = new_population

    return best(population)


#run program
print("Maximum weight of the Backpack: 120")
print("Weight(Importance) of Boxes: 20(6) 30(5) 60(8) 90(7) 50(6) 70(9) 30(4)")
print("finding the best solution using genetic algorithm...")

# generate initial population
population = initial()
best_population = ga()
print_best(best_population)


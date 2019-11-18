# COMP131 Homework4: Genetic Algorithm
# Kerem San and Xingyi Han
# Purpose: Implementation of a knapsack problem using genetic algorithm

# Reference: https://en.wikipedia.org/wiki/Knapsack_problem

# constants
MAX = 120
BOX_WEIGHT = [20, 30, 60, 90, 50, 70, 30]
IMPORTANCE = [6, 5, 8, 7, 6, 9, 4]

# Return an array of 10 random individual
def initial():

# Takes a genome
# Returns the sum of importance, returns 0 if the weight is greater than max weight
def fitness(population):

# Takes an array of genome and an array of total importance
# Returns half of the array
def cull(population, importance):

# Takes an array of genome
# Returns an array after cross-over the genome 
def cross(population):


# Takes an array of genome
# Returns an array after mutation
def mutation(population):

# Takes an array of sum of importance
# Returns the index of the largest importance
def best(sum_imp):

# Takes a genome
# Print out what box we take based on the assignment in genome
def print_best(genome):


# generates and search the best solution using genetic algorithm
def ga():
    print("Maximum weight of the Backpack: 120")
    print("Weight(Importance) of Boxes: 20(6) 30(5) 60(8) 90(7) 50(6) 70(9) 30(4)")
    print("finding the best solution using genetic algorithm...")
    # generate initial population
    pop = initial()

    # generate an array to record the sum of importance for each one in population
    sum_value = [None] * 10

    for i in range():
        # use fitness function to calculate the sum of importance for each one in population
        for i in range(10):
            sum_importance[i] = fitness(pop[i])

        #cull half of them
        cull_pop = cull(pop, sum_importance[i])

        #cross-cover
        cross_pop = cross(cull_pop)

        #mutate the genomes
        mutation_pop = mutation(cross_pop)

        pop = mutation_pop

    best_genome = pop[best(sum_importance)]

    print_best(best_genome)



#run program
ga()


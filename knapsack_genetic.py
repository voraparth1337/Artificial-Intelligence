# Written by Parth V
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !!
# www.parthvora.tk

#################################################################################
#                 Knapsack problem using Genetic Algorithm                      #
#                                                                               #
#################################################################################

from itertools import permutations
import random

# Sack weight and total items
max_weight, no_of_items = 10, 4

# no of generations and fitness measure for initial population
generations, fitness = 4, 25

# item weight and profit
items = [(4, 27),
         (3, 25),
         (5, 40),
         (7, 50)
         ]


def get_weight_profit(set_of_numbers):
    '''
    Function returns the weight and profit of a tuple
    :param set_of_numbers:  input tuple
    :return: weight and profit of the tuple
    '''
    global items
    weight = 0
    profit = 0
    for index, item in enumerate(set_of_numbers):
        weight = weight + (items[index][0] * item)
        profit = profit + (items[index][1] * item)
    return (weight, profit)


# produces children
def crossover(parent_1, parent_2):
    '''
    Function produces crossover children of parents provided
    :param parent_1: parent 1 tuple
    :param parent_2: parent 2 tuple
    :return: children tuple
    '''
    global no_of_items
    children_1 = []
    children_2 = []
    division_point = random.randrange(1, no_of_items - 1)
    for i in range(0, division_point + 1):
        children_1.append(parent_1[i])
        children_2.append(parent_2[i])
    for i in range(division_point + 1, no_of_items):
        children_1.append(parent_2[i])
        children_2.append(parent_1[i])
    return tuple(children_1), tuple(children_2)


# to calculate fitness
def get_fitness(object_array):
    '''
    Function returns fitness of input tuple
    if weight exceeds the max weight , return a very bad fitness, else return profit
    :param object_array: input tuple
    :return: fitness 
    '''
    max_weight = 10
    weight, profit = get_weight_profit(object_array)
    if weight > max_weight:
        profit = -1000
    return profit


def print_list():
    # print output
    global population
    print('{:15}{:>10}{:>10}'.format('items', 'weight', 'profit'))
    for item in population:
        a, b = get_weight_profit(item)
        print('{:10}{:>10}{:>10}'.format(str(item), str(a), str(b)))


def get_the_best(*args):
    '''
    given 2 parents and 2 children, this function returns best of 3
    :param args: array of 4 tuples
    :return: return top 2 out of 4 given based on fitness function
    '''
    global max_weight
    temp = sorted(args, key=get_fitness)
    temp1 = list(filter(lambda x: get_weight_profit(x)[0] <= max_weight, temp))
    if len(temp1) < 2:
        return args[0], args[1]
    else:
        return temp1[len(temp1) - 1], temp1[len(temp1) - 2]


def mutation(children):
    '''
    Function mutates a random bit in the tuple
    :param children: input tuple
    :return: mutated children
    '''
    flip_bit = random.randrange(0, no_of_items)
    child = list(children)
    if child[flip_bit] == 1:
        child[flip_bit] = 0
    else:
        child[flip_bit] = 1
    return child


# producting state space tree
all_possible_children = []

# production of all possible children
for p in permutations([0, 0, 0, 0, 1, 1, 1, 1], 4):
    all_possible_children.append(p)

# removing repetitions
all_possible_children = set(all_possible_children)


# generates population of random sets from initial values
def generate_population(all_possible_children, fitness):
    '''
    Function generates initial population using base fitness
    :param all_possible_children: children list
    :param fitness: fitness criteria
    :return: initial population
    '''
    population = set()
    temp_size = len(all_possible_children)
    population_size = len(all_possible_children) // 2
    counter = 0
    while counter != population_size:
        index = random.randrange(0, temp_size)
        temp = tuple(all_possible_children)
        item = temp[index]
        if get_weight_profit(item)[1] >= fitness:
            population.add(item)
            counter = len(population)
    return population


# generating population
population = list(generate_population(all_possible_children, fitness))

# printing population
print("Initial Population")
print_list()

population_size = len(population)

# crossover stage
for i in range(population_size - 1):
    for j in range(i, population_size):
        p1, p2 = population[i], population[j]
        c1, c2 = crossover(p1, p2)
        new1, new2 = get_the_best(p1, p2, c1, c2)
        if new1 not in population:
            r1 = population.pop(i)
            population.insert(i, new1)
        if new2 not in population:
            r2 = population.pop(j)
            population.insert(j, new2)

print("After crossover")
print_list()

# mutation stage
for index, item in enumerate(population):
    new_item = mutation(item)
    population.pop(index)
    population.insert(index, new_item)

print("After Mutation")
print_list()

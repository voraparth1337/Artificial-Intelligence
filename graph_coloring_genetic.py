# Written by Parth V 
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion 
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !! 
# www.parthvora.tk

#################################################################################
#                Graph Coloring using Genetic Algorithm                         #
#                                                                               #
#################################################################################

# code for given graph, however it can be modified for other graph types

#########################
#                       #
#     O-------O         #
#     |       |         #
#     |       |         #
#     O-------O         #
#                       #
#########################

from itertools import permutations
from random import randint

child = []
# initial population - 4 nodes and 3 colors - repeat the number for each node, so
# for 4 nodes, we have each color number (i.e from 1-3 ) , 4 times and since
# each tuple can have only 4 nodes, second argument is 4
for p in permutations([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3], 4):
    child.append(p)
# removing duplicates
child = set(child)


def get_fitness(object_tuple):
    '''
    Function computes the fitness of a tuple, if adjacent nodes have same color
    then a very bad fitness is returned, else
    lesser the colors used higher the fitness is returned
    this is obtained by taking the inverse fraction of number of colors used
    :param object_tuple: input tuple
    :return: fitness
    '''

    # checking if adjacent have same color
    for i in range(len(object_tuple)):
        if object_tuple[i] == object_tuple[(i + 1) % 4]:
            return -999
    object_tuple = set(object_tuple)

    # taking inverse fraction otherwise
    value = 1 / len(set(object_tuple))
    return value * 100


def get_children(parent1, parent2):
    '''
        Function produces crossover children of parents provided
        :param parent1: parent 1 tuple
        :param parent2: parent 2 tuple
        :return: children tuple
        '''
    child1 = [0, 0, 0, 0]
    child2 = [0, 0, 0, 0]
    parent1 = list(parent1)
    parent2 = list(parent2)
    crossover_point = randint(1, 3)
    for i in range(0, crossover_point):
        child1[i] = parent1[i]
        child2[i] = parent2[i]
    for i in range(crossover_point, 4):
        child1[i] = parent2[i]
        child2[i] = parent1[i]
    return child1, child2


def mutate(item):
    '''
        Function mutates a random bit in the tuple
        :param item: input tuple
        :return: mutated children
        '''
    item = list(item)
    position = randint(0, 4)
    value = randint(1, 5)
    item[position] = value
    return tuple(item)


pop_size = 20
population = []
temp = 1
l = []

# initial population for fitness above 30
for item in child:
    if get_fitness(item) > 30:
        l.append(item)

population_size = len(l)

print('Initial')
for item in l:
    print(item)

# performing crossover
for i in range(population_size):
    for j in range(population_size):
        pat1 = l[i]
        pat2 = l[j]
        child1, child2 = get_children(pat1, pat2)
        temp = sorted([pat1, pat2, child1, child2], key=get_fitness)
        new1, new2 = temp[-1], temp[-2]
        if new1 not in l:
            l[i] = new1
        if new2 not in l:
            l[j] = new2
print('crossover')
for item in l:
    print(item)

# performing mutation
for i in range(len(population)):
    new_item = mutate(l[i])
    l[i] = new_item

print('Mutation')
for item in l:
    print(item)

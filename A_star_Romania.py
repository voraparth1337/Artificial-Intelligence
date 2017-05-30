# Written by Parth V 
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion 
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !! 
# www.parthvora.tk

##############################################################
#           A_STAR ALGORITHM FOR THE MAP OF ROMANIA          #
#                FROM RUSSEL NORVIG BOOK                     #                                               
#                                                            #                   
##############################################################

# NOTE : The same function of 'A_STAR()' can be used for GREEDY BEST FIRST SEARCH by removing
# distance metric from node class and having only SLD as the true cost of the node, thus at each step 
# expanding the node with minimum SLD or h(n). Rest everything can be the same

expanded = []
unexpanded = []
cities = []

root = 'Arad'
dest = 'Bucharest'
chosen = None
# dictionary of SLD
sld = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77,
    'Hirsova': 151, 'Lasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100,
    'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Valsui': 199, 'Zerind': 374
}

# map of ROMANIA
map_ = {
    'Arad': ['Timisoara', 'Zerind', 'Sibiu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Rimnicu Vilcea', 'Pitesti', 'Dobreta'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Bucharest': ['Giurgiu', 'Pitesti', 'Fagaras', 'Urziceni'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Valsui'],
    'Eforie': ['Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Valsui': ['Urziceni', 'Lasi'],
    'Lasi': ['Valsui', 'Neamt'],
    'Neamt': ['Lasi']
}

# distance between 2 cities
dist = [('Arad', 'Timisoara', 118), ('Arad', 'Sibiu', 140), ('Arad', 'Zerind', 75), ('Timisoara', 'Lugoj', 111),
        ('Lugoj', 'Mehadia', 70), ('Mehadia', 'Dobreta', 75), ('Dobreta', 'Craiova', 120), ('Zerind', 'Oradea', 71),
        ('Oradea', 'Sibiu', 151), ('Sibiu', 'Fagaras', 99), ('Sibiu', 'Rimnicu Vilcea', 80),
        ('Rimnicu Vilcea', 'Pitesti', 97), ('Rimnicu Vilcea', 'Craiova', 146), ('Pitesti', 'Craiova', 138),
        ('Pitesti', 'Bucharest', 101), ('Bucharest', 'Fagaras', 211), ('Bucharest', 'Giurgiu', 90),
        ('Bucharest', 'Urziceni', 85), ('Urziceni', 'Hirsova', 98), ('Urziceni', 'Valsui', 142),
        ('Hirsova', 'Eforie', 88), ('Valsui', 'Lasi', 92), ('Lasi', 'Neamt', 87)
        ]


# city class
class City:
    def __init__(self, name, sld, n):
        '''
        Function sets nodes name as name, sld and its neighbours as list n
        :param name: name of city
        :param sld:  slf from goal
        :param n: list of neighbours
        '''
        self.name = name
        self.sld = sld
        self.neighbours = list(n)
        self.cost = 0
        self.distance = 0
        self.parent = ''

    def __eq__(self, other):
        # cities are equal if their names are equal
        return self.name == other.name

    def set_parent(self, parent, distance):
        # sets parents as well as distance and cost
        # here distance is g(n) and cost is f(n) and h(n) being heuristic
        if self.parent == '':
            self.parent = parent
        else:
            pass
        
        self.distance = distance
        self.cost = self.sld + self.distance


def get_sld(name):
    ''' Return the sld of that city'''
    return sld[list(filter(lambda x: x == name, sld.keys()))[0]]


def get_smallest():
    '''Get the smallest node for expansion from unexpanded nodes'''
    index, smallest = 0, 99999
    for i, item in enumerate(unexpanded):
        if item.cost < smallest:
            index = i
            smallest = item.cost
    return unexpanded[index]


def get_city(name):
    # get city object given the city name
    return list(filter(lambda x: x.name == name, cities))[0]


def get_distance(city_1, city_2):
    # get distance between two cities
    for item in dist:
        if (item[0] == city_1 and item[1] == city_2) or (item[0] == city_2 and item[1] == city_1):
            return item[2]


for item in map_.keys():
    # create city object for each city
    temp = City(item, get_sld(item), map_[item])
    cities.append(temp)

# start by putting root in unexpanded
unexpanded.append(get_city(root))


def A_STAR():
    '''
    Function performs A star, by expanding the least cost unexpanded node and then adding its childern
    or neighbours in the unexpanded set and itself moving into expanded. This continues till the destination
    node is selected for expansion
    :return: path from root to destination
    '''
    chosen = get_smallest()
    # checking if chosen is destination
    if chosen.name == dest:
        print('Destination ->', chosen.name)
        print('cost ->', chosen.cost)
        return
    else:
        # if not then process its children
        print('chosen --> ', chosen.name)
        expanded.append(chosen)
        unexpanded.remove(chosen)
        for item in chosen.neighbours:
            temp = get_city(item)
            temp.set_parent(chosen.name, get_distance(temp.name, chosen.name) + chosen.distance)
            unexpanded.append(temp)
            print('child nodes -> ', temp.name, 'Cost -> ', temp.cost)
        # calling A star again for its children
        A_STAR()

# first call
A_STAR()

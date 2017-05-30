# Written by Parth V 
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion 
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !! 
# www.parthvora.tk

#################################################################################
#                         8 puzzle solution using GBFS                          #                                     
#                          (GREEDY BEST FIRST SEARCH)                           #
#################################################################################


# 0 represents blank space
import math, copy

# we use dictionary to represent states, with key being the number and value being a tuple of co-ordinates in the matrix
# goal state
goal_state = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 2),
    5: (2, 2),
    6: (2, 1),
    7: (2, 0),
    8: (1, 0),
    0: (1, 1)
}

# initial state
initial_state = {
    1: (0, 1),
    2: (1, 1),
    3: (0, 2),
    4: (1, 2),
    5: (2, 2),
    6: (2, 1),
    7: (2, 0),
    8: (0, 0),
    0: (1, 0)
}

# since I am using Dict for state, we use this method to print it in matrix notation
def get_matrix(state):
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for value, position in state.items():
        row = position[0]
        col = position[1]
        matrix[row][col] = value
    return matrix


def get_manahattan_distance(current, goal):
    '''
    Function computes the manhattan distance for one point on the puzzle board
    We use sum of absolute difference between current and goal points as distance
    
    :param current: (x,y) current position of point (number)
    :param goal: (x,y) goal position of point (number)
    :return: distance from goal for that point
    '''
    cx = current[0]
    cy = current[1]
    gx = goal[0]
    gy = goal[1]
    distance = math.fabs(cx - gx) + math.fabs(cy - gy)
    distance = int(distance)
    return distance


def total_weight(state, goal_state):
    '''
    Function calculates the total manhattan distance for each point (number) on puzzle board
    Compares current and goal state, to return the current weight or total manhattan distance
    
    :param state: current state
    :param goal_state: goal state
    :return: total manhattan distance
    '''
    d = 0
    for number, position in state.items():
        current = position
        goal = goal_state[number]
        d += get_manahattan_distance(current, goal)
    return d


class Node:
    # we use node class to keep track of each state
    def __init__(self, state, parent):
        self.state = state
        self.child = []
        self.visited = False
        self.parent = parent
        self.cost = 0
        self.visited = False

    def add_child(self, node):
        self.child.append(node)

    def generate_children(self):
        # most important method to generate children,
        # since each blank can move in 4 directions we check if its movements exceeds the board
        # boundaries and if it doesnt we add the changed state as one of the children of the current state

        # getting position of blank
        blank = self.state[0]
        blank_x = blank[0]
        blank_y = blank[1]

        if blank_y - 1 >= 0:
            # can it go up ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x, blank_y - 1)
            old_value = list(filter(lambda x: self.state[x] == (blank_x, blank_y - 1), self.state))[0]
            new_state[0] = new
            new_state[old_value] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            new_node.cost = total_weight(new_state, goal_state)
            self.add_child(new_node)

        if blank_x - 1 >= 0:
            # can it go left ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x - 1, blank_y)
            old_value = list(filter(lambda x: self.state[x] == (blank_x - 1, blank_y), self.state))[0]
            new_state[0] = new
            new_state[old_value] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            new_node.cost = total_weight(new_state, goal_state)
            self.add_child(new_node)

        if blank_x + 1 <= 2:
            # can it go right ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x + 1, blank_y)
            old_value = list(filter(lambda x: self.state[x] == (blank_x + 1, blank_y), self.state))[0]
            new_state[0] = new
            new_state[old_value] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            new_node.cost = total_weight(new_state, goal_state)
            self.add_child(new_node)

        if blank_y + 1 <= 2:
            # can it go down ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x, blank_y + 1)
            old_value = list(filter(lambda x: self.state[x] == (blank_x, blank_y + 1), self.state))[0]
            new_state[0] = new
            new_state[old_value] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            new_node.cost = total_weight(new_state, goal_state)
            self.add_child(new_node)

    def __eq__(self, other):
        # function to check if two objects represent the same state
        for item, value in self.state.items():
            if value != other.state[item]:
                return False
        return True

# method to print matrix notation
def print_matrix(state: object):
    matrix = get_matrix(state)
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print('---------')


# GBFS LOGIC STARTS

unexpanded = []
expanded = []


def get_smallest():
    
    #Function returns the smallest node amond unexpaned nodes based on cost
    #h(n) for gbfs and f(n) for A*
    index = -1
    smallest = 9999
    for i, item in enumerate(unexpanded):
        if item.cost < smallest:
            index = i
            smallest = item.cost
    return unexpanded[index]


root = Node(initial_state, None)
root.cost = total_weight(initial_state, goal_state)
unexpanded.append(root)


def GREEDY_BEST_FIRST_SEARCH():
    '''
    this method is same as A_STAR used for map of romania , only here sld is replaced by manhattan distance, rest
    procedure is same, to get a clear picture on how this method works, refer a star romania.py 
    :return: 
    '''
    chosen = get_smallest()
    print('Chosen')
    print_matrix(chosen.state)
    if total_weight(chosen.state, goal_state) == 0:
        return chosen
    else:
        chosen.generate_children()
        expanded.append(chosen)
        unexpanded.remove(chosen)
        for item in chosen.child:
            if not item.visited:
                unexpanded.append(item)
        GREEDY_BEST_FIRST_SEARCH()


ans = GREEDY_BEST_FIRST_SEARCH()

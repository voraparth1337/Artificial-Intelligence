# Written by Parth V 
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion 
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !! 
# www.parthvora.tk

#################################################################################
#                         8 puzzle solution using BFS                           #                                     
#                                                                               #
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
    def __init__(self, state):
        self.state = state
        self.child = []
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
            new_state = copy.deepcopy(self)
            new_state.child = []
            new = (blank_x, blank_y - 1)
            old_value = list(filter(lambda x: self.state[x] == (blank_x, blank_y - 1), self.state))[0]
            # swapping values
            new_state.state[0] = new
            new_state.state[old_value] = (blank_x, blank_y)
            self.add_child(new_state)

        if blank_x - 1 >= 0:
            # can it go left ?
            new_state = copy.deepcopy(self)
            new_state.child = []
            new = (blank_x - 1, blank_y)
            old_value = list(filter(lambda x: self.state[x] == (blank_x - 1, blank_y), self.state))[0]
            new_state.state[0] = new
            new_state.state[old_value] = (blank_x, blank_y)
            self.add_child(new_state)

        if blank_x + 1 <= 2:
            # can it go right ?
            new_state = copy.deepcopy(self)
            new_state.child = []
            new = (blank_x + 1, blank_y)
            old_value = list(filter(lambda x: self.state[x] == (blank_x + 1, blank_y), self.state))[0]
            new_state.state[0] = new
            new_state.state[old_value] = (blank_x, blank_y)
            self.add_child(new_state)

        if blank_y + 1 <= 2:
            # can it go down ?
            new_state = copy.deepcopy(self)
            new_state.child = []
            new = (blank_x, blank_y + 1)
            old_value = list(filter(lambda x: self.state[x] == (blank_x, blank_y + 1), self.state))[0]
            new_state.state[0] = new
            new_state.state[old_value] = (blank_x, blank_y)
            self.add_child(new_state)

    def __eq__(self, other):
        # function to check if two objects represent the same state
        for item, value in self.state.items():
            if value != other.state[item]:
                return False
        return True


# printing matrix representing state
def print_matrix(state: object):
    matrix = get_matrix(state)
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])
    print('---------')


# GENERATING A DYNAMIC TREE
initial_node = Node(initial_state)
already = []
temp_node = initial_node
already.append(temp_node)
level = []
level.append(temp_node)

# TREE UPTO 6 levels
for i in range(6):
    # children of current level will become next level
    next_level = []
    for item in level:
        # for each state at current level, we generate children
        item.generate_children()

        # this array helps us ensure , there are no repeated states in the tree
        new_child = []
        for j in range(len(item.child)):
            # checking for each item, in child list to see if its already present in tree
            if item.child[j] not in already:
                already.append(item.child[j])
                next_level.append(item.child[j])
                new_child.append(item.child[j])

        # we replace it with new child, to ensure that it doesnt have any repeated children
        item.child = new_child

    # setting the next level as current level, after the present current level processing is done
    level = next_level


# implementing the actual BFS - details of it can be found in individual BFS.py file
class Queue:
    def __init__(self):
        self.array = []

    def pop(self):
        return self.array.pop()

    def push(self, value):
        self.array.insert(0, value)

    def top(self):
        return self.array[-1]


q = Queue()

q.push(initial_node)
output = []
goal_node = Node(goal_state)

while q.array:
    temp = q.pop()
    output.append(temp)
    if temp == goal_node:
        break
    for item in temp.child:
        if not item.visited:
            q.push(item)
            item.visited = True
for item in output:
    print_matrix(item.state)

# Written by Parth V 
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion 
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !! 
# www.parthvora.tk

#################################################################################
#                         8 puzzle solution using DFS                           #                                     
#                                                                               #
#################################################################################

# NOTE: ONCE YOU HAVE PREPARED THE STATE SPACE TREE, YOU 
# CAN USE ANY UNINFORMED SEARCH METHOD ON THE STATE SPACE TREE WITH LITTLE MODIFICATIONS
# REFER TO INDIVIDUAL BFS,DFS,DLS AND IDS FILES TO GET AN IDEA.
# THIS IS DFS VERSION, SIMPLE CHANGES CAN BE MADE TO MAKE IT DLS AND IDS

# 0 represents blank space
import copy

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


def print_matrix(state):
    # printing matrix representing state
    matrix = [[0 for y in range(3)] for x in range(3)]
    for key, value in state.items():
        matrix[value[0]][value[1]] = key
    for item in matrix:
        print(item)


class Node:
    # we use node class to keep track of each state
    def __init__(self, state, parent):
        self.state = state
        self.child = []
        self.parent = parent
        self.visited = False
        if parent:
            self.level = self.parent.level + 1
        else:
            self.level = 0

    def __eq__(self, other):
        for key, value in self.state.items():
            if other.state[key] != value:
                return False
        return True

    def get_children(self):
        # most important method to generate children,
        # since each blank can move in 4 directions we check if its movements exceeds the board
        # boundaries and if it doesnt we add the changed state as one of the children of the current state

        # getting position of blank

        blank = self.state[0]
        blank_x, blank_y = blank

        if blank_x + 1 <= 2:
            # can it go right ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x + 1, blank_y)
            old_val = list(filter(lambda x: self.state[x] == (blank_x + 1, blank_y), self.state))[0]
            new_state[0] = new
            new_state[old_val] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            self.child.append(new_node)

        if blank_x - 1 >= 0:
            # can it go left ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x - 1, blank_y)
            old_val = list(filter(lambda x: self.state[x] == (blank_x - 1, blank_y), self.state))[0]
            new_state[0] = new
            new_state[old_val] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            self.child.append(new_node)

        if blank_y + 1 <= 2:
            # can it go down ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x, blank_y + 1)
            old_val = list(filter(lambda x: self.state[x] == (blank_x, blank_y + 1), self.state))[0]
            new_state[0] = new
            new_state[old_val] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            self.child.append(new_node)

        if blank_y - 1 >= 0:
            # can it go up ?
            new_state = copy.deepcopy(self.state)
            new = (blank_x, blank_y - 1)
            old_val = list(filter(lambda x: self.state[x] == (blank_x, blank_y - 1), self.state))[0]
            new_state[0] = new
            new_state[old_val] = (blank_x, blank_y)
            new_node = Node(new_state, self)
            self.child.append(new_node)


# GENERATING A DYNAMIC TREE

level = []
visited = []
initial_node = Node(initial_state, None)
level.append(initial_node)
visited.append(initial_node)

# TREE UPTO 6 levels
for i in range(6):
    # children of current level will become next level
    next_level = []
    for item in level:
        # for each state at current level, we generate children
        item.get_children()

        # this array helps us ensure , there are no repeated states in the tree
        child = []
        for sub_item in item.child:
            # checking for each item, in child list to see if its already present in tree
            if sub_item not in visited:
                next_level.append(sub_item)
                visited.append(sub_item)
                child.append(sub_item)

        # we replace it with new child, to ensure that it doesnt have any repeated children
        item.child = child

    # setting the next level as current level, after the present current level processing is done
    level = next_level


# implementing the actual DFS - details of it can be found in individual DFS.py file
class Stack:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def top(self):
        return self.array[-1]


output = []
s = Stack()
s.push(initial_node)
output.append(initial_node)
initial_node.visited = True

while s.array:
    child_list = s.top().child
    next = None
    for item in child_list:
        if not item.visited:
            next = item
            break
    if next:
        s.push(next)
        output.append(next)
        next.visited = True
    else:
        s.pop()

for item in output:
    node = item.state
    if item == Node(goal_state, None):
        print('goal')
        print_matrix(item.state)
    else:
        print('** ** ** ** ** ** ** ** ** ** ** ** **')
        print_matrix(item.state)

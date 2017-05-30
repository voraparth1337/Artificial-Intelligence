# Written by Parth V
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !!
# www.parthvora.tk

######################################
#      Implementation of IDS         #
#      (Iterative Deepening search)  #
######################################

# NOTE: this same algorithm can be used for any state space tree, with minor modifications
# NOTE: ** SAME AS DLS JUST ADD A LOOP TO CHANGE LEVEL TILL GOAL IS FOUND

class Stack:
    # stack class to implement STACK
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        return self.array.pop()

    def top(self):
        return self.array[-1]

    def __str__(self):
        return str(self.array)


class Node:
    # node class for each item in graph/ tree
    def __init__(self, id, child, visited=False):
        self.id = id
        self.children = child
        self.visited = False
        # level and parent to keep track of which level we are visiting
        self.parent = None
        self.level = 0

    def set_level(self):
        # setting level of the node
        self.level = self.parent.level + 1


def get_node(id):
    # get node object -> given node id
    global nodes
    return_list = list(filter(lambda x: x.id == id, nodes))
    return return_list[0]


# test case 1
graph = {
    'A': ['B', 'D', 'G'],
    'B': ['A', 'E', 'F'],
    'C': ['F', 'H'],
    'D': ['A', 'F'],
    'E': ['B', 'G'],
    'F': ['B', 'C', 'D'],
    'G': ['A', 'E'],
    'H': ['C'],
}

# test case 2
'''graph = {
	1:[2,3],
	2:[4,5],
	3:[1],
	4:[2],
	5:[2],
}'''

# basic logic : push into stack in each iteration and write to output, pop only when a node has no neighbours left
# this can be found out using a variable next, if its none for all children -> it means all its children are visited
# and we must simply pop it off
# Same as DFS, only change is we call off search when the desired level is reached

nodes = []

for node, child in graph.items():
    n = Node(node, child)
    nodes.append(n)

# for each level from i = 0 to 5, we get different graphs
# same as DLS with an extra for loop to change level
for i in range(6):

    # setting values false for each iteration
    for item in nodes:
        item.visited = False

    output = []
    stack = Stack()
    root = get_node('A')
    stack.push(root)
    output.append(root)
    root.visited = True
    root.parent = None
    root.level = 1

    # setting level


    while stack.array:
        parent = stack.top()
        child_list = stack.top().children
        next = None

        # checking for unvisited children
        for item in child_list:
            item = get_node(item)
            if item.visited == False:
                next = item
                break

        # change from DFS , where we set level and parent, to
        # limit our search
        if next:
            next.parent = parent
            next.set_level()

        # before operating we check its level
        if next and next.level <= i:
            stack.push(next)
            output.append(next)
            next.visited = True

        # if all children are visited then POP()
        else:
            stack.pop()

    # printing output
    print('Output for level ' + str(i))
    for item in output:
        print(' NODE: ' + (item.id) + ' level ' + str(item.level), end=' > ')
    print()

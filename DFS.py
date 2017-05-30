# Written by Parth V 
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion 
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !! 
# www.parthvora.tk

######################################
#      Implementation of DFS         #                                                                         
#                                    #                                          
######################################

# NODE: this same algorithm can be used for any state space tree, with minor modifications

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


def get_node(id):
    # get node object -> given node id
    global nodes
    return_list = list(filter(lambda x: x.id == id, nodes))
    return return_list[0]

# test case 1
# graph = {
#	'A': ['B','D','G'],
#	'B': ['A','E','F'],
#	'C': ['F','H'],
#	'D': ['A','F'],
#	'E': ['B','G'],
#	'F': ['B','C','D'],
#	'G': ['A','E'],
#	'H': ['C'],
# }

# test case 2
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [1],
    4: [2],
    5: [2],
}

# STACK IMPLEMENTAION

output = []
nodes = []
stack = Stack()

for node, child in graph.items():
    n = Node(node, child)
    nodes.append(n)

root = get_node(1)
stack.push(root)
output.append(root)
root.visited = True

# basic logic : push into stack in each iteration and write to output, pop only when a node has no neighbours left
# this can be found out using a variable next, if its none for all children -> it means all its children are visited
# and we must simply pop it off

while stack.array:
    child_list = stack.top().children
    next = None
    
    # checking for unvisited children
    for item in child_list:
        item = get_node(item)
        if item.visited == False:
            next = item
            break

    # if unvisited children then add to stack
    if next :
        stack.push(next)
        output.append(next)
        next.visited = True

    # if all children are visited then POP()
    else:
        stack.pop()

# printing output

for item in output:
    print(item.id,end=' > ')
























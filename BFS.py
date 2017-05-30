# Written by Parth V 
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion 
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !! 
# www.parthvora.tk

######################################
#      Implementation of BFS         #                                                                         
#                                    #                                          
######################################

# NOTE: this same algorithm can be used for any state space tree, with minor modifications

class Queue:
    # Queue class to implement queue
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.insert(0, value)

    def pop(self):
        return self.array.pop()

    def top(self):
        return self.array[-1]


class Node:
    # node class for each node in state space tree
    def __init__(self, id, child):
        self.id = id
        self.children = child
        self.inStack = False


def get_node(value):
    # get node object given node value
    global nodes
    for item in nodes:
        if item.id == value:
            return item


# state space tree
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

nodes = []
output = []

for node, child in graph.items():
    n = Node(node, child)
    nodes.append(n)
# main bfs logic
q = Queue()

# push root
root = get_node('A')
q.push(root)
root.inStack = True

# till all nodes are reached
while q.array:
    temp = q.pop()
    output.append(temp)
    for item in temp.children:
        t = get_node(item)
        if not t.inStack:
            q.push(get_node(item))
            t.inStack = True
# output
print('output nodes visited')

for item in output:
    print(item.id,end=' > ')

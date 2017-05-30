# Written by Parth V
# Disclaimer : I am no expert in python but just a learner. In no way is this code perfect or the most 'pythonic' implementaion
# It was written for practice and understanding the concepts. Feel free to extend or make it better. Cheers !!
# www.parthvora.tk

####################################################################
#      Uninformed Search - BFS over map of given as graph          #
#                                                                  #
####################################################################

def bfs(root, graph, dest):
    '''
    Function performs BFS over graph given its root and destination
    :param root: Starting node
    :param graph: Entire graph
    :param dest: Ending node
    :return: Sequence of nodes visited
    '''
    queue, parent = [], []
    parent.append(('X', root))
    queue.insert(0, root)
    while queue:
        item = queue.pop()
        print('popped item----' + str(item))
        for value in graph[item]:
            if value not in [item[1] for item in parent]:
                if value == dest:
                    parent.append((item, value))
                    queue.insert(0, value)
                    print('queue ---' + str(queue))
                    print('Nodes Visited ---' + str([item[1] for item in parent]) + '\n')
                    return parent
                else:
                    parent.append((item, value))
                    queue.insert(0, value)
        print('queue ----' + str(queue))
        print('visited ----' + str([item[1] for item in parent]))


def get_path(parent, child):
    '''
    Function returns a path from parent to child
    :param parent: parent 
    :param child: child
    :return: path
    '''
    dad = list(filter(lambda x: x[1] == child, parent))[0][0];
    if dad == 'X':
        output.append(child)
        return
    else:
        output.append(child)
        get_path(parent, dad)

# initial graph
graph = {
    'A': ['B', 'S'],
    'B': ['A'],
    'S': ['A', 'C', 'G'],
    'G': ['F', 'H', 'S'],
    'F': ['C', 'G'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'H': ['E', 'G']
}

n = 9
root = 'A'
dest = 'H'
result, output = [], []

parent = bfs(root, graph, dest)

get_path(parent, dest)
print('---Path---')
print(' -> '.join(output[::-1]))
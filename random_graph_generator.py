import numpy as np

def random_graph(n):
    """ Creates a random graph of size n, where n is the number of kingdoms """
    adjacency_matrix = []
    for i in range(n):
        node_edges = list(np.random.rand(n))
        for node_index in range(len(node_edges)):
            if np.random.uniform() < 0.1 and node_index != i:
                node_edges[node_index] = "x"
        adjacency_matrix.append(node_edges)

    return adjacency_matrix



def print_matrix(matrix):
    """ Prints matrix to be more user friendly """
    for row in matrix:
        rowString = ""
        for item in row:
            rowString += str(item) + " "
        print(rowString)


print(np.arange(20))
print_matrix(random_graph(20))

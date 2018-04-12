import networkx as nx
from networkx.algorithms import approximation
import random
import numpy as np
import matplotlib.pyplot as plt
import utils
# from input_graph_utils import *

random.seed(3)


def decimal_digits_check(number):
    number = str(number)
    parts = number.split('.')
    if len(parts) == 1:
        return True
    else:
        return len(parts[1]) <= 5


def data_parser(input_data):
    number_of_kingdoms = int(input_data[0][0])
    list_of_kingdom_names = input_data[1]
    starting_kingdom = input_data[2][0]
    adjacency_matrix = [[entry if entry == 'x' else float(entry) for entry in row] for row in input_data[3:]]
    return number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix


def adjacency_matrix_to_graph(adjacency_matrix):
    node_weights = [adjacency_matrix[i][i] for i in range(len(adjacency_matrix))]
    adjacency_matrix_formatted = [[0 if entry == 'x' else entry for entry in row] for row in adjacency_matrix]
    
    for i in range(len(adjacency_matrix_formatted)):
        adjacency_matrix_formatted[i][i] = 0
    
    G = nx.convert_matrix.from_numpy_matrix(np.matrix(adjacency_matrix_formatted))
    
    for node, datadict in G.nodes.items():
        datadict['weight'] = node_weights[node]
    
    return G


def is_metric(G):
    shortest = dict(nx.floyd_warshall(G))
    for u, v, datadict in G.edges(data=True):
        assert shortest[u][v] == datadict['weight'], 'Direct path from {} to {} (weight {}) is not shortest path (weight {})'.format(u, v, datadict['weight'], shortest[u][v])
    return True


def adjacency_matrix_to_edge_list(adjacency_matrix):
    edge_list = []
    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[0])):
            if adjacency_matrix[i][j] != 'x':
                edge_list.append((i, j))
    return edge_list


def adjacency_matrix_to_adjacency_lists(adjacency_matrix):
    adjacency_lists = []
    for i in range(len(adjacency_matrix)):
        adjacency_lists.append([])
        for j in range(len(adjacency_matrix[0])):
            if adjacency_matrix[i][j] != 'x':
                adjacency_lists[i].append(j)
    return adjacency_lists

def tour_to_list_of_edges(tour):
    list_of_edges = []
    for vertex_index in range(len(tour) - 1):
        list_of_edges.append((tour[vertex_index], tour[vertex_index + 1]))
    return list_of_edges

# A* helper function
def kingdoms_state_after_conquer(neighbors_list, original_state):
    """Return kingdoms where all neighbors have surrendered, in binary
    >>> kingdoms_state_after_conquer([0,1], 0b000)
    3
    >>> kingdoms_state_after_conquer([0,1,2], 0b001)
    7
    """
    new = original_state
    for i in neighbors_list:
        new = new | (1 << i)
    return new

# Dijkstra functions
def isSurrendered(G, kingdom_name):
    """ Returns whether a kingdom has surrendered """
    return kingdom_name not in G[kingdom_name]

def checkSurrendered(G):
    """ Returns whether all kingdoms have surrendered """
    for kingdom in G.keys():
        if not isSurrendered(G, kingdom):
            return False
    return True

def conquer(G, kingdom_name, conquered_kingdoms):
    """ Conquers by adding kingdom to conquered_kingdoms list, surrenders kingdoms by removing self edge"""
    return conquered_kingdoms + kingdom_name, surrenderKingdoms(G, kingdom_name)

def surrenderKingdoms(G, kingdom_name):
    """ Neighbors around a kingdom and that kingdom that is conquered surrender """
    for kingdom in G[kingdom_name]:
        if kingdom_name in G[kingdom]:
            G[kingdom].remove(kingdom_name)
    return G

def getKingdomCost(G, kingdom_name):
    """ Returns cost of conquering a kingdom """
    return G[kingdom_name][kingdom_name]["weight"]

def mapKingdomtoCost(G, list_of_kingdom_names):
    """ Creates a dictionary that maps kingdoms to cost to conquer """
    cost_to_conquer_dict = {}
    for kingdom in list_of_kingdom_names:
        cost_to_conquer_dict[kingdom] = getKingdomCost(G, kingdom)
    return cost_to_conquer_dict



if __name__ == '__main__':
    import doctest
    doctest.testmod()

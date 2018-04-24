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
        assert node_weights[node] != 'x', 'The conquering cost of node number {} was specified to be x. Conquering costs cannot be x.'.format(node)
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

# Greedy Algorithm Functions
def isSurrendered(G, kingdom_name):
    """ Returns whether a kingdom has surrendered """
    return kingdom_name not in G

def areAllSurrendered(matrix):
    """ Returns whether all kingdoms have surrendered """
    return all(matrix[i][i] == 'x' for i in range(len(matrix)))

def conquer(matrix, kingdom_name, conquered_kingdoms):
    """ Conquers by adding kingdom to conquered_kingdoms list, surrenders kingdoms by removing self edge"""
    conquered_kingdoms.append(kingdom_name)
    return conquered_kingdoms, surrenderKingdoms(matrix, kingdom_name)

def surrenderKingdoms(matrix, kingdom_index):
    """ Neighbors around a kingdom and that kingdom that is conquered surrender """
    kingdoms_surrendered_indices = []
    for i in range(len(matrix[kingdom_index])):
        if matrix[kingdom_index][i] != 'x':
            kingdoms_surrendered_indices.append(i)
    for i in kingdoms_surrendered_indices:
        matrix[i][i] = 'x'
    matrix[kingdom_index][kingdom_index] = 'x'
    return matrix

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

def is_valid_walk(G, closed_walk):
    return all([(closed_walk[i], closed_walk[i+1]) in G.edges for i in range(len(closed_walk) - 1)])


def get_edges_from_path(path):
    return [(path[i], path[i+1]) for i in range(len(path) - 1)]


def cost_of_solution(G, closed_walk, conquered_set):
    cost = 0
    message = ''
    if not is_valid_walk(G, closed_walk):
        message += 'This is not a valid walk for the given graph\n'
        cost = 'infinite'
    if not closed_walk[0] == closed_walk[-1]:
        message += 'The start and end vertices are not the same\n'
        cost = 'infinite'
    if not nx.is_dominating_set(G, conquered_set):
        message += 'It is not true that every kingdom is either conquered, or adjacent to a conquered kingdom\n'
        cost = 'infinite'
    if cost != 'infinite':
        if len(closed_walk) == 1:
            closed_walk_edges = []
        else:
            closed_walk_edges = get_edges_from_path(closed_walk[:-1]) + [(closed_walk[-2], closed_walk[-1])]
        conquering_cost = sum([G.nodes[v]['weight'] for v in conquered_set])
        travelling_cost = sum([G.edges[e]['weight'] for e in closed_walk_edges])
        cost = conquering_cost + travelling_cost
        message += f'The conquering cost of your solution is {conquering_cost}\n'
        message += f'The travelling cost of your solution is {travelling_cost}\n'
        
    message += f'The total cost of your solution is {cost}'
    return cost, message


def convert_kingdom_names_to_indices(list_to_convert, list_of_kingdom_names):
    return [list_of_kingdom_names.index(name) for name in list_to_convert]


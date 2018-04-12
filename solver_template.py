import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *

"""
======================================================================
  Complete the following function.
======================================================================
"""


def solve(list_of_kingdom_names, starting_kingdom, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_kingdom_names: An list of kingdom names such that node i of the graph corresponds to name index i in the list
        starting_kingdom: The name of the starting kingdom for the walk
        adjacency_matrix: The adjacency matrix from the input file

    Output:
        Return 2 things. The first is a list of kingdoms representing the walk, and the second is the set of kingdoms that are conquered
    """
    N = len(list_of_kingdom_names)
    KINGDOM_POSS = 2 ** N
    G = nx.Graph()

    dict_kingdom_index_to_name = {i: name for i, name in enumerate(list_of_kingdom_names)}
    dict_kingdom_name_to_index = {name: i for i, name in enumerate(list_of_kingdom_names)}
    
    starting_kingdom_index = dict_kingdom_name_to_index[starting_kingdom]

    # print(list_of_kingdom_names)
    # print(starting_kingdom)
    # print(adjacency_matrix)
    adjacency_lists = adjacency_matrix_to_adjacency_lists(adjacency_matrix)
    # print(adjacency_lists)

    # Our graph G has nodes of tuples, form:
    # 0: kingdom_index (0 to n-1)
    # 1: kingdoms_state which describes which kingdoms have surrendered in binary

    # A* Method

    for kingdom_index in range(N):
        for kingdoms_state in range(KINGDOM_POSS):
            G.add_node((kingdom_index, kingdoms_state))

    # adding edges for conquering kingdoms
    for i in range(N):
        adj_list = adjacency_lists[i]
        for k_state in range(KINGDOM_POSS):
            kingdoms_i_conquered = kingdoms_state_after_conquer(adj_list, k_state)
            if kingdoms_i_conquered != k_state:
                G.add_edge((i, k_state), (i, kingdoms_i_conquered), weight=adjacency_matrix[i][i])

    # adding edges for taking roads
    for i in range(N):
        for j in range(i + 1, N):
            if adjacency_matrix[i][j] != 'x':
                for k_state in range(KINGDOM_POSS):
                    G.add_edge((i, k_state), (j, k_state), weight=adjacency_matrix[i][j])

    # import matplotlib.pyplot as plt
    # nx.draw(G)
    # nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')

    # print edges for debugging
    # for u,v,weight in G.edges.data('weight'):
    #     print(u,v,weight)

    # run astar
    path = nx.algorithms.astar_path(G, (starting_kingdom_index, 0), (starting_kingdom_index, KINGDOM_POSS - 1))
    print(path)

    # convert path to walk and kingdoms conquered
    closed_walk = [starting_kingdom]
    conquered_kingdoms = []

    prevKingdom, prevState = path[0]
    for i in range(1, len(path)):
        currKingdom, currState = path[i]
        if currKingdom != prevKingdom:
            closed_walk.append(dict_kingdom_index_to_name[currKingdom])
        elif currState != prevState:
            conquered_kingdoms.append(dict_kingdom_index_to_name[currKingdom])
        else:
            raise Exception('node cycled back to self')
        prevKingdom, prevState = currKingdom, currState
    # raise Exception('"solve" function not defined')

    # Dijkstras
    # Populate nodes in the graph
    # for kingdom_name in list_of_kingdom_names:
    #     G.add_node(kingdom_name)
    #
    # # Populate edges in the graph
    # for i in range(N):
    #     adj_list = adjacency_lists[i]
    #     for j in adj_list:
    #         G.add_edge(dict_kingdom_index_to_name[i], dict_kingdom_index_to_name[j], weight=adjacency_matrix[i][j])
    #
    # # Run dijkstras from the start node
    # paths = nx.algorithms.single_source_dijkstra_path(G, starting_kingdom)
    # print(G["Kanto"]["Kanto"])
    # print(paths)
    #
    # print(G["Kanto"])
    # # for kingdom_name in paths.keys():

    return closed_walk, conquered_kingdoms


"""
======================================================================
   No need to change any code below this line
======================================================================
"""


def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)
    
    input_data = utils.read_file(input_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    closed_walk, conquered_kingdoms = solve(list_of_kingdom_names, starting_kingdom, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    output_filename = utils.input_to_output(filename)
    output_file = f'{output_directory}/{output_filename}'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    utils.write_data_to_file(output_file, closed_walk, ' ')
    utils.write_to_file(output_file, '\n', append=True)
    utils.write_data_to_file(output_file, conquered_kingdoms, ' ', append=True)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)

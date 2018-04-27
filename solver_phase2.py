import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *
# from queue import Queue

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
    # Potentially useful tools
    N = len(list_of_kingdom_names)
    dict_kingdom_index_to_name = {i: name for i, name in enumerate(list_of_kingdom_names)}
    dict_kingdom_name_to_index = {name: i for i, name in enumerate(list_of_kingdom_names)}
    tuples_kingdom_name_to_cost = [(name, cost) for name, cost in zip(list_of_kingdom_names, [adjacency_matrix[i][i] for i in range(len(list_of_kingdom_names))])]
    starting_kingdom_index = dict_kingdom_name_to_index[starting_kingdom]
    dict_kingdom_index_to_cost = {i: adjacency_matrix[i][i] for i in range(N)}

    ################################################################
    ##### STEINER TREE ALGORITHM ###################################
    ################################################################

    ### Greedy solution: sort in some way and add the "optimal" conquering kingdom

    ## Attempt #1: sort using Dijkstra's
    G = nx.Graph()
    adjacency_lists = adjacency_matrix_to_adjacency_lists(adjacency_matrix)
    dict_kingdom_index_to_name = {i: name for i, name in enumerate(list_of_kingdom_names)}
    dict_kingdom_name_to_index = {name: i for i, name in enumerate(list_of_kingdom_names)}

    # Create G
    # Populate nodes in the graph
    for kingdom_name in list_of_kingdom_names:
        G.add_node(kingdom_name)

    # Populate edges in the graph
    for i in range(N):
        for j in adjacency_lists[i]:
            G.add_edge(dict_kingdom_index_to_name[i], dict_kingdom_index_to_name[j], weight=adjacency_matrix[i][j])

    # Run dijkstras from the start node
    shortest_paths_lengths = nx.algorithms.single_source_dijkstra_path_length(G, starting_kingdom)

    tuples_kingdom_name_to_self_cost = [(name, cost) for name, cost in zip(list_of_kingdom_names, [adjacency_matrix[i][i] for i in range(len(list_of_kingdom_names))])]
    tuples_kingdom_name_to_total_cost = [(tup[0], tup[1] + shortest_paths_lengths[tup[0]]) for tup in tuples_kingdom_name_to_self_cost]

    starting_kingdom_index = dict_kingdom_name_to_index[starting_kingdom]
    sorted_kingdom_tuples_by_self_cost = sorted(tuples_kingdom_name_to_self_cost, key=lambda x: x[1]) # for sorting greedily using kingdom cost
    sorted_kingdom_tuples_by_total_cost = sorted(tuples_kingdom_name_to_total_cost, key=lambda x: x[1]) # for sorting greedily using djikstra's cost
    sorted_kingdom_names = [tup[0] for tup in sorted_kingdom_tuples_by_total_cost]
    # sorted_kingdom_names = [tup[0] for tup in sorted_kingdom_tuples_by_self_cost]

    ### Upon some sorted greedy strategy, add kingdoms to conquer in this order

    # Kevin's implementation
    set_surrendered_indices = set()
    conquered_kingdoms_indices = []
    while len(set_surrendered_indices) < N:
        # pop of next
        tentative_conquer_name = sorted_kingdom_names.pop(0)
        tentative_conquer_index = dict_kingdom_name_to_index[tentative_conquer_name]
        # test if conquering actually forces new kingdoms to surrender
        helpful = False
        for kingdom in adjacency_lists[tentative_conquer_index] + [tentative_conquer_index]:
            if kingdom not in set_surrendered_indices:
                helpful = True
                break
        if helpful:
            conquered_kingdoms_indices.append(tentative_conquer_index)
            for kingdom in adjacency_lists[tentative_conquer_index] + [tentative_conquer_index]:
                set_surrendered_indices.add(kingdom)

    ### Remove most expensive kingdoms that lead to over-conquering (i.e. don't need to be conquered)

    # first sort kingdoms by conquer cost
    # check kingdom X:
    # check if at least one neighbor is in set to conquer (so X itself surrenders)
    # for each neighbor, check if it is conquered or has at least neighbor in set to conquer

    # def has_conquered_neighbors(kingdom):
    #     return any(neighbor in set_conquered_kingdoms_indices for neighbor in adjacency_lists[X])
    #
    # set_conquered_kingdoms_indices = set(conquered_kingdoms_indices)
    # for X in reversed(sorted(conquered_kingdoms_indices, key=lambda i: dict_kingdom_index_to_cost[i])):
    #     if has_conquered_neighbors(X)\
    #             and all(has_conquered_neighbors(neighbor) or neighbor in set_conquered_kingdoms_indices for neighbor in adjacency_lists[X] if neighbor != X):
    #         set_conquered_kingdoms_indices.remove(X)
    #
    conquered_kingdoms = [dict_kingdom_index_to_name[i] for i in conquered_kingdoms_indices]

    G = adjacency_matrix_to_graph(adjacency_matrix)
    special_nodes = conquered_kingdoms_indices
    if starting_kingdom_index not in special_nodes:
        special_nodes.append(starting_kingdom_index)
    st = nx.algorithms.approximation.steinertree.steiner_tree(G, special_nodes)

    visited = []
    for _ in range(len(adjacency_lists)):
        visited.append(False)
    count = 0
    visited_order = []

    def dfs(visited_list, curr_kingdom, visited_order_list, counting):
        visited[curr_kingdom] = True
        counting = counting + 1
        visited_order_list.append(curr_kingdom)
        for x in st[curr_kingdom]:
            if visited_list[x] == False:
                dfs(visited_list, x, visited_order, counting)
                if(counting != len(st)):
                        visited_order_list.append(curr_kingdom)

    if len(conquered_kingdoms_indices) == 1:
        visited_order = conquered_kingdoms_indices
    else:
        dfs(visited, starting_kingdom_index, visited_order, count)
        original_graph = adjacency_matrix_to_graph(adjacency_matrix)
        # print(visited_order)
        return_path = nx.algorithms.astar_path(original_graph, visited_order.pop(len(visited_order)-1), starting_kingdom_index)
        visited_order.extend(return_path)
    # for node, datadict in st.nodes.items():
    #     print(node)
    # print(return_path)
    # print(visited_order)

    closed_walk = [dict_kingdom_index_to_name[i] for i in visited_order]

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

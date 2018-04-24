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
    # G = nx.from_numpy_matrix(np.array(adjacency_matrix))
    adjacency_array = np.array(adjacency_matrix)

    dict_kingdom_index_to_name = {i: name for i, name in enumerate(list_of_kingdom_names)}
    dict_kingdom_name_to_index = {name: i for i, name in enumerate(list_of_kingdom_names)}

    tuples_kingdom_name_to_cost = [(name, cost) for name, cost in zip(list_of_kingdom_names, [adjacency_matrix[i][i] for i in range(len(list_of_kingdom_names))])]
    
    starting_kingdom_index = dict_kingdom_name_to_index[starting_kingdom]

    # print(list_of_kingdom_names)
    # print(starting_kingdom)
    # print(adjacency_matrix)
    adjacency_lists = adjacency_matrix_to_adjacency_lists(adjacency_matrix)
    # print(adjacency_lists)

    # Our graph G has nodes of tuples, form:
    # 0: kingdom_index (0 to n-1)
    # 1: kingdoms_state which describes which kingdoms have surrendered in binary

    # Steiner Tree Algorithm
    sorted_kingdom_tuples_by_cost = sorted(tuples_kingdom_name_to_cost, key=lambda x: x[1])
    sorted_kingdom_names = [tup[0] for tup in sorted_kingdom_tuples_by_cost]
    conquered_kingdoms_indices = ["dummy"]
    while not areAllSurrendered(adjacency_array):
        conquered_kingdoms, adjacency_array = conquer(adjacency_array, dict_kingdom_name_to_index[sorted_kingdom_names.pop(0)], conquered_kingdoms_indices)
    conquered_kingdoms_indices.pop(0)

    conquered_kingdoms = [dict_kingdom_index_to_name[i] for i in conquered_kingdoms_indices]


    # This part still doesn't work, need to fix how we are making the graph G
    G = adjacency_matrix_to_graph(adjacency_matrix)
    st = nx.algorithms.approximation.steinertree.steiner_tree(G, conquered_kingdoms_indices)
    # for node, datadict in st.nodes.items():
    #     print(node)
    

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
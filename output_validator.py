# Released to students

import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from utils import *
from student_utils_sp18 import *


def validate_output(input_file, output_file, params=[]):
    print('Processing', input_file)
    
    input_data = utils.read_file(input_file)
    output_data = utils.read_file(output_file)
    return tests(input_data, output_data, params=params)


def validate_all_outputs(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, '.in')
    output_files = utils.get_files_with_extension(output_directory, '.out')

    all_results = []
    for input_file in input_files:
        output_file = utils.input_to_output(input_file)
        print(input_file, output_file)
        if output_file not in output_files:
            print('No corresponding .out file for ', input_file)
            results = None
        else:
            results = validate_output(input_file, output_file, params=params)

        all_results.append((input_file, results))
    return all_results


def tests(input_data, output_data, params=[]):
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    kingdom_tour = output_data[0]
    conquered_kingdoms = output_data[1]

    if not all([kingdom in list_of_kingdom_names for kingdom in kingdom_tour]):
        print('At least one name in your tour is not in the list of kingdom names')

    if not all([kingdom in kingdom_tour for kingdom in conquered_kingdoms]):
        print('At least one name in your conquered set does not belong to the tour')

    if not kingdom_tour[0] == kingdom_tour[-1]:
        print('Your tour does not start and end at the same kingdom')

    list_of_edges_in_tour = tour_to_list_of_edges(kingdom_tour)
    kingdom_name_to_index = lambda name : list_of_kingdom_names.index(name)
    kingdom_index_to_name = lambda index : list_of_kingdom_names[index]
    edges_in_tour_by_index = list(map(lambda edge : (kingdom_name_to_index(edge[0]), kingdom_name_to_index(edge[1])), list_of_edges_in_tour))
    edges_valid = [adjacency_matrix[edge[0]][edge[1]] != 'x' for edge in edges_in_tour_by_index]
    edges_to_self = [edge[0] == edge[1] for edge in edges_in_tour_by_index]
    if not all(edges_valid) or any(edges_to_self):
        print('The kingdoms you listed do not form a valid tour in the graph')
        print('Nonexistent edges by index and name, and edge index in walk:')
        for i in range(len(list_of_edges_in_tour)):
            if not edges_valid[i]:
                print(edges_in_tour_by_index[i],list_of_edges_in_tour[i],i)
        print('Edges of kingdom to self by index and name, and edge index:')
        for i in range(len(list_of_edges_in_tour)):
            if edges_to_self[i]:
                print(edges_in_tour_by_index[i],list_of_edges_in_tour[i],i)

    # Check whether kingdoms are all surrendered

    for name in conquered_kingdoms:
        kingdom_pos = list_of_kingdom_names.index(name)
        for i in range(len(adjacency_matrix)):
            if adjacency_matrix[i][kingdom_pos] != 'x' or adjacency_matrix[kingdom_pos][i] != 'x':
                adjacency_matrix[i][i] = 'x'

    not_surrendered = [adjacency_matrix[i][i] != 'x' for i in range(len(adjacency_matrix))]
    if any(not_surrendered):
        print('You have some kingdoms that have not surrendered!')
        print([i for i in range(len(adjacency_matrix)) if not_surrendered[i]])

    return("Success!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the output validator is run on all files in the output directory. Else, it is run on just the given output file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output', type=str, help='The path to the output file or directory')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    if args.all:
        input_directory, output_directory = args.input, args.output
        validate_all_outputs(input_directory, output_directory, params=args.params)
    else:
        input_file, output_file = args.input, args.output
        validate_output(input_file, output_file, params=args.params)

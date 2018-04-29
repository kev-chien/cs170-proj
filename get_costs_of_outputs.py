import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def analyze_from_file(input_file, output_file, params=[]):
    print('Processing', output_file)
    
    # code from output_validator
    input_data = utils.read_file(input_file)
    output_data = utils.read_file(output_file)

    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    G = adjacency_matrix_to_graph(adjacency_matrix)

    # kingdom_tour = output_data[0]
    # conquered_kingdoms = output_data[1]

    closed_walk = convert_kingdom_names_to_indices(output_data[0], list_of_kingdom_names)
    conquered_set = convert_kingdom_names_to_indices(output_data[1], list_of_kingdom_names)

    # code from cost_of_solution() in student_utils_sp18
    if len(closed_walk) == 1:
        closed_walk_edges = []
    else:
        closed_walk_edges = get_edges_from_path(closed_walk[:-1]) + [(closed_walk[-2], closed_walk[-1])]

    conquering_cost = sum([G.nodes[v]['weight'] for v in conquered_set])
    travelling_cost = sum([G.edges[e]['weight'] for e in closed_walk_edges])
    cost = conquering_cost + travelling_cost

    # print('output_file', cost)
    return travelling_cost, conquering_cost, cost


def analyze_all(output_directory, costs_directory, params=[]):
    input_files = set(utils.get_files_with_extension('inputs', 'in'))
    num_outputs = len(os.listdir(output_directory))

    # writing into csv table
    # data = np.empty((num_outputs + 1, 5))
    header = ['output_dir', 'output_filename', 'travel_cost', 'conquer_cost', 'cost']

    costs_file = f'{costs_directory}/{output_directory}.csv'
    if not os.path.exists(costs_directory):
        os.makedirs(costs_directory)
    utils.write_data_to_file(costs_file, header, ',')

    for name in os.listdir(output_directory):
        if name.endswith("out"):
            if 'inputs/' + name.replace('.out', '.in') not in input_files:
                continue
            num, ext = name.split(".")
            t_cost, c_cost, cost = analyze_from_file(f'inputs/{num}.in', f'{output_directory}/{name}', params=params)
            line_data = [output_directory, name, t_cost, c_cost, cost]
            utils.write_to_file(costs_file, '\n', append=True)
            utils.write_data_to_file(costs_file, line_data, ',', append=True)

    # print(data)
    # np.savetxt('{}/{}.csv'.format(costs_directory, output_directory), data, delimiter=",")


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('output_directory', type=str, nargs='?', help='The path to the outputs directory')
    parser.add_argument('costs_directory', type=str, nargs='?', default='costs', help='The path to the directory to write cost csv to')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    costs_directory = args.costs_directory
    analyze_all(output_directory, costs_directory, params=args.params)

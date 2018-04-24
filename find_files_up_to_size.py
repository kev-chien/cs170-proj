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


def analyze_from_file(input_file, input_filename, output_directory, n, params=[]):
    # print('Processing', input_file)

    basename, filename = os.path.split(input_file)
    
    output_filename = "inputs_for_astar_lim_{}".format(n)
    output_file = f'{output_directory}/{output_filename}'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    input_data = utils.read_file(input_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    if number_of_kingdoms <= n:
        utils.write_to_file(output_file, input_filename + "\n", append=True)


def analyze_all(input_directory, output_directory, n, params=[]):
    # input_files = utils.get_files_with_extension(input_directory, 'in')

    files = []
    filenames = []
    for name in os.listdir(input_directory):
        if name.endswith("in"):
            files.append(f'{input_directory}/{name}')
            filenames.append(name)
    for i in range(len(files)):
      analyze_from_file(files[i], filenames[i], output_directory, n, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('input', type=str, help='The path to the input file directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('n', type=int, default='15', help='The upper bound on the size of graphs allowed')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    input_directory = args.input
    n = args.n
    analyze_all(input_directory, output_directory, n, params=args.params)

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


def analyze_from_file(input_file, input_filename, output_directory, params=[]):
    # print('Processing', input_file)

    basename, filename = os.path.split(input_file)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    input_data = utils.read_file(input_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    lower_bound = 0
    upper_bound = 752
    if len(params) == 1:
        upper_bound = int(float(params[0]))
        if number_of_kingdoms <= n:
            output_filename = "inputs_size_{}".format(upper_bound)
            output_file = f'{output_directory}/{output_filename}'
            utils.write_to_file(output_file, input_filename + "\n", append=True)
    elif len(params) == 2:
        lower_bound = int(float(params[0]))
        upper_bound = int(float(params[1]))
        if number_of_kingdoms <= upper_bound and number_of_kingdoms >= lower_bound:
            output_filename = "inputs_size_{}_to_{}".format(lower_bound, upper_bound)
            output_file = f'{output_directory}/{output_filename}'
            utils.write_to_file(output_file, input_filename + "\n", append=True)
    elif len(params) == 3:
        # python3 find_files_up_to_size.py inputs files_by_id 726 752 count_by_id
        # params[2] signifies to count by filename
        lower_bound = int(float(params[0]))
        upper_bound = int(float(params[1]))
        if int(float(filename[:-3])) <= upper_bound and int(float(filename[:-3])) >= lower_bound:
            output_filename = "inputs_size_{}_to_{}".format(lower_bound, upper_bound)
            output_file = f'{output_directory}/{output_filename}'
            utils.write_to_file(output_file, input_filename + "\n", append=True)


def analyze_all(input_directory, output_directory, params=[]):
    # input_files = utils.get_files_with_extension(input_directory, 'in')

    files = []
    filenames = []
    for name in os.listdir(input_directory):
        if name.endswith("in"):
            files.append(f'{input_directory}/{name}')
            filenames.append(name)
    for i in range(len(files)):
      analyze_from_file(files[i], filenames[i], output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('input', type=str, help='The path to the input file directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    input_directory = args.input
    analyze_all(input_directory, output_directory, params=args.params)

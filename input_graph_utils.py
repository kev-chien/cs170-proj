import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *

class KingdomGraph:
  def __init__(N):
    self.A = []



def matrixToInputFile(input_filename, num, kingdom_names, starting_kingdom, matrix_data, input_directory="in"):
    input_file = f'{input_directory}/{input_filename}'
    if not os.path.exists(input_directory):
        os.makedirs(input_directory)
    utils.write_data_to_file(input_file, [num], '\n')
    utils.write_data_to_file(input_file, kingdom_names, ' ', append=True)
    utils.write_data_to_file(input_file, '\n', '', append=True)
    utils.write_data_to_file(input_file, [starting_kingdom], '\n', append=True)
    for row in matrix_data:
      utils.write_data_to_file(input_file, row, ' ', append=True)
      utils.write_data_to_file(input_file, '\n', '', append=True)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    input_data = utils.read_file("sample_input.in")
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    matrixToInputFile("testprint.in", number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix)

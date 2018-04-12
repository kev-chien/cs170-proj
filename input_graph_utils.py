import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *

class KingdomGraph:
    adj_mat = None
    num = None
    kingdom_names = None
    starting_kingdom = None

    def __init__(self, N, kingdom_names=None, starting_kingdom=None):
        self.num = N
        self.adj_mat = [['x' for _ in range(N)] for _ in range(N)]
        if not kingdom_names:
            self.kingdom_names = ['k{}'.format(i) for i in range(N)]
        else:
            self.kingdom_names = kingdom_names[:]
        if starting_kingdom:
            self.starting_kingdom = starting_kingdom

    def addEdge(self, i, j, cost):
        self.adj_mat[i][j] = cost
        self.adj_mat[j][i] = cost
    
    def addConquerCost(self, i, cost):
        self.adj_mat[i][i] = cost

    def setStartingKindom(self, starting_kingdom):
        self.starting_kingdom = starting_kingdom
    

def kingdomGraphToInputFile(input_filename, kingdom_graph):
    matrixToInputFile(input_filename,
                    kingdom_graph.num,
                    kingdom_graph.kingdom_names,
                    kingdom_graph.starting_kingdom,
                    kingdom_graph.adj_mat)

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

    # input_data = utils.read_file("in/sample_input.in")
    # number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    # matrixToInputFile("testprint.in", number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix)

    kg = KingdomGraph(3, starting_kingdom="k1")
    kg.addEdge(0,1,3)
    kg.addConquerCost(0,5)
    kg.addEdge(1,2,0.5)
    kg.addConquerCost(1,1)
    kg.addConquerCost(2,2)

    kingdomGraphToInputFile("test_kgbuilder_input.in", kg)

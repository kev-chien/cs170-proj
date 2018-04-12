import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *

class KingdomGraph:
    adj_mat = None
    N = None
    kingdom_names = None
    starting_kingdom = None

    def __init__(self, N, kingdom_names=None, starting_kingdom=None, adj_mat=None):
        self.N = N

        if not adj_mat:
            self.adj_mat = [['x' for _ in range(N)] for _ in range(N)]
        else:
            self.adj_mat=adj_mat

        if not kingdom_names:
            self.kingdom_names = ['k{}'.format(i) for i in range(N)]
        else:
            self.kingdom_names = kingdom_names[:]
        
        if starting_kingdom:
            self.starting_kingdom = starting_kingdom
        
        self.i_to_n = {i: name for i, name in enumerate(kingdom_names)}
        self.n_to_i = {name: i for i, name in enumerate(kingdom_names)}
    

    def addEdge(self, i, j, cost):
        if self.N <= i or self.N <= j or i < 0 or j < 0:
            raise Exception('kingdom index out of bounds')
        self.adj_mat[i][j] = cost
        self.adj_mat[j][i] = cost

    def addEdgeByName(self, name_i, name_j, cost):
        i = self.n_to_i[name_i]
        j = self.n_to_i[name_j]
        self.adj_mat[i][j] = cost
        self.adj_mat[j][i] = cost
    
    def addConquerCost(self, i, cost):
        self.adj_mat[i][i] = cost

    def addConquerCostByName(self, name, cost):
        i = self.n_to_i[name]
        self.adj_mat[i][i] = cost

    def setStartingKindom(self, starting_kingdom):
        self.starting_kingdom = starting_kingdom
    

# Writing to input file functions
def kingdomGraphToInputFile(input_filename, kingdom_graph):
    matrixToInputFile(input_filename,
                    kingdom_graph.N,
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

# Drawing functions
def drawFromKingdomGraph(kingdom_graph):
    adj_mat = kingdom_graph.adj_mat
    names = kingdom_graph.kingdom_names
    nxGraph = adjacency_matrix_to_graph(adj_mat)
    node_labels={i: '{}: {}'.format(names[i], adj_mat[i][i]) for i in range(kingdom_graph.N)}
    # print(node_labels)
    drawGraph(nxGraph, node_labels)

def drawGraph(G, node_labels):
    edge_labels=dict([((u,v,),d['weight']) for u,v,d in G.edges(data=True)])

    pos=nx.spring_layout(G)
    nx.draw_networkx(G,pos,with_labels=False)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    nx.draw_networkx_labels(G,pos,labels=node_labels)
    plt.show()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # input_data = utils.read_file("in/sample_input.in")
    # number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    # matrixToInputFile("testprint.in", number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix)


    # test creating kingdomGraph
    kg = KingdomGraph(3, starting_kingdom="k1")
    kg.addEdge(0,1,3)
    kg.addConquerCost(0,5)
    kg.addEdge(1,2,0.5)
    kg.addConquerCost(1,1)
    kg.addConquerCost(2,2)

    kingdomGraphToInputFile("test_kgbuilder_input.in", kg)

    # test drawing graph
    input_file = "in/sample_input.in"
    input_data = utils.read_file(input_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    kg = KingdomGraph(number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix)
    drawFromKingdomGraph(kg)


from input_graph_utils import *

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # input_data = utils.read_file("in/sample_input.in")
    # number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    # matrixToInputFile("testprint.in", number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix)


    # test creating kingdomGraph
    # Kevin's 50 kingdoms
    kg = KingdomGraph(50, starting_kingdom="k1", kingdom_names=['k{}'.format(i+1) for i in range(50)])
    kg.addEdgeByName('k1','k2',3)
    kg.addConquerCostByName('k1',35)

    kingdomGraphToInputFile("test_kgbuilder_input.in", kg)

    # test drawing graph
    drawFromKingdomGraph(kg)
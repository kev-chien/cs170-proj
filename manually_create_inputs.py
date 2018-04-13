from input_graph_utils import *

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # input_data = utils.read_file("in/sample_input.in")
    # number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)

    # matrixToInputFile("testprint.in", number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix)


    # test creating kingdomGraph
    # Kevin's 50 kingdoms
    # kg = KingdomGraph(50, starting_kingdom="k1", kingdom_names=['k{}'.format(i+1) for i in range(50)])
    # kg.addEdgeByNameByName('k1','k2',3)
    # kg.addConquerCostByName('k1',35)
    #
    #

    # Lawrence's 50 kingdoms
    kg = KingdomGraph(100, starting_kingdom="l1", kingdom_names=['l{}'.format(i+1) for i in range(50)]+['k{}'.format(i+1) for i in range(50)])
    kg.addConquerCostByName('l1', 10000)
    kg.addConquerCostByName('l2', 9)
    kg.addConquerCostByName('l3', 5)
    kg.addConquerCostByName('l4', 1)
    kg.addConquerCostByName('l5', 8)
    kg.addConquerCostByName('l6', 5)
    kg.addConquerCostByName('l7', 20)
    kg.addConquerCostByName('l8', 2)
    kg.addConquerCostByName('l9', 8)
    kg.addConquerCostByName('l10', 10)
    kg.addConquerCostByName('l11', 7)
    kg.addConquerCostByName('l12', 11)
    kg.addConquerCostByName('l13', 1)
    kg.addConquerCostByName('l14', 7)
    kg.addConquerCostByName('l15', 3)
    kg.addConquerCostByName('l16', 7)
    kg.addConquerCostByName('l17', 8)
    kg.addConquerCostByName('l18', 20)
    kg.addConquerCostByName('l19', 1)
    kg.addConquerCostByName('l20', 3)
    kg.addConquerCostByName('l21', 24)
    kg.addConquerCostByName('l22', 3)
    kg.addConquerCostByName('l23', 8)
    kg.addConquerCostByName('l24', 15)
    kg.addConquerCostByName('l25', 4)
    kg.addConquerCostByName('l26', 5)
    kg.addConquerCostByName('l27', 2)
    kg.addConquerCostByName('l28', 7)
    kg.addConquerCostByName('l29', 3)
    kg.addConquerCostByName('l30', 10)
    kg.addConquerCostByName('l31', 5)
    kg.addConquerCostByName('l32', 30)
    kg.addConquerCostByName('l33', 1)
    kg.addConquerCostByName('l34', 66)
    kg.addConquerCostByName('l35', 7)
    kg.addConquerCostByName('l36', 3)
    kg.addConquerCostByName('l37', 7)
    kg.addConquerCostByName('l38', 5)
    kg.addConquerCostByName('l39', 2)
    kg.addConquerCostByName('l40', 15)
    kg.addConquerCostByName('l41', 7)
    kg.addConquerCostByName('l42', 2)
    kg.addConquerCostByName('l43', 9)
    kg.addConquerCostByName('l44', 10)
    kg.addConquerCostByName('l45', 9)
    kg.addConquerCostByName('l46', 100)
    kg.addConquerCostByName('l47', 7)
    kg.addConquerCostByName('l48', 8)
    kg.addConquerCostByName('l49', 50)
    kg.addConquerCostByName('l50', 3)

    # 7 clusters of 7

    # 1
    kg.addEdgeByName('l1', 'l2', 2)
    kg.addEdgeByName('l2', 'l3', 10)
    kg.addEdgeByName('l3', 'l4', 1)
    kg.addEdgeByName('l2', 'l5', 5)
    kg.addEdgeByName('l2', 'l7', 7)
    kg.addEdgeByName('l5', 'l6', 1)
    kg.addEdgeByName('l6', 'l7', 5)
    kg.addEdgeByName('l7', 'l8', 40)

    # 2
    kg.addEdgeByName('l1', 'l9', 2)
    kg.addEdgeByName('l9', 'l10', 20)
    kg.addEdgeByName('l10', 'l11', 1)
    kg.addEdgeByName('l10', 'l12', 2)
    kg.addEdgeByName('l11', 'l13', 8)
    kg.addEdgeByName('l12', 'l14', 10)
    kg.addEdgeByName('l14', 'l15', 1)

    # 3
    kg.addEdgeByName('l1', 'l16', 100)
    kg.addEdgeByName('l16', 'l17', 1)
    kg.addEdgeByName('l16', 'l19', 3)
    kg.addEdgeByName('l17', 'l18', 7)
    kg.addEdgeByName('l19', 'l20', 2)
    kg.addEdgeByName('l20', 'l21', 9)
    kg.addEdgeByName('l18', 'l21', 1)
    kg.addEdgeByName('l21', 'l22', 1)

    # 4
    kg.addEdgeByName('l1', 'l23', 75)
    kg.addEdgeByName('l23', 'l24', 5)
    kg.addEdgeByName('l24', 'l25', 3)
    kg.addEdgeByName('l24', 'l26', 2)
    kg.addEdgeByName('l23', 'l27', 2)
    kg.addEdgeByName('l24', 'l27', 4)
    kg.addEdgeByName('l27', 'l28', 7)
    kg.addEdgeByName('l28', 'l29', 5)

    # 5
    kg.addEdgeByName('l1', 'l30', 50)
    kg.addEdgeByName('l30', 'l31', 2)
    kg.addEdgeByName('l30', 'l32', 3)
    kg.addEdgeByName('l31', 'l32', 4)
    kg.addEdgeByName('l32', 'l33', 12)
    kg.addEdgeByName('l33', 'l34', 13)
    kg.addEdgeByName('l32', 'l34', 2)
    kg.addEdgeByName('l34', 'l35', 2)
    kg.addEdgeByName('l35', 'l36', 7)
    kg.addEdgeByName('l34', 'l36', 8)

    # 6
    kg.addEdgeByName('l1', 'l37', 1000)
    kg.addEdgeByName('l37', 'l38', 1)
    kg.addEdgeByName('l38', 'l39', 2)
    kg.addEdgeByName('l37', 'l40', 2)
    kg.addEdgeByName('l40', 'l41', 1)
    kg.addEdgeByName('l41', 'l42', 8)
    kg.addEdgeByName('l40', 'l43', 9)

    # 7
    kg.addEdgeByName('l1', 'l44', 25)
    kg.addEdgeByName('l44', 'l45', 2)
    kg.addEdgeByName('l44', 'l46', 1)
    kg.addEdgeByName('l45', 'l46', 2)
    kg.addEdgeByName('l46', 'l47', 20)
    kg.addEdgeByName('l46', 'l48', 2)
    kg.addEdgeByName('l46', 'l49', 10)
    kg.addEdgeByName('l49', 'l50', 21)

    # kingdomGraphToInputFile("50_lawrence.in", kg)

    # kg = KingdomGraph(50, starting_kingdom="k1", kingdom_names=['k{}'.format(i+1) for i in range(50)])
    
    # kingdom conquer costs
    kg.addConquerCostByName('k1',1000)
    kg.addConquerCostByName('k2',3)
    kg.addConquerCostByName('k3',5)
    kg.addConquerCostByName('k4',10)
    kg.addConquerCostByName('k5',60)
    kg.addConquerCostByName('k6',100)
    kg.addConquerCostByName('k7',1)
    kg.addConquerCostByName('k8',10)
    kg.addConquerCostByName('k9',60)
    kg.addConquerCostByName('k10',30)
    kg.addConquerCostByName('k11',30)
    kg.addConquerCostByName('k12',100)
    kg.addConquerCostByName('k13',5)
    kg.addConquerCostByName('k14',20)
    kg.addConquerCostByName('k15',100)
    kg.addConquerCostByName('k16',10)
    kg.addConquerCostByName('k17',60)
    kg.addConquerCostByName('k18',10)
    kg.addConquerCostByName('k19',5)
    kg.addConquerCostByName('k20',90)
    kg.addConquerCostByName('k21',20)
    kg.addConquerCostByName('k22',50)
    kg.addConquerCostByName('k23',50)
    kg.addConquerCostByName('k24',1)
    kg.addConquerCostByName('k25',10)
    kg.addConquerCostByName('k26',100)
    kg.addConquerCostByName('k27',10)
    kg.addConquerCostByName('k28',70)
    kg.addConquerCostByName('k29',80)
    kg.addConquerCostByName('k30',10)
    kg.addConquerCostByName('k31',90)
    kg.addConquerCostByName('k32',20)
    kg.addConquerCostByName('k33',100)
    kg.addConquerCostByName('k34',15)
    kg.addConquerCostByName('k35',10)
    kg.addConquerCostByName('k36',5)
    kg.addConquerCostByName('k37',20)
    kg.addConquerCostByName('k38',10)
    kg.addConquerCostByName('k39',20)
    kg.addConquerCostByName('k40',20)
    kg.addConquerCostByName('k41',30)
    kg.addConquerCostByName('k42',4)
    kg.addConquerCostByName('k43',100)
    kg.addConquerCostByName('k44',1)
    kg.addConquerCostByName('k45',20)
    kg.addConquerCostByName('k46',10)
    kg.addConquerCostByName('k47',30)
    kg.addConquerCostByName('k48',150)
    kg.addConquerCostByName('k49',20)
    kg.addConquerCostByName('k50',10)

    # edge costs
    # connect Lawrence and Kevin's
    kg.addEdgeByName('k1','l1',1)
    # northwest
    kg.addEdgeByName('k1','k4',5)
    kg.addEdgeByName('k1','k2',10)
    kg.addEdgeByName('k1','k3',18)
    kg.addEdgeByName('k2','k7',5)
    kg.addEdgeByName('k4','k5',2)
    kg.addEdgeByName('k5','k6',3)
    kg.addEdgeByName('k6','k7',1)
    kg.addEdgeByName('k5','k8',3)
    kg.addEdgeByName('k6','k19',100)
    kg.addEdgeByName('k7','k27',5)
    # north
    kg.addEdgeByName('k8','k9',10)
    kg.addEdgeByName('k8','k13',20)
    kg.addEdgeByName('k8','k11',50)
    kg.addEdgeByName('k9','k10',40)
    kg.addEdgeByName('k10','k13',10)
    kg.addEdgeByName('k12','k13',80)
    kg.addEdgeByName('k11','k12',10)
    kg.addEdgeByName('k10','k14',10)
    # northeast
    kg.addEdgeByName('k14','k15',50)
    kg.addEdgeByName('k15','k16',81)
    kg.addEdgeByName('k15','k17',80)
    kg.addEdgeByName('k16','k17',1)
    kg.addEdgeByName('k14','k18',10)
    kg.addEdgeByName('k18','k21',10)
    kg.addEdgeByName('k21','k23',10)
    kg.addEdgeByName('k23','k26',20)
    kg.addEdgeByName('k26','k25',71)
    kg.addEdgeByName('k25','k24',1)
    kg.addEdgeByName('k24','k22',10)
    kg.addEdgeByName('k22','k20',10)
    kg.addEdgeByName('k20','k18',10)
    kg.addEdgeByName('k20','k19',80)
    # southwest
    kg.addEdgeByName('k27','k29',10)
    kg.addEdgeByName('k29','k30',10)
    kg.addEdgeByName('k30','k31',10)
    kg.addEdgeByName('k31','k33',31)
    kg.addEdgeByName('k29','k32',5)
    kg.addEdgeByName('k32','k33',6)
    kg.addEdgeByName('k27','k28',5)
    kg.addEdgeByName('k28','k33',5)
    kg.addEdgeByName('k33','k34',1)
    # south
    kg.addEdgeByName('k34','k35',5)
    kg.addEdgeByName('k35','k36',3)
    kg.addEdgeByName('k36','k37',2)
    kg.addEdgeByName('k34','k39',10)
    kg.addEdgeByName('k34','k41',4)
    kg.addEdgeByName('k41','k40',15)
    kg.addEdgeByName('k40','k39',1)
    kg.addEdgeByName('k39','k38',3)
    kg.addEdgeByName('k37','k39',5)
    kg.addEdgeByName('k37','k38',7)
    kg.addEdgeByName('k38','k42',10)
    kg.addEdgeByName('k42','k43',2)
    kg.addEdgeByName('k43','k44',2)
    kg.addEdgeByName('k43','k45',2)
    kg.addEdgeByName('k45','k46',5)
    kg.addEdgeByName('k46','k47',4)
    kg.addEdgeByName('k47','k48',3)
    kg.addEdgeByName('k48','k49',5)
    kg.addEdgeByName('k48','k50',2)

    #kingdomGraphToInputFile("m50_input.in", kg)
    kingdomGraphToInputFile("100.in", kg)

    # test drawing graph
    # drawFromKingdomGraph(kg)
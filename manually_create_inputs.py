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

    # Combined 100 kingdoms

    # for 100 kingdoms:
    # kg = KingdomGraph(100, starting_kingdom="l1", kingdom_names=['l{}'.format(i+1) for i in range(50)] +['k{}'.format(i+1) for i in range(50)])
    
    # for 200 kingdoms:
    kg = KingdomGraph(200,
                      starting_kingdom="l1",
                      kingdom_names=['l{}'.format(i+1) for i in range(50)] \
                                  + ['k{}'.format(i+1) for i in range(50)] \
                                  + ['L{}'.format(i+1) for i in range(50)] \
                                  + ['K{}'.format(i+1) for i in range(50)])

    # kg = KingdomGraph(50, starting_kingdom="l1", kingdom_names=['l{}'.format(i+1) for i in range(50)])

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
    kg.addEdgeByName('l12', 'l13', 8)
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
    kg.addEdgeByName('l46', 'l48', 10)
    kg.addEdgeByName('l46', 'l49', 10)
    kg.addEdgeByName('l48', 'l49', 2)
    kg.addEdgeByName('l49', 'l50', 21)

    kingdomGraphToInputFile("50_lawrence.in", kg)

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
    kg.addEdgeByName('k3','k6',6)
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



    kingdomGraphToInputFile("100.in", kg)
    # END of 100
    

    # DUPLICATING 50 of Lawrence's kingdoms to create 150
    kg.addConquerCostByName('L1', 10000)
    kg.addConquerCostByName('L2', 9)
    kg.addConquerCostByName('L3', 5)
    kg.addConquerCostByName('L4', 1)
    kg.addConquerCostByName('L5', 8)
    kg.addConquerCostByName('L6', 5)
    kg.addConquerCostByName('L7', 20)
    kg.addConquerCostByName('L8', 2)
    kg.addConquerCostByName('L9', 8)
    kg.addConquerCostByName('L10', 10)
    kg.addConquerCostByName('L11', 7)
    kg.addConquerCostByName('L12', 11)
    kg.addConquerCostByName('L13', 1)
    kg.addConquerCostByName('L14', 7)
    kg.addConquerCostByName('L15', 3)
    kg.addConquerCostByName('L16', 7)
    kg.addConquerCostByName('L17', 8)
    kg.addConquerCostByName('L18', 20)
    kg.addConquerCostByName('L19', 1)
    kg.addConquerCostByName('L20', 3)
    kg.addConquerCostByName('L21', 24)
    kg.addConquerCostByName('L22', 3)
    kg.addConquerCostByName('L23', 8)
    kg.addConquerCostByName('L24', 15)
    kg.addConquerCostByName('L25', 4)
    kg.addConquerCostByName('L26', 5)
    kg.addConquerCostByName('L27', 2)
    kg.addConquerCostByName('L28', 7)
    kg.addConquerCostByName('L29', 3)
    kg.addConquerCostByName('L30', 10)
    kg.addConquerCostByName('L31', 5)
    kg.addConquerCostByName('L32', 30)
    kg.addConquerCostByName('L33', 1)
    kg.addConquerCostByName('L34', 66)
    kg.addConquerCostByName('L35', 7)
    kg.addConquerCostByName('L36', 3)
    kg.addConquerCostByName('L37', 7)
    kg.addConquerCostByName('L38', 5)
    kg.addConquerCostByName('L39', 2)
    kg.addConquerCostByName('L40', 15)
    kg.addConquerCostByName('L41', 7)
    kg.addConquerCostByName('L42', 2)
    kg.addConquerCostByName('L43', 9)
    kg.addConquerCostByName('L44', 10)
    kg.addConquerCostByName('L45', 9)
    kg.addConquerCostByName('L46', 100)
    kg.addConquerCostByName('L47', 7)
    kg.addConquerCostByName('L48', 8)
    kg.addConquerCostByName('L49', 50)
    kg.addConquerCostByName('L50', 3)

    # 7 clusters of 7

    # connect L (lawrence's second graph) through L1 to k33
    kg.addEdgeByName('L1', 'k33', 2)

    # 1
    kg.addEdgeByName('L1', 'L2', 2)
    kg.addEdgeByName('L2', 'L3', 10)
    kg.addEdgeByName('L3', 'L4', 1)
    kg.addEdgeByName('L2', 'L5', 5)
    kg.addEdgeByName('L2', 'L7', 7)
    kg.addEdgeByName('L5', 'L6', 1)
    kg.addEdgeByName('L6', 'L7', 5)
    kg.addEdgeByName('L7', 'L8', 40)

    # 2
    kg.addEdgeByName('L1', 'L9', 2)
    kg.addEdgeByName('L9', 'L10', 20)
    kg.addEdgeByName('L10', 'L11', 1)
    kg.addEdgeByName('L10', 'L12', 2)
    kg.addEdgeByName('L12', 'L13', 8)
    kg.addEdgeByName('L12', 'L14', 10)
    kg.addEdgeByName('L14', 'L15', 1)

    # 3
    kg.addEdgeByName('L1', 'L16', 100)
    kg.addEdgeByName('L16', 'L17', 1)
    kg.addEdgeByName('L16', 'L19', 3)
    kg.addEdgeByName('L17', 'L18', 7)
    kg.addEdgeByName('L19', 'L20', 2)
    kg.addEdgeByName('L20', 'L21', 9)
    kg.addEdgeByName('L18', 'L21', 1)
    kg.addEdgeByName('L21', 'L22', 1)

    # 4
    kg.addEdgeByName('L1', 'L23', 75)
    kg.addEdgeByName('L23', 'L24', 5)
    kg.addEdgeByName('L24', 'L25', 3)
    kg.addEdgeByName('L24', 'L26', 2)
    kg.addEdgeByName('L23', 'L27', 2)
    kg.addEdgeByName('L24', 'L27', 4)
    kg.addEdgeByName('L27', 'L28', 7)
    kg.addEdgeByName('L28', 'L29', 5)

    # 5
    kg.addEdgeByName('L1', 'L30', 50)
    kg.addEdgeByName('L30', 'L31', 2)
    kg.addEdgeByName('L30', 'L32', 3)
    kg.addEdgeByName('L31', 'L32', 4)
    kg.addEdgeByName('L32', 'L33', 12)
    kg.addEdgeByName('L33', 'L34', 13)
    kg.addEdgeByName('L32', 'L34', 2)
    kg.addEdgeByName('L34', 'L35', 2)
    kg.addEdgeByName('L35', 'L36', 7)
    kg.addEdgeByName('L34', 'L36', 8)

    # 6
    kg.addEdgeByName('L1', 'L37', 1000)
    kg.addEdgeByName('L37', 'L38', 1)
    kg.addEdgeByName('L38', 'L39', 2)
    kg.addEdgeByName('L37', 'L40', 2)
    kg.addEdgeByName('L40', 'L41', 1)
    kg.addEdgeByName('L41', 'L42', 8)
    kg.addEdgeByName('L40', 'L43', 9)

    # 7
    kg.addEdgeByName('L1', 'L44', 25)
    kg.addEdgeByName('L44', 'L45', 2)
    kg.addEdgeByName('L44', 'L46', 1)
    kg.addEdgeByName('L45', 'L46', 2)
    kg.addEdgeByName('L46', 'L47', 20)
    kg.addEdgeByName('L46', 'L48', 10)
    kg.addEdgeByName('L46', 'L49', 10)
    kg.addEdgeByName('L48', 'L49', 2)
    kg.addEdgeByName('L49', 'L50', 21)


    # DUPLICATING 50 of Kevins's kingdoms to create 200

    kg.addConquerCostByName('K1',1000)
    kg.addConquerCostByName('K2',3)
    kg.addConquerCostByName('K3',5)
    kg.addConquerCostByName('K4',10)
    kg.addConquerCostByName('K5',60)
    kg.addConquerCostByName('K6',100)
    kg.addConquerCostByName('K7',1)
    kg.addConquerCostByName('K8',10)
    kg.addConquerCostByName('K9',60)
    kg.addConquerCostByName('K10',30)
    kg.addConquerCostByName('K11',30)
    kg.addConquerCostByName('K12',100)
    kg.addConquerCostByName('K13',5)
    kg.addConquerCostByName('K14',20)
    kg.addConquerCostByName('K15',100)
    kg.addConquerCostByName('K16',10)
    kg.addConquerCostByName('K17',60)
    kg.addConquerCostByName('K18',10)
    kg.addConquerCostByName('K19',5)
    kg.addConquerCostByName('K20',90)
    kg.addConquerCostByName('K21',20)
    kg.addConquerCostByName('K22',50)
    kg.addConquerCostByName('K23',50)
    kg.addConquerCostByName('K24',1)
    kg.addConquerCostByName('K25',10)
    kg.addConquerCostByName('K26',100)
    kg.addConquerCostByName('K27',10)
    kg.addConquerCostByName('K28',70)
    kg.addConquerCostByName('K29',80)
    kg.addConquerCostByName('K30',10)
    kg.addConquerCostByName('K31',90)
    kg.addConquerCostByName('K32',20)
    kg.addConquerCostByName('K33',100)
    kg.addConquerCostByName('K34',15)
    kg.addConquerCostByName('K35',10)
    kg.addConquerCostByName('K36',5)
    kg.addConquerCostByName('K37',20)
    kg.addConquerCostByName('K38',10)
    kg.addConquerCostByName('K39',20)
    kg.addConquerCostByName('K40',20)
    kg.addConquerCostByName('K41',30)
    kg.addConquerCostByName('K42',4)
    kg.addConquerCostByName('K43',100)
    kg.addConquerCostByName('K44',1)
    kg.addConquerCostByName('K45',20)
    kg.addConquerCostByName('K46',10)
    kg.addConquerCostByName('K47',30)
    kg.addConquerCostByName('K48',150)
    kg.addConquerCostByName('K49',20)
    kg.addConquerCostByName('K50',10)

    # edge costs
    # connect Lawrence and Kevin's
    kg.addEdgeByName('K1','l23',1)
    # northwest
    kg.addEdgeByName('K1','K4',5)
    kg.addEdgeByName('K1','K2',10)
    kg.addEdgeByName('K1','K3',18)
    kg.addEdgeByName('K3','K6',6)
    kg.addEdgeByName('K2','K7',5)
    kg.addEdgeByName('K4','K5',2)
    kg.addEdgeByName('K5','K6',3)
    kg.addEdgeByName('K6','K7',1)
    kg.addEdgeByName('K5','K8',3)
    kg.addEdgeByName('K6','K19',100)
    kg.addEdgeByName('K7','K27',5)
    # north
    kg.addEdgeByName('K8','K9',10)
    kg.addEdgeByName('K8','K13',20)
    kg.addEdgeByName('K8','K11',50)
    kg.addEdgeByName('K9','K10',40)
    kg.addEdgeByName('K10','K13',10)
    kg.addEdgeByName('K12','K13',80)
    kg.addEdgeByName('K11','K12',10)
    kg.addEdgeByName('K10','K14',10)
    # northeast
    kg.addEdgeByName('K14','K15',50)
    kg.addEdgeByName('K15','K16',81)
    kg.addEdgeByName('K15','K17',80)
    kg.addEdgeByName('K16','K17',1)
    kg.addEdgeByName('K14','K18',10)
    kg.addEdgeByName('K18','K21',10)
    kg.addEdgeByName('K21','K23',10)
    kg.addEdgeByName('K23','K26',20)
    kg.addEdgeByName('K26','K25',71)
    kg.addEdgeByName('K25','K24',1)
    kg.addEdgeByName('K24','K22',10)
    kg.addEdgeByName('K22','K20',10)
    kg.addEdgeByName('K20','K18',10)
    kg.addEdgeByName('K20','K19',80)
    # southwest
    kg.addEdgeByName('K27','K29',10)
    kg.addEdgeByName('K29','K30',10)
    kg.addEdgeByName('K30','K31',10)
    kg.addEdgeByName('K31','K33',31)
    kg.addEdgeByName('K29','K32',5)
    kg.addEdgeByName('K32','K33',6)
    kg.addEdgeByName('K27','K28',5)
    kg.addEdgeByName('K28','K33',5)
    kg.addEdgeByName('K33','K34',1)
    # south
    kg.addEdgeByName('K34','K35',5)
    kg.addEdgeByName('K35','K36',3)
    kg.addEdgeByName('K36','K37',2)
    kg.addEdgeByName('K34','K39',10)
    kg.addEdgeByName('K34','K41',4)
    kg.addEdgeByName('K41','K40',15)
    kg.addEdgeByName('K40','K39',1)
    kg.addEdgeByName('K39','K38',3)
    kg.addEdgeByName('K37','K39',5)
    kg.addEdgeByName('K37','K38',7)
    kg.addEdgeByName('K38','K42',10)
    kg.addEdgeByName('K42','K43',2)
    kg.addEdgeByName('K43','K44',2)
    kg.addEdgeByName('K43','K45',2)
    kg.addEdgeByName('K45','K46',5)
    kg.addEdgeByName('K46','K47',4)
    kg.addEdgeByName('K47','K48',3)
    kg.addEdgeByName('K48','K49',5)
    kg.addEdgeByName('K48','K50',2)

    # kingdomGraphToInputFile("m50_input.in", kg)
    kingdomGraphToInputFile("200.in", kg)
    # kingdomGraphToInputFile("50_lawrence.in", kg)
    # test drawing graph
    # drawFromKingdomGraph(kg)
import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
from student_utils_sp18 import *
sys.path.insert(0, './python-christofides-0.1.2')
from pyChristofides import christofides

"""
======================================================================
  Complete the following function.
======================================================================
"""


def solve(list_of_kingdom_names, starting_kingdom, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_kingdom_names: An list of kingdom names such that node i of the graph corresponds to name index i in the list
        starting_kingdom: The name of the starting kingdom for the walk
        adjacency_matrix: The adjacency matrix from the input file

    Output:
        Return 2 things. The first is a list of kingdoms representing the walk, and the second is the set of kingdoms that are conquered
    """

    dict_conquer_strategies = {
        'naive': naiveGreedy,
        'dijkstras': dijkstrasGreedy,
        'dijkstras-degree': dijkstrasAndDegreeGreedy
    }

    dict_path_strategies = {
        'steiner-DFS': steinerDFS,
        'christo-TSP': christoTSP
    }

    if len(params) == 0:
        params.append('dijkstras-degree')
    if len(params) < 2:
        params.append('steiner-DFS')

    conquer_strategy = dict_conquer_strategies[params[0]]
    path_strategy = dict_path_strategies[params[1]]

    ### TOOLKIT ###
    N = len(list_of_kingdom_names)
    dict_kingdom_index_to_name = {i: name for i, name in enumerate(list_of_kingdom_names)}
    dict_kingdom_name_to_index = {name: i for i, name in enumerate(list_of_kingdom_names)}
    tuples_kingdom_name_to_cost = [(name, cost) for name, cost in zip(list_of_kingdom_names, [adjacency_matrix[i][i] for i in range(len(list_of_kingdom_names))])]
    starting_kingdom_index = dict_kingdom_name_to_index[starting_kingdom]
    dict_kingdom_index_to_cost = {i: adjacency_matrix[i][i] for i in range(N)}
    adjacency_lists = adjacency_matrix_to_adjacency_lists(adjacency_matrix)

    tools = {
        'N': N,
        'dict_kingdom_index_to_name': dict_kingdom_index_to_name,
        'dict_kingdom_name_to_index': dict_kingdom_name_to_index,
        'tuples_kingdom_name_to_cost': tuples_kingdom_name_to_cost,
        'starting_kingdom_index': starting_kingdom_index,
        'dict_kingdom_index_to_cost': dict_kingdom_index_to_cost,
        'adjacency_lists': adjacency_lists
    }

    ## --- STEP 1: FIND KINGDOMS TO CONQUER --- ##
    conquered_kingdoms = conquer_strategy(list_of_kingdom_names, adjacency_matrix, starting_kingdom, **tools)
    conquered_kingdoms_indices = [dict_kingdom_name_to_index[i] for i in conquered_kingdoms]


    ## --- STEP 2: FIND PATH THROUGH KINGDOMS TO CONQUER --- ##
    closed_walk = path_strategy(list_of_kingdom_names, starting_kingdom, adjacency_matrix, conquered_kingdoms_indices, **tools)

    return closed_walk, conquered_kingdoms


###########################################
## --- KINGDOM CONQUERING STRATEGIES --- ##
###########################################

def naiveGreedy(list_of_kingdom_names, adjacency_matrix, starting_kingdom,
        N, dict_kingdom_index_to_name, dict_kingdom_name_to_index, tuples_kingdom_name_to_cost, starting_kingdom_index, dict_kingdom_index_to_cost, adjacency_lists):
    """Order kingdoms by increasing cost to conquer"""
    for key, value in styles.iteritems():      # styles is a regular dictionary
        setattr(someobject, key, value)
    tuples_kingdom_name_to_self_cost = [(name, cost) for name, cost in zip(list_of_kingdom_names, [adjacency_matrix[i][i] for i in range(len(list_of_kingdom_names))])]
    sorted_kingdom_tuples_by_self_cost = sorted(tuples_kingdom_name_to_self_cost, key=lambda x: x[1])
    order = [tup[0] for tup in sorted_kingdom_tuples_by_self_cost]
    conquered_kingdoms = conquerKingdoms(order, adjacency_matrix, len(list_of_kingdom_names), dict_kingdom_name_to_index, dict_kingdom_index_to_cost, dict_kingdom_index_to_name)
    return conquered_kingdoms


def dijkstrasGreedy(list_of_kingdom_names, adjacency_matrix, starting_kingdom,
        N, dict_kingdom_index_to_name, dict_kingdom_name_to_index, tuples_kingdom_name_to_cost, starting_kingdom_index, dict_kingdom_index_to_cost, adjacency_lists):
    """Order kingdoms by the length of the shortest path from the starting kingdom to it + cost to conquer"""
    G = buildGraph(list_of_kingdom_names, adjacency_matrix, dict_kingdom_index_to_name)
    shortest_paths_lengths = nx.algorithms.single_source_dijkstra_path_length(G, starting_kingdom)
    tuples_kingdom_name_to_self_cost = [(name, cost) for name, cost in zip(list_of_kingdom_names, [adjacency_matrix[i][i] for i in range(len(list_of_kingdom_names))])]
    tuples_kingdom_name_to_total_cost = [(tup[0], tup[1] + shortest_paths_lengths[tup[0]]) for tup in tuples_kingdom_name_to_self_cost]
    sorted_kingdom_tuples_by_total_cost = sorted(tuples_kingdom_name_to_total_cost, key=lambda x: x[1])
    order = [tup[0] for tup in sorted_kingdom_tuples_by_total_cost]
    conquered_kingdoms = conquerKingdoms(order, adjacency_matrix, len(list_of_kingdom_names), dict_kingdom_name_to_index, dict_kingdom_index_to_cost, dict_kingdom_index_to_name)
    return conquered_kingdoms


def dijkstrasAndDegreeGreedy(list_of_kingdom_names, adjacency_matrix, starting_kingdom,
        N, dict_kingdom_index_to_name, dict_kingdom_name_to_index, tuples_kingdom_name_to_cost, starting_kingdom_index, dict_kingdom_index_to_cost, adjacency_lists):
    """Order kingdoms by dijkstra's greedy cost divided by the degree of the kingdom"""
    G = buildGraph(list_of_kingdom_names, adjacency_matrix, dict_kingdom_index_to_name)
    shortest_paths_lengths = nx.algorithms.single_source_dijkstra_path_length(G, starting_kingdom)
    tuples_kingdom_name_to_self_cost = [(name, cost) for name, cost in zip(list_of_kingdom_names, [adjacency_matrix[i][i] for i in range(len(list_of_kingdom_names))])]
    tuples_kingdom_name_to_total_cost = [(kingdom, (cost + shortest_paths_lengths[kingdom]) / countNeighbors(kingdom, adjacency_matrix, dict_kingdom_name_to_index)) for kingdom, cost in tuples_kingdom_name_to_self_cost]
    sorted_kingdom_tuples_by_total_cost = sorted(tuples_kingdom_name_to_total_cost, key=lambda x: x[1])
    order = [kingdom for kingdom, cost in sorted_kingdom_tuples_by_total_cost]
    conquered_kingdoms = conquerKingdoms(order, adjacency_matrix, len(list_of_kingdom_names), dict_kingdom_name_to_index, dict_kingdom_index_to_cost, dict_kingdom_index_to_name)
    return conquered_kingdoms

def countNeighbors(kingdom, adjacency_matrix, dict_kingdom_name_to_index):
    """Counts number of neighbors of a kingdom, helper function for dijstrasAndDegreeGreedy + 1"""
    kingdom_index = dict_kingdom_name_to_index[kingdom]
    neighbors = adjacency_matrix[kingdom_index]
    return sum(neighbor != 'x' for neighbor in neighbors) + 1


## -- KINGDOM CONQUERING TOOLKIT -- ##

def conquerKingdoms(order, adjacency_matrix, N, dict_kingdom_name_to_index, dict_kingdom_index_to_cost, dict_kingdom_index_to_name):
    """Conquers kingdoms until all surrendered.
    1) First sort kingdoms by conquer cost
    2) Check kingdom X:
    3) Check if at least one neighbor is in set to conquer (so X itself surrenders)
    4) For each neighbor, check if it is conquered or has at least neighbor in set to conquer"""
    adjacency_lists = adjacency_matrix_to_adjacency_lists(adjacency_matrix)
    set_surrendered_indices = set()
    conquered_kingdoms_indices = []
    while len(set_surrendered_indices) < N:
        # pop of next
        tentative_conquer_name = order.pop(0)
        tentative_conquer_index = dict_kingdom_name_to_index[tentative_conquer_name]
        # test if conquering actually forces new kingdoms to surrender
        helpful = False
        for kingdom in adjacency_lists[tentative_conquer_index] + [tentative_conquer_index]:
            if kingdom not in set_surrendered_indices:
                helpful = True
                break
        if helpful:
            conquered_kingdoms_indices.append(tentative_conquer_index)
            for kingdom in adjacency_lists[tentative_conquer_index] + [tentative_conquer_index]:
                set_surrendered_indices.add(kingdom)

    # Remove most expensive kingdoms that lead to over-conquering (i.e. don't need to be conquered)
    set_conquered_kingdoms_indices = set(conquered_kingdoms_indices)
    has_conquered_neighbors = lambda X: any(neighbor in set_conquered_kingdoms_indices for neighbor in adjacency_lists[X])
    for X in reversed(sorted(conquered_kingdoms_indices, key=lambda i: dict_kingdom_index_to_cost[i])):
        if has_conquered_neighbors(X) and all(has_conquered_neighbors(neighbor) or neighbor in set_conquered_kingdoms_indices for neighbor in adjacency_lists[X] if neighbor != X):
            set_conquered_kingdoms_indices.remove(X)

    conquered_kingdoms = [dict_kingdom_index_to_name[i] for i in conquered_kingdoms_indices]
    return conquered_kingdoms

def buildGraph(list_of_kingdom_names, adjacency_matrix, dict_kingdom_index_to_name):
    """Builds graph using adjacency matrix"""
    adjacency_lists = adjacency_matrix_to_adjacency_lists(adjacency_matrix)
    G = nx.Graph()
    for kingdom_name in list_of_kingdom_names:
        G.add_node(kingdom_name)

    # Populate edges in the graph
    for i in range(len(list_of_kingdom_names)):
        for j in adjacency_lists[i]:
            G.add_edge(dict_kingdom_index_to_name[i], dict_kingdom_index_to_name[j], weight=adjacency_matrix[i][j])

    return G

## -- STEINER TREE + DFS PATH STRATEGY -- ##

def steinerDFS(list_of_kingdom_names, starting_kingdom, adjacency_matrix, conquered_kingdoms_indices,
        N, dict_kingdom_index_to_name, dict_kingdom_name_to_index, tuples_kingdom_name_to_cost, starting_kingdom_index, dict_kingdom_index_to_cost, adjacency_lists):
    G = adjacency_matrix_to_graph(adjacency_matrix)
    special_nodes = conquered_kingdoms_indices
    if starting_kingdom_index not in special_nodes:
        special_nodes.append(starting_kingdom_index)
    st = nx.algorithms.approximation.steinertree.steiner_tree(G, special_nodes)

    visited = []
    for _ in range(len(adjacency_lists)):
        visited.append(False)
    count = 0
    visited_order = []

    def dfs(curr_kingdom):
        visited[curr_kingdom] = True
        nonlocal count
        count += 1
        visited_order.append(curr_kingdom)
        for x in st[curr_kingdom]:
            if not visited[x]:
                dfs(x)
                if(count != len(st)):
                    visited_order.append(curr_kingdom)

    if len(conquered_kingdoms_indices) == 1:
        visited_order = conquered_kingdoms_indices
    else:
        dfs(starting_kingdom_index)
        original_graph = adjacency_matrix_to_graph(adjacency_matrix)
        return_path = nx.algorithms.astar_path(original_graph, visited_order.pop(len(visited_order)-1), starting_kingdom_index)
        visited_order.extend(return_path)

    closed_walk = [dict_kingdom_index_to_name[i] for i in visited_order]

    return closed_walk


## -- CHRISTOFIDES TSP STRATEGY -- ##

def christoTSP(list_of_kingdom_names, starting_kingdom, adjacency_matrix, conquered_kingdoms_indices,
        N, dict_kingdom_index_to_name, dict_kingdom_name_to_index, tuples_kingdom_name_to_cost, starting_kingdom_index, dict_kingdom_index_to_cost, adjacency_lists):
    
    # build TSP distance matrix to represent each node in conquered_kingdoms_indices
    # contain edges of weight based on shortest path
    G = adjacency_matrix_to_graph(adjacency_matrix)
    shortest_paths = dict(nx.shortest_path(G, weight="weight"))
    shortest_lengths = dict(nx.shortest_path_length(G, weight="weight"))

    N_TSP = len(conquered_kingdoms_indices)
    dict_TSP_index_to_index = { TSP_index: index for TSP_index, index in enumerate(conquered_kingdoms_indices)}
    dict_index_to_TSP_index = { index: TSP_index for TSP_index, index in enumerate(conquered_kingdoms_indices)}

    distance_matrix = [[0] * N_TSP] * N_TSP
    print(N_TSP)

    print(shortest_lengths)
    print(distance_matrix)

    for i in range(N_TSP):
        for j in range(i + 1, N_TSP):
            print(i, j, shortest_lengths[i][j])
            distance_matrix[i][j] = shortest_lengths[i][j]
    closed_walk = []

    print(distance_matrix)

    # run christofides

    return closed_walk

"""
======================================================================
   No need to change any code below this line
======================================================================
"""


def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)

    input_data = utils.read_file(input_file)
    number_of_kingdoms, list_of_kingdom_names, starting_kingdom, adjacency_matrix = data_parser(input_data)
    closed_walk, conquered_kingdoms = solve(list_of_kingdom_names, starting_kingdom, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    output_filename = utils.input_to_output(filename)
    output_file = f'{output_directory}/{output_filename}'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    utils.write_data_to_file(output_file, closed_walk, ' ')
    utils.write_to_file(output_file, '\n', append=True)
    utils.write_data_to_file(output_file, conquered_kingdoms, ' ', append=True)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)

def solve_all_from_list(input_directory, output_directory, list_file_name, params=[]):
    files = []

    with open(list_file_name) as f:
        filenames = f.read().splitlines()

    for name in os.listdir(input_directory):
        if name.endswith("in") and name in filenames:
            files.append(f'{input_directory}/{name}')

    for input_file in files:
        solve_from_file(input_file, output_directory, params=params)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true',
                        help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('--fromlist', action='store_true',
                        help='If specified, olve all the files give an input file describing a list of files (in params)')
    parser.add_argument('input', type=str, help='The path to the input file or directory or input_list')
    parser.add_argument('output_directory', type=str, nargs='?', default='.',
                        help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER,
                        help='Extra arguments passed in (file of the list of files)')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        print(args.all)
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    elif args.fromlist:
        # Example: python3 solver_template.py --fromlist inputs outputs-astar files_up_to_size/inputs_lim_15
        input_directory = args.input
        input_list_file = args.params[0]
        solve_all_from_list(input_directory, output_directory, input_list_file, params=args.params[1:])
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)

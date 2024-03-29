"""Simple network optimization problem"""

from __future__ import print_function
import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Locations in seconds. to convert to degrees use high school math
    data['locations'] = [
        (152045, -299332),
        (152042, -299334),
        (152029, -299343),
        (152034, -299335),
        (152035, -299333),
        (152044, -299337),
        (152043, -299341),
        (152041, -299378),
        (152040, -299364),
        (152042, -299365),
        (152032, -299371),
        (152032, -299357),
        (152032, -299385),
        (152036, -299386),
        (152027, -299337),
        (152031, -299332),
        (152029, -299356),
        (152015, -299374),
        (152026, -299364),
        (151986, -299428),
        (151989, -299447),
        (151973, -299447),
        (151973, -299442),
        (151972, -299444),
        (151974, -299436),
        (151974, -299430),
        (151973, -299424),
        (152020, -299358),
        (152016, -299357),
        (152019, -299358),
        (152019, -299356),
        (152010, -299360),
        (152002, -299350),
        (152004, -299341),
        (152000, -299342),
        (151999, -299344),
        (152000, -299346),
        (151989, -299377),
        (152006, -299368),
        (152083, -299348),
        (152006, -299396),
        (151987, -299399),
        (152000, -299387),
        (151988, -299409),
        (151976, -299412),
        (151974, -299389),
        (151996, -299349),
        (151990, -299344),
        (151988, -299345),
        (151988, -299348),
        (151987, -299353),
        (151988, -299358),
        (151988, -299360),
        (151987, -299359),
        (151975, -299353),
        (151981, -299347),
        (151971, -299340),
        (151980, -299350),
        (151963, -299359),
        (151967, -299345),
        (151965, -299344),
        (151963, -299344),
        (151960, -299344),
        (151958, -299344),
        (151956, -299349),
        (151958, -299349),
        (151964, -299340),
        (151958, -299340),
        (151952, -299338),
        (151953, -299344),
        (151950, -299343),
        (151950, -299340),
        (151948, -299340),
        (151947, -299339),
        (151946, -299336),
        (151946, -299344),
        (151944, -299451),
        (151944, -299347),
        (151954, -299349),
        (151952, -299349),
        (151948, -299362),
        (151946, -299351),
        (151940, -299347),
        (151942, -299348),
        (151941, -299336),
        (151942, -299333),
        (151939, -299330),
        (151955, -299323),
        (151956, -299403),
        (151956, -299357),
        (151966, -299337),
        (151936, -299347),
        (151938, -299341),
        (151929, -299345),
        (151938, -299351),
        (151932, -299349),
        (151930, -299348),
        (151928, -299335),
        (151925, -299336),
        (151922, -299338),
        (151925, -299334),
        (151937, -299333),
        (151965, -299355),
        (151963, -299355),
        (151956, -299361),
        (151952, -299368),
        (151954, -299362),
        (151952, -299355),
        (151959, -299355),
        (151961, -299357),
        (151962, -299354),
        (151958, -299361),
        (151955, -299384),
        (151969, -299411),
        (151944, -299383),
        (151943, -299382),
        (151940, -299387),
        (151938, -299385),
        (151935, -299385),
        (151937, -299395),
        (151935, -299392),
        (151941, -299395),
        (151943, -299395),
        (151946, -299396),
        (151939, -299391),
        (151931, -299385),
        (151934, -299394),
        (151931, -299392),
        (151930, -299393),
        (151925, -299387),
        (151928, -299392),
        (151926, -299393),
        (151924, -299393),
        (151922, -299392),
        (151920, -299390),
        (151916, -299397),
        (151943, -299402),
        (151943, -299406),
        (151941, -299408),
        (151941, -299405),
        (151939, -299407),
        (151941, -299400),
        (151939, -299400),
        (151937, -299400),
        (151935, -299399),
        (151937, -299406),
        (151935, -299406),
        (151933, -299406),
        (151931, -299404),
        (151933, -299400),
        (151929, -299400),
        (151927, -299400),
        (151929, -299406),
        (151927, -299405),
        (151925, -299408),
        (151923, -299406),
        (151925, -299399),
        (151924, -299400),
        (151922, -299398),
        (151922, -299406),
        (151920, -299407),
        (151942, -299356),
        (151942, -299353),
        (151940, -299355),
        (151946, -299361),
        (151942, -299361),
        (151944, -299367),
        (151946, -299367),
        (151939, -299370),
        (151942, -299364),
        (151939, -299373),
        (151935, -299367),
        (151935, -299371),
        (151934, -299366),
        (151930, -299364),
        (151930, -299371),
        (151926, -299363),
        (151938, -299357),
        (151934, -299359),
        (151932, -299360),
        (151934, -299355),
        (151934, -299352),
        (151932, -299356),
        (151928, -299355),
        (151923, -299359),
        (151925, -299354),
        (151923, -299355),
        (151945, -299374),
        (151935, -299358),
        (151962, -299416),
        (151955, -299422),
        (151966, -299423),
        (151953, -299424),
        (151957, -299428),
        (151966, -299426),
        (151966, -299428),
        (151959, -299430),
        (151951, -299432),
        (151966, -299435),
        (151957, -299434),
        (151951, -299434),
        (151947, -299438),
        (151966, -299437),
        (151958, -299436),
        (151953, -299436),
        (151960, -299439),
        (151966, -299441),
        (151941, -299412),
        (151941, -299415),
        (151941, -299421),
        (151935, -299414),
        (151938, -299416),
        (151937, -299412),
        (151942, -299427),
        (151942, -299424),
        (151943, -299425),
        (151943, -299427),
        (151943, -299429),
        (151927, -299424),
        (151936, -299437),
        (151926, -299440),
        (151933, -299443),
        (151930, -299445),
        (151929, -299446),
        (151926, -299445),
        (151933, -299429),
        (151933, -299423),
        (151933, -299419),
        (151933, -299414),
        (151924, -299412),
        (151923, -299412),
        (151921, -299412),
        (151897, -299422),
        (151910, -299447),
        (151903, -299441),
        (151876, -299444),
        (151870, -299426),
        (151880, -299446),
        (151919, -299354),
        (151917, -299354),
        (151917, -299364),
        (151913, -299357),
        (151915, -299354),
        (151911, -299355),
        (151919, -299370),
        (151918, -299377),
        (151916, -299376),
        (151914, -299375),
        (151915, -299364),
        (151911, -299369),
        (151909, -299365),
        (151911, -299375),
        (151909, -299377),
        (151907, -299377),
        (151905, -299376),
        (151907, -299365),
        (151905, -299365),
        (151907, -299359),
        (151906, -299353),
        (151903, -299354),
        (151904, -299360),
        (151902, -299359),
        (151901, -299365),
        (151903, -299369),
        (151901, -299371),
        (151903, -299381),
        (151903, -299376),
        (151897, -299376),
        (151899, -299369),
        (151898, -299359),
        (151900, -299359),
        (151896, -299359),
        (151894, -299367),
        (151896, -299365),
        (151894, -299369),
        (151896, -299370),
        (151894, -299374),
        (151896, -299374),
        (151918, -299337),
        (151916, -299342),
        (151901, -299352),
        (151899, -299354),
        (151916, -299381),
        (151912, -299382),
        (151908, -299386),
        (151907, -299386),
        (151905, -299386),
        (151911, -299382),
        (151908, -299383),
        (151918, -299391),
        (151913, -299394),
        (151913, -299398),
        (151910, -299396),
        (151911, -299394),
        (151915, -299390),
        (151896, -299380),
        (151898, -299383),
        (151898, -299380),
        (151899, -299383),
        (151897, -299386),
    ]  # yapf: disableS
    data['num_vehicles'] = 1
    data['depot'] = 0
    return data


def compute_euclidean_distance_matrix(locations):
    """Creates callback to return distance between points."""
    distances = {}
    for from_counter, from_node in enumerate(locations):
        distances[from_counter] = {}
        for to_counter, to_node in enumerate(locations):
            if from_counter == to_counter:
                distances[from_counter][to_counter] = 0
            else:
                # Euclidean distance
                distances[from_counter][to_counter] = (int(
                    math.hypot((from_node[0] - to_node[0]),
                               (from_node[1] - to_node[1]))))
    return distances


def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    print('Objective: {}'.format(assignment.ObjectiveValue()))
    index = routing.Start(0)
    plan_output = 'Route:\n'
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} ->'.format(manager.IndexToNode(index))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)
    plan_output += 'Objective: {}m\n'.format(route_distance)


def main():
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['locations']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    distance_matrix = compute_euclidean_distance_matrix(data['locations'])

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distance_matrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if assignment:
        print_solution(manager, routing, assignment)


if __name__ == '__main__':
    main()

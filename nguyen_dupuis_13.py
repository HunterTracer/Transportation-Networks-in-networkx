import networkx as nx


def nguyen_dupuis_13():
    gv_od_graph = nx.DiGraph()
    gv_od_graph.add_edges_from([
        (1, 2, {"trip_rate": 19.0}),
        (1, 3, {"trip_rate": 38.0}),
        (4, 2, {"trip_rate": 28.5}),
        (4, 3, {"trip_rate": 9.5}),
    ])

    ev_od_graph = nx.DiGraph()
    ev_od_graph.add_edges_from([
        (1, 2,  {"trip_rate": 1.0}),
        (1, 3,  {"trip_rate": 2.0}),
        (4, 2,  {"trip_rate": 1.5}),
        (4, 3,  {"trip_rate": 0.5}),
    ])

    transport_graph = nx.DiGraph()
    transport_graph.add_nodes_from([
        (1,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (2,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (3,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (4,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (5,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (6,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (7,  {"type": "virtual", "capacity": 50., "time": 20. / 60.}),
        (8,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (9,  {"type": "virtual", "capacity": 50., "time": 20. / 60.}),
        (10, {"type": "virtual", "capacity": 50., "time": 20. / 60.}),
        (11, {"type": "regular", "capacity": 0.,  "time": 0.}),
        (12, {"type": "virtual", "capacity": 50., "time": 20. / 60.}),
        (13, {"type": "regular", "capacity": 0.,  "time": 0.}),
    ])
    transport_graph.add_edges_from([
        (1,  5,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (1,  12, {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (4,  5,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (4,  9,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (5,  6,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (5,  9,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (6,  7,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (6,  10, {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (7,  8,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (7,  11, {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (8,  2,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (9,  10, {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (9,  13, {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (10, 11, {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (11, 2,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (11, 3,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (12, 6,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (12, 8,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
        (13, 3,  {"type": "regular", "capacity": 60., "time": 20. / 60.}),
    ])

    for source, target in gv_od_graph.edges:
        edge_paths = list(nx.all_simple_edge_paths(transport_graph, source, target))
        gv_od_graph[source][target]["edge_paths"] = []
        gv_od_graph[source][target]["edge_paths_time"] = []
        for edge_path in edge_paths:
            edge_path_time = 0.
            for edge in edge_path:
                edge_path_time += transport_graph[edge[0]][edge[1]]["time"]
            gv_od_graph[source][target]["edge_paths"].append(edge_path)
            gv_od_graph[source][target]["edge_paths_time"].append(edge_path_time)

    for source, target in ev_od_graph.edges:
        edge_paths = list(nx.all_simple_edge_paths(transport_graph, source, target))
        ev_od_graph[source][target]["edge_paths"] = []
        ev_od_graph[source][target]["edge_paths_time"] = []
        for edge_path in edge_paths:
            edge_path_time = 0.
            for edge in edge_path:
                edge_path_time += transport_graph[edge[0]][edge[1]]["time"]
            for i in range(len(edge_path) - 1):
                if transport_graph.nodes[edge_path[i][0]]["type"] == "virtual":
                    ev_edge_path = edge_path[:]
                    ev_edge_path.insert(i, (edge_path[i][0], edge_path[i][0]))
                    ev_od_graph[source][target]["edge_paths"].append(ev_edge_path)
                    ev_od_graph[source][target]["edge_paths_time"].append(
                        edge_path_time + transport_graph.nodes[edge_path[i][0]]["time"])

    return gv_od_graph, ev_od_graph, transport_graph


if __name__ == "__main__":
    net = nguyen_dupuis_13()

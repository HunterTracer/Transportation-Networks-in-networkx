import networkx as nx


def ring_12():
    gv_od_graph = nx.DiGraph()
    gv_od_graph.add_edges_from([
        (1, 6,  {"trip_rate": 12.5}),
        (1, 10, {"trip_rate": 18.75}),
        (1, 11, {"trip_rate": 12.5}),
        (1, 12, {"trip_rate": 9.375}),

        (3, 6,  {"trip_rate": 12.5}),
        (3, 10, {"trip_rate": 9.375}),
        (3, 11, {"trip_rate": 10.0}),
        (3, 12, {"trip_rate": 6.25}),

        (4, 9,  {"trip_rate": 6.25}),
        (4, 10, {"trip_rate": 9.375}),
        (4, 12, {"trip_rate": 12.5}),
    ])

    ev_od_graph = nx.DiGraph()
    ev_od_graph.add_edges_from([
        (1, 6,  {"trip_rate": 2.0}),
        (1, 10, {"trip_rate": 3.0}),
        (1, 11, {"trip_rate": 3.2}),
        (1, 12, {"trip_rate": 2.4}),

        (3, 6,  {"trip_rate": 2.8}),
        (3, 10, {"trip_rate": 3.6}),
        (3, 11, {"trip_rate": 2.4}),
        (3, 12, {"trip_rate": 1.6}),

        (4, 9, {"trip_rate": 2.0}),
        (4, 10, {"trip_rate": 2.0}),
        (4, 12, {"trip_rate": 2.4}),
    ])

    transport_graph = nx.DiGraph()
    transport_graph.add_nodes_from([
        (1,  {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
        (2,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (3,  {"type": "regular", "capacity": 0.,  "time": 0.}),
        (4,  {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
        (5,  {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
        (6,  {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
        (7,  {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
        (8,  {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
        (9,  {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
        (10, {"type": "regular", "capacity": 0.,  "time": 0.}),
        (11, {"type": "regular", "capacity": 0.,  "time": 0.}),
        (12, {"type": "virtual", "capacity": 15., "time": 20. / 60.}),
    ])
    transport_graph.add_edges_from([
        (1,  2,  {"type": "regular", "capacity": 20.,  "time": 10. / 60.}),
        (1,  3,  {"type": "regular", "capacity": 18.,  "time": 6. / 60.}),
        (1,  4,  {"type": "regular", "capacity": 9.8,  "time": 5. / 60.}),

        (2,  1,  {"type": "regular", "capacity": 20.,  "time": 10. / 60.}),
        (2,  5,  {"type": "regular", "capacity": 7.9,  "time": 5.5 / 60.}),
        (2,  6,  {"type": "regular", "capacity": 17.,  "time": 6.5 / 60.}),

        (3,  1,  {"type": "regular", "capacity": 18.,  "time": 6. / 60.}),
        (3,  4,  {"type": "regular", "capacity": 8.5,  "time": 6. / 60.}),
        (3,  7,  {"type": "regular", "capacity": 19.,  "time": 10.2 / 60.}),

        (4,  1,  {"type": "regular", "capacity": 9.8,  "time": 5. / 60.}),
        (4,  3,  {"type": "regular", "capacity": 8.5,  "time": 6. / 60.}),
        (4,  5,  {"type": "regular", "capacity": 13.5, "time": 12. / 60.}),
        (4,  8,  {"type": "regular", "capacity": 14.,  "time": 11.5 / 60.}),

        (5,  2,  {"type": "regular", "capacity": 7.9,  "time": 5.5 / 60.}),
        (5,  4,  {"type": "regular", "capacity": 13.5, "time": 12. / 60.}),
        (5,  6,  {"type": "regular", "capacity": 8.2,  "time": 6.5 / 60.}),
        (5,  9,  {"type": "regular", "capacity": 13.8, "time": 12.5 / 60.}),

        (6,  2,  {"type": "regular", "capacity": 17.,  "time": 6.5 / 60.}),
        (6,  5,  {"type": "regular", "capacity": 8.2,  "time": 6.5 / 60.}),
        (6,  10, {"type": "regular", "capacity": 20.,  "time": 10.5 / 60.}),

        (7,  3,  {"type": "regular", "capacity": 19.,  "time": 10.2 / 60.}),
        (7,  8,  {"type": "regular", "capacity": 8.9,  "time": 5.8 / 60.}),
        (7,  11, {"type": "regular", "capacity": 17.5, "time": 6.3 / 60.}),

        (8,  4,  {"type": "regular", "capacity": 14.,  "time": 11.5 / 60.}),
        (8,  7,  {"type": "regular", "capacity": 8.9,  "time": 5.8 / 60.}),
        (8,  9,  {"type": "regular", "capacity": 13.2, "time": 11. / 60.}),
        (8,  11, {"type": "regular", "capacity": 9.76, "time": 5.7 / 60.}),

        (9,  5,  {"type": "regular", "capacity": 13.8, "time": 12.5 / 60.}),
        (9,  8,  {"type": "regular", "capacity": 13.2, "time": 11. / 60.}),
        (9,  10, {"type": "regular", "capacity": 9.15, "time": 5.9 / 60.}),
        (9,  12, {"type": "regular", "capacity": 8.97, "time": 5.8 / 60.}),

        (10, 6,  {"type": "regular", "capacity": 20.,  "time": 10.5 / 60.}),
        (10, 9,  {"type": "regular", "capacity": 9.15, "time": 5.9 / 60.}),
        (10, 12, {"type": "regular", "capacity": 18.2, "time": 6.1 / 60.}),

        (11, 7,  {"type": "regular", "capacity": 17.5, "time": 6.3 / 60.}),
        (11, 8,  {"type": "regular", "capacity": 9.76, "time": 5.7 / 60.}),
        (11, 12, {"type": "regular", "capacity": 20.,  "time": 9.8 / 60.}),

        (12, 9,  {"type": "regular", "capacity": 8.97, "time": 5.8 / 60.}),
        (12, 10, {"type": "regular", "capacity": 18.2, "time": 6.1 / 60.}),
        (12, 11, {"type": "regular", "capacity": 20.,  "time": 9.8 / 60.}),
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
    gv_od_graph, ev_od_graph, transport_graph = ring_12()

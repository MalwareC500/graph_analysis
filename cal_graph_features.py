import os
import networkx as nx
from networkx.drawing.nx_pydot import read_dot
import matplotlib.pyplot as plt
from networkx.classes.function import density
from networkx.algorithms.components import number_connected_components
from networkx.algorithms.centrality import closeness_centrality, degree_centrality, betweenness_centrality
from networkx.algorithms.distance_measures import radius, diameter
from networkx.algorithms.shortest_paths.generic import shortest_path, shortest_path_length
import numpy as np
import csv


def properties_of_array(d):
    deg = [val for key, val in d.items()]
    d = np.array(deg)
    return [np.min(d), np.max(d), np.median(d), np.mean(d), np.std(d)]

if __name__ == "__main__":
    csvfile = open("features.csv", mode="w")
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    label = []
    label.append("file name")
    label.append("number of nodes")
    label.append("number of edges")
    label.append("density")
    label.extend(["deg_min", "deg_max", "deg_median", "deg_mean", "deg_std"])
    label.extend(["closeness_min", "closeness_max", "closeness_median", "closeness_mean", "closeness_std"])
    label.extend(["betweeness_min", "betweeness_max", "betweeness_median", "betweeness_mean", "betweeness_std"])
    label.extend(["shortest_path_min", "shortest_path_max", "shortest_path_median", "shortest_path_mean", "shortest_path_std"])
    label.append("diameter")
    label.append("radius")
    csvwriter.writerow(label)
    for fname in os.listdir("output"):
        print(fname)
        try:
            G = read_dot(os.path.join("output", fname))
            nx.draw(G)
        except:
            print("cannot load graph")
            continue
        if G.number_of_nodes() == 0:
            print("Cannot read binary file")
            continue
        data = []
        data.append(fname)
        data.append(G.number_of_nodes())
        data.append(G.number_of_edges())
        data.append(density(G))
        deg_centrality = degree_centrality(G)
        data.extend(properties_of_array(deg_centrality))
        cln_centrality = closeness_centrality(G)
        data.extend(properties_of_array(cln_centrality))
        btn_centrality = betweenness_centrality(G)
        data.extend(properties_of_array(btn_centrality))
        st_path = shortest_path(G)
        deg = [len(val) for key, val in st_path.items()]
        d = np.array(deg)
        data.extend([np.min(d), np.max(d), np.median(d), np.mean(d), np.std(d)])
        try:
            data.append(diameter(G.to_undirected()))
        except:
            data.append(0)
        try:
            data.append(radius(G.to_undirected()))
        except:
            data.append(0)
        csvwriter.writerow(data)
    csvfile.close()

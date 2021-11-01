import pandas as pd
import numpy as np


# This function for identifing childs' nodes
def links(data, station):
    link_ls = []
    i = 0
    # Check non zeros nodes of an station _neighbours_ and adding (cost, name) to a list
    control = data[data[station[1]] != 0]
    nodes = control.index.values
    for i in range(len(nodes)):
        tup = (data[station[1]][nodes[i]], nodes[i])
        link_ls.append(tup)
        i += 1
    return link_ls


# DFS Algorithm
def dfs(data, start, target):
    path = []
    fringe = []
    station = (0, start)
    path.append(station)
    # While find goal
    while station[1] != target:
        # Extend the node and find its connections
        link = links(data, station)
        for lk in link:
            # Was the node extended? If not, append it to STACK
            if not any(p[1] == lk[1] for p in path):
                fringe.append(lk)
        # Remove a node from STACK
        station = fringe.pop(-1)
        if not any(pth[1] == station[1] for pth in path):
            path.append(station)
    return path


def path_cost(path):
    cost = 0
    for sts in path:
        cost += sts[0]
    return cost

def path_list(path):
    path_lis = []
    for pth in path:
        path_lis.append(pth[1])
    return path_lis


def travel_path(path, begin):
    travel_lis = []
    station = path.pop(-1)
    travel_lis.append(station)
    while station[1] != begin:
        # Find links of station
        link = links(data, station)
        for lk in link:
            # IF links are in the end of path THEN append to travel_path
            if lk[1] == path[-1][1]:
                travel_lis.append(lk)
        # Check last station of path
        path.pop(-1)
        station = travel_lis[-1]
    travel_lis.reverse()
    return travel_lis


data = pd.read_csv('metro_stations_sparse_matrix_distoriented.csv')
# Preparing Data Frame
data = data.fillna(0)
data = data.iloc[:, 1:]
label = data.columns
data.index = label

begin = input("Please enter your beginning: ")
end = input("Please enter your destination: ")
path = dfs(data, begin, end)
show_path = path_list(path)
cost = path_cost(path)
travel_path = travel_path(path, begin)
cost_travel_path = path_cost(travel_path)
print("DFS:", show_path)
print("DFS COST:", cost)
print("TRAVEL PATH:", path_list(travel_path))
print("TRAVEL COST:", cost_travel_path)

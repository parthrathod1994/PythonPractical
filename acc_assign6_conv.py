from collections import defaultdict
import math
import random

def updatepath(node):
    randomvalue = random.randint(0,3)
    #print(node,"to other node:",randomvalue)
    for i in range(0,n):
        distance[node][i] = distance[node][i] + randomvalue

def mainbruteforce(graph,u, d, visited, path):
    # Mark the current node as visited and store in path
    visited[u] = True
    path.append(u)
    updatepath(u)

    if u == d:
        sumv = 0
        for i in range(len(path)-1):
            sumv = sumv + distance[path[i]][path[i+1]]

        no_path.append([])
        index = len(no_path)-1
        for i in path:
            no_path[index].append(i)

        path_cost.append(sumv)

    else:
        # If current vertex is not destination
        # Recur for all the vertices adjacent to this vertex
        for i in graph[u]:
            if visited[i] == False:
                mainbruteforce(graph,i, d, visited, path)

    path.pop()
    visited[u] = False

def bruteforce(distance,n,src,dest):

    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if distance[i][j] != math.inf:
                graph[i].append(j)

    visited = [False] * (n)

    path = []

    # Call the recursive helper function to print all paths
    mainbruteforce(graph,src, dest, visited, path)

    print("Best path=",no_path[path_cost.index(min(path_cost))])

    print("Value of path=",min(path_cost))

no_path = []
path_cost = []

#start the program
n = 9

#adjacency matrix
distance = [[math.inf, 4, math.inf, math.inf, math.inf, math.inf, math.inf, 8, math.inf],
            [4, math.inf, 8, math.inf, math.inf, math.inf, math.inf, 11, math.inf],
            [math.inf, 8, math.inf, 7, math.inf, 4, math.inf, math.inf, 2],
            [math.inf, math.inf, 7, math.inf, 9, 14, math.inf, math.inf, math.inf],
            [math.inf, math.inf, math.inf, 9, math.inf, 10, math.inf, math.inf, math.inf],
            [math.inf, math.inf, 4, 14, 10, math.inf, 2, math.inf, math.inf],
            [math.inf, math.inf, math.inf, math.inf, math.inf, 2, math.inf, 1, 6],
            [8, 11, math.inf, math.inf, math.inf, math.inf, 1, math.inf, 7],
            [math.inf, math.inf, 2, math.inf, math.inf, math.inf, 6, 7, math.inf]]

src = int(input("input Source node:"))
dest = int(input("input Destination node:"))

bruteforce(distance,n,src,dest)

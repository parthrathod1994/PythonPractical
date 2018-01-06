import math
import random
flag_array = []

def updatepath(node):
    randomvalue = random.randint(0,3)
    #print(node,"to other node:",randomvalue)
    for i in range(0,n):
        distance[node][i] = distance[node][i] + randomvalue

def minDistance(dist,flag_array,n):
    min_value = math.inf
    for i in range(0,n):
        if dist[i] < min_value and flag_array[i] == False:
            min_value = dist[i]
            min_index = i
    return min_index

def shortest_path(graph, src,n):
    dist = [math.inf] * n
    flag_array = [False] * n
    dist[src] = 0

    for cout in range(n):
        #find the node index that have min cost
        u = minDistance(dist,flag_array,n)
        flag_array[u] = True
        updatepath(u)
        for i in range(n):
            if graph[u][i] > 0 and flag_array[i]==False and dist[i] > dist[u] + graph[u][i]:
                dist[i] = dist[u] + graph[u][i]
                path[i] = u
    return dist

#start the program
n=9

#adjacency matrix
distance = [[math.inf, 2, math.inf, math.inf, math.inf, math.inf, math.inf, 8, math.inf],
            [math.inf, math.inf, 8, math.inf, math.inf, math.inf, math.inf, 11, math.inf],
            [math.inf, math.inf, math.inf, 7, math.inf, 1, math.inf, math.inf, 2],
            [math.inf, math.inf, math.inf, math.inf, 9, math.inf, math.inf, math.inf, math.inf],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
            [math.inf, math.inf, math.inf, 14, 10, math.inf, math.inf, math.inf, math.inf],
            [math.inf, math.inf, math.inf, math.inf, math.inf, 2, math.inf, math.inf, math.inf],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 1, math.inf, 7],
            [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 6, math.inf, math.inf]]


src = int(input("input Source node:"))
dest = int(input("input Destination node:"))

path = [-1] * n
dist = shortest_path(distance,src,n)

#answer
print("from node",src,"to",dest,"time taken is=",dist[dest])

def printPath(path,j):
    if (path[j] == -1):
        print(j,end=" ")
        return
    printPath(path, path[j])
    print(j,end=" ")

print("Path=",end="")
printPath(path,dest)
#printSolution(dist,path)

print("Path=",path)
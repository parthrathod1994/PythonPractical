# for i in range(0,n):
#     distance.append([])
#     for j in range(0,n):
#         distance[i].append(math.inf)
#
#
# for i in range(0,n):
#     print("node connect with",i,":",end="")
#     n1=int(input())
#     for j in range(0,n1):
#         print(i,"to j=",end="")
#         temp = int(input())
#         if distance[temp][i]!=math.inf:
#             distance[i][temp]=distance[temp][i]
#         else:
#             print("=",end="")
#             distance[i][temp]=int(input())

# for i in range(0,n):
#     distance.append([])
#
#     for j in range(0,n):
#         if i == j:
#             distance[i].append(0)
#         else:
#             print(i,"to",j,"=",end="")
#             distance[i].append(int(input()))

def found_list(data):
    for i in final_list:
        if data == i:
            return 0
    return 1

#Print Distance from source node
def printSolution(dist,n):
    print("Vertex tDistance from Source")
    for node in range(n):
        print(node, "t", dist[node])
from itertools import permutations

conn = [[0,2,3],[2,0,4],[3,4,0]]
dist = [[0,2,1],[2,0,3],[1,3,0]]
f = [0,1,2]
temp=30000

print("Connection Between Components : ")
for i in range(0,3):
    for j in range(0,3):
        print(conn[i][j],end=" ")
    print("")

print("Distance Between Components : ")
for i in range(0,3):
    for j in range(0,3):
        print(dist[i][j],end=" ")
    print("")

permutelist = list(permutations(range(0,3)))

print("all permutation=",permutelist)

cost = 0
newCost = 5000
for l in permutelist:
    cost = (conn[l[0]][l[1]] * dist[l[0]][l[1]])
    if newCost > cost:
        cost = cost + (conn[l[1]][l[2]] * dist[l[1]][l[2]])
        minlist = l
        print("Value=",cost)
        if newCost >cost:
            newCost = cost

print("min cost=",newCost)
print("min list=",minlist)

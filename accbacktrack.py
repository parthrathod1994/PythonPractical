from itertools import permutations

newCost = 5000

def combination(a,b,cost,seq,flag):
    tempCost = 3200
    f=0
    for j in range(seq+1,3):
        f = 1

        #suffle
        temp = flag[seq + 1]
        flag[seq + 1] = flag[j]
        flag[j] = temp

        newCost = cost + (a[flag[seq + 1]][flag[seq]] * b[flag[seq + 1]][flag[seq]])

        temp = combination(a, b, newCost, seq + 1, flag)

        print("Till_now :",newCost,"::: Further_Cost =", temp - newCost)

        if temp < tempCost:
            tempCost = temp

        temp=flag[seq+1]
        flag[seq+1]=flag[j]
        flag[j]=temp

    if f == 0:
        return cost
    else:
        return tempCost

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

print("all permutation=",list(permutations(range(0,3))))

for j in range(0,3):
    i = f[0]
    f[0]= f[j]
    f[j]= i
    minCost = combination(conn,dist,0,0,f)

    if minCost < temp:
        temp = minCost

    i = f[0]
    f[0]= f[j]
    f[j]= i
    print("Minimum Cost :",temp)
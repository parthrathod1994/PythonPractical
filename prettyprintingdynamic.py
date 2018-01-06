import math
def cost(list_word,i,j):
    sum = 0
    for k in range(i,j):
        sum = sum + len(list_word[k])
    return  sum

def dynamic(list_word,length):
    n=len(list_word)
    cost_mat = []
    min_cost = []
    result = []

    for i in range(0,n):
        cost_mat.append([])
        min_cost.append(0)
        result.append(0)
        for j in range(0,n):
            cost_mat[i].append(0)

    for i in range(0,n):
        cost_mat[i][i] = pow((length - len(list_word[i])),2)
        for j in range(i+1,n):
            len_word = cost(list_word,i,j+1) + j - i
            if len_word <= length:
                cost_mat[i][j] = pow(length - len_word,2)
            else:
                cost_mat[i][j] = math.inf

    for i in range(n-1,-1,-1):
        min_cost[i] = cost_mat[i][n - 1]
        result[i] = n
        for j in range(n-1,i,-1):
            if cost_mat[i][j-1] == math.inf:
                continue
            if min_cost[i] > min_cost[j] + cost_mat[i][j - 1]:
                min_cost[i] = min_cost[j] + cost_mat[i][j - 1]
                result[i] = j

    for i in range(0,n):
        for j in range(0,n):
                print(cost_mat[i][j]," ",end="")
        print("\n")

    print("Result matrix=", result)
    print("Min matrix=", min_cost)
    print("Cost=",min_cost[0])

    file2 = open("wraptext.txt", "wt")

    i = 0;
    j = 0;
    while j < len(list_word):
        j = result[i]
        str1 = ""
        for k in range(i, j):
            str1 = str1 + " " + str(list_word[k])
        print(str1)
        #file2.write(str1 + '\n')
        i = j

print("Eneter The Length to Wrap:")
length = int(input())

file1 = open("plaintext.txt","r")
file1_data = file1.read()
data_len = len(file1_data)

split_data = file1_data.split(" ")

print("No Of Word=",len(split_data))

cost(split_data,0,2)

final_data = dynamic(split_data,length)
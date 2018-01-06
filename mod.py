k=0
for i in range(2,98):
    for j in range(2,98):
        if i != pow(i,j,97):
            k = k + 1
        else:
            if k == 95:
                print(i)
                k=0
            else:
                k=0
                break
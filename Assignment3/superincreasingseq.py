w = [2,7,8,21,42,89,180,354]

flag = 0

sum = w[0]
for i in w[1:]:
    if sum > i:
        flag = 1
    sum = sum + i

if flag == 0:
    print("entered value is super increasing seq")
else:
    print("entered value is not a super increasing seq")
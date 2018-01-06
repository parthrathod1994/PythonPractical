#application of the fermat theoram: primality testing
#https://en.wikipedia.org/wiki/Fermat_primality_test

import random as randm
z = int(input("Enter no:"))

flag = 0

for i in range(0,2):
    a = randm.randint(2,z-1)
    data = pow(a,z-1)
    if data%z != 1:
        flag = 1
        break

if flag==0:
    print("Its a prime no")
else:
    print("Not a prime no")

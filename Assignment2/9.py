import Assignment2 as assign
from fractions import gcd

def findgenerator(z):
    generator = []

    phi = int(assign.eulerfunction(z))

    nophi = int(assign.eulerfunction(phi))

    #if a is a generator of Zn*, then Zn*={a^i mod n |0≤ i ≤Φ(n)-1}
    for i in range(1,z):
        temp = pow(i,phi) % z
        for j in range(2,phi):
            temp1 = pow(i, j) % z
            if temp1 != temp:
                if j == phi-1:
                  generator.append(i)
            else:
                break
    if len(generator) == nophi:
        print("Z*",z,"is cyclic group and its generator are:")
        print(generator)
        #b=a^i mod z is also a generator where gcd(i,phi)=1
        print("Property:")
        for j in generator[0]:
            for i in (1,z):
                print(pow(j,i),end=" ")
    else:
        print("its not a cyclic group")

flag = 1
while flag == 1:
    z = int(input("Enter the z Value:"))
    findgenerator(z)
    flag = int(input("enter 1 to continue:"))

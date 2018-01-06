import Assignment2 as assign

def findgenerator(z):
    generator = []

    phi = int(assign.eulerfunction(z))

    nophi = int(assign.eulerfunction(phi))

    k=1
    for i in range(1,z):
        temp = pow(i,1)%z
        for j in range(2,z):
            temp1 = pow(i, j) % z
            if temp1 == 1:
                if j == phi:
                  generator.append(i)
                break

    if(len(generator) == nophi):
        for i in generator:
            print(i,end=" ")
        print("\nZ*",z,"is a Cyclic Group")
    else:
        print("Not a Cyclic Group")

flag = 1
while flag == 1:
    z = int(input("Enter the z Value:"))
    findgenerator(z)
    flag = int(input("enter 1 to continue:"))

#25,27,49,81 is a cyclic group
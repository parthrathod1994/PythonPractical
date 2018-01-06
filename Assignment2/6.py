import sympy as sp
z = int(input("enter z value:"))

if sp.isprime(z):
    k=0
    for i in range(1,z):
        for j in range(1,z):
            if i*j%z == 1:
                print(i,"inverse=",j)
                k+=1

    if k == z-1:
        print("Its a GF and its order is:",k+1)
    else:
        print("Its not a GF and its order is:",k+1)
else:
    print("Please enter prime no")
import sympy as sp

def primefactor(n):
    flag=0
    i=1
    prime_ar = []
    while n>1:
        if n%sp.prime(i)==0:
            prime_ar.append(sp.prime(i))
            #print("Fact",sp.prime(i))
            n=n/sp.prime(i)
        else:
            i+=1

    k=prime_ar[0]
    for i in prime_ar[1:]:
        if k != i:
            return 0
        k=i

    return 1

flag = 1
while flag == 1:
    z = int(input("Enter the z Value:"))
    if primefactor(z) == 1:
        print("is a cyclic group")
    else:
        print("not a cyclic group")
    flag = int(input("enter 1 to continue:"))
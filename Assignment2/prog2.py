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

z = int(input("enter z value:"))

flag = primefactor(z)

if flag == 1:
    k=0
    for i in range(1,z):
        for j in range(1,z):
            if i*j%z == 1:
                print(i,"inverse=",j)
                k+=1

    print("Its a GF and its order is:",k)
else:
    print("Its not a GF")
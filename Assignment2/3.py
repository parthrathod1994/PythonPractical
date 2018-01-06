import sympy as sp
distinct = []

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

    k=0
    for i in prime_ar:
        if k!=i:
            k=i
            distinct.append(i)
            print(i)



x=int(input("Enter No:"))
primefactor(x)
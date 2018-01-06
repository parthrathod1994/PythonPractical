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
        else:
            flag=1
    return flag

def eulerfunction(n):
    if sp.isprime(n)==1:
        return n-1
    else:
        flag = primefactor(n)
        if flag == 1:
            output = n
            for i in distinct:
                output = int(output * (1-(1/i)))

            distinct.clear()
            return output
        else:
            output = 1
            for i in distinct:
                output = output * (i-1)

            distinct.clear()
            return output
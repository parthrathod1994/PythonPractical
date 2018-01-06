import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    inv = e
    gf = phi
    q = 0
    a1 = 1
    a2 = 0
    a3 = gf
    b1 = 0
    b2 = 1
    b3 = inv
    while b3 > 1:
        q = int(a3 / b3)
        t1 = a1 - (q * b1)
        t2 = a2 - (q * b2)
        t3 = a3 - (q * b3)
        a1 = b1
        a2 = b2
        a3 = b3
        b1 = t1
        b2 = t2
        b3 = t3

    if b2 < 0:
        b2 = b2 % gf
        return b2
    else:
        return b2

w = [2,7,11,21,42,89,180,354]
sum = 0
for i in w:
    sum = sum + i

print("sum=",sum)

q = random.randrange(sum +1 , sum + 100)
#q=881

r = random.randrange(1, sum)
#r = 588
g = gcd(r,q)
while g != 1:
    r = random.randrange(1, sum)
    g = gcd(r, q)

print("r=",r,"q=",q)

B = []

for i in w:
    B.append((i*r)%q)

print("Public key=",B)

word = input("input what you encrypt:")
k = 0
datasum = []

for i in word:
    word_bit = format(ord(i),"08b")
    datasum.append(0)
    for j in range(0,8):
        datasum[k] = datasum[k] + (int(word_bit[j])*B[j])
    #datasum[k] = datasum[k]%q
    print(word_bit," ",ord(i)," ",datasum[k])
    k+=1

r_inverse = multiplicative_inverse(r,q)
print("inverse=",r_inverse)
plaintext = []
for i in datasum:
    plaintext.append((i*r_inverse)%q)
binplaintext = []

print("plaintext=",plaintext)
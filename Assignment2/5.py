inv = int(input("inverse no="))
gf = int(input("GF(no)="))
q=0
a1=1
a2=0
a3=gf
b1=0
b2=1
b3=inv
print("a1 ","a2 ", "a3 ","b1 ","b2 ","b3 ")
print(a1," ",a2," ",a3," ",b1," ",b2," ",b3)
while b3 > 1:
    q=int(a3/b3)
    t1 = a1 - (q * b1)
    t2 = a2 - (q * b2)
    t3 = a3 - (q * b3)
    a1 = b1
    a2 = b2
    a3 = b3
    b1 = t1
    b2 = t2
    b3 = t3
    print(a1, " ", a2, " ", a3, " ", b1, " ", b2, " ", b3)

if b2 < 0:
    b2 = b2 % gf
    print("Inverse Of No=", b2)
else:
    print("Inverse Of No=",b2)
a=0
x=0
n=8
while a<1000 and x<100 and n<2048:
    print("Enter Value Of a=",end="")
    a=int(input())
    print("Enter Value Of x=",end="")
    x=int(input())
    print("Enter Value Of n=",end="")
    n=int(input())

output = pow(a,x)%n
print("output=",output)
z = int(input("Enter Z Value:"))

def finddistict(n,array):
    for i in array:
        if i==n:
            return 0
    return 1

array = []
arraybar = []

for i in range(1,z):
    k = (i*i) % z
    if finddistict(k,array) == 1 and k != 0:
        array.append(k)

array.sort()

for i in range(1,z):
    if finddistict(i,array):
        arraybar.append(i)

print("Q:",end="")
for i in array:
    print(i,end=" ")

print("\nQ Bar:",end="")
for i in arraybar:
    print(i,end=" ")
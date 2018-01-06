import time
ne = int(input())
a = []
inv = 0;
for i in range(0, ne):
    a.append(ne-i)

start = time.clock();
for i in range(0, ne):
    for j in range(0,ne):
        if i < j and a[i] > a[j]:
            inv += 1

stop = time.clock();
current_microsec_time = int(round((stop - start) * 1000000))
print("time=", current_microsec_time)
print("No Of Inversion=", inv)
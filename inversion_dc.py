import time
inv = 0

def combine(newlist, st, mid, lt):
    global inv
    alength = (mid - st) + 1
    blength = lt - mid
    alist = newlist[st:mid+1]
    blist = newlist[mid+1:lt+1]
    for i in range(0,alength):
        for j in range(0,blength):
            if(alist[i]>blist[j]):
                inv += 1

#function
def devide_Conqure(newlist, st, lt):
    if st < lt:
        mid = int(st + ((lt-st)/2))
        devide_Conqure(newlist, st, mid)
        devide_Conqure(newlist, mid+1, lt)
        combine(newlist, st, mid, lt)

ne = int(input())
a = []
inv = 0;
for i in range(0, ne):
    a.append(ne-i)

start = time.clock();

devide_Conqure(a, 0, ne-1)

stop = time.clock();
current_microsec_time = int(round((stop - start) * 1000000))
print("time=", current_microsec_time)
print("No Of Inversion=", inv)
import time
a = int(input())
b = int(input())
ans = 1
start = time.clock()

while True:
    q = int(b/2)
    r = int(b % 2)
    if r == 1:
        ans = ans*a
    if q == 0:
        break
    b = q;
    a = a*a;

stop = time.clock()
current_microsec_time = int(round((stop - start) * 1000000))
print(current_microsec_time)
print(ans)


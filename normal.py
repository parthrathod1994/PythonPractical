import time
a = int(input())
b = int(input())
ans = 1
start = time.clock()
for i in range(0, b):
    ans = ans * a

stop = time.clock()
current_microsec_time = int(round((stop - start) * 1000000))
print(current_microsec_time)
print(ans)
import sys

n, m  = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))


prefix_list = [0]
sum = 0
for v in num_list:
    sum += v
    prefix_list.append(sum)



query_list = []
for i in range(m):
    x = list(map(int, sys.stdin.readline().split()))
    query_list.append(x)

for q in query_list:
    start = q[0] -1
    finish = q[1]

    if start <0 :
        start = 0

    print(prefix_list[finish] - prefix_list[start])











# n = int(input())
# lst = []
# for i in range(n):
#     t = int(input())
#     lst.append(t)

# tl = []
# result = 0

# min = 999999999
# for i in range(n-1):
#     tl.append(lst[i+1]-lst[i])
#     if lst[i+1]-lst[i] <= min:
#         min = lst[i+1]-lst[i]
        
# flag = 0

# for i in range(len(tl)-1):
#     if tl[i] != tl[i+1]:
#         flag = 1
#         break
# if flag == 0:
#     print(0)
# else:


#     if min != 1:
#         for i in range(2, min+1):
#             if min % i == 0:
#                 min = i
#                 break

#     for i in range(n-1):
#         if lst[i+1]-lst[i] != min:
#             result += (((lst[i+1]-lst[i]) // min) - 1)

#     print(result)

from math import gcd
n = int(input())
lst = []
for i in range(n):
    t = int(input())
    lst.append(t)

temp_lst = []
for i in range(n-1):
    temp_lst.append(lst[i+1]-lst[i])
temp_lst_ = []
for i in range(n-2):
    temp_lst_.append(gcd(temp_lst[i], temp_lst[i+1]))
d = min(temp_lst_)
count = 0
# for i in range(min(lst), max(lst)+1, d):
#     count += 1
count = (max(lst)-min(lst)) // d + 1

print(count-len(lst))
# 거의 99프로까지 가서 실패
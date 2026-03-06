# def solve():
#     num = int(input())
#     iter_num = int(input())
#     lists = []
#     varius = [1]

#     for i in range(iter_num):
#         lst = list(map(int, input().split()))
#         lists.append(lst)

#     for lst in lists:
#         if (lst[0] in varius) or (lst[1] in varius):
#             varius.append(lst[0])
#             varius.append(lst[1])

#     result = set(varius)
#     print(result)
#     print(len(result)-1)

# 이 방식은 순서를 고려해버려서 틀림. 리스트를 차례대로 한번씩 검사해서 바이러스감염 여부를 판단해버리니 순서가 바뀌면 대응 못함. 


def solve():
    num = int(input())
    iter_num = int(input())
    lists = []
    varius = [1]

    for i in range(iter_num):
        lst = list(map(int, input().split()))
        lists.append(lst)
    
    graph = {i: [] for i in range(1, num + 1)} # 크기가 num인 딕셔너리 선언 방법

    for lst in lists:
        graph[lst[0]].append(lst[1])
        graph[lst[1]].append(lst[0])
    
    def temp(i):
         


    for i in range(1, num+1):
        if i in varius:
            for j in graph[i]:
                varius.append(j)
    
    
    print(set(varius))
    print(graph)
    print(len(set(varius))-1)

solve()
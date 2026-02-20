# setAnum, setBnum = map(int, input().split())
# setA = list(map(int, input().split()))
# setB = list(map(int, input().split()))

# notsetA = []
# notsetB = []

# for i in range(len(setA)):
#     if setA[i] not in setB:
#         notsetB.append(setA[i])

# for i in range(len(setB)):
#     if setB[i] not in setA:
#         notsetA.append(setB[i])


# print(len(set(notsetA+notsetB)))
# 시간 초과 실패

setAnum, setBnum = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

notsetA = setA - setB
notsetB = setB - setA

print(len(notsetA | notsetB))
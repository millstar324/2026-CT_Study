#start : 10:34
#end: 11:26
#2차원 배열 만들기 [[]]*n 안됨

import sys

def solve():
    n = int(sys.stdin.readline())
    arr = [ [None] for _ in range(51)]
    # print(arr)
    for i in range(n):
        word = sys.stdin.readline().strip()
        word_len = len(word)
        # print(word_len)
        # print(f"arr[word_len]:{arr[word_len]}")
        
        if arr[word_len][0] == None:
            arr[word_len].append(word)
            arr[word_len].remove(None)
            # print(arr)
            # print(f"프린트한것if:{arr[word_len]}")
        else:
            if  word in arr[word_len]:
                pass
            else: 
                arr[word_len].append(word)
                # print(f"프린트한것:{arr[word_len]}")
                arr[word_len].sort()
    


    for i in arr:
        if i[0] != None:
            for j in i:
                print(j)

solve()


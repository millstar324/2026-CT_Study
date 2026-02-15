check_q = []
check_ans = []

r_arr=[0]*5
r_count=0

def check_f(arr):
    # print("arr:",arr)
    
    
    for i,v_l in enumerate(check_q):
        count = 0
        for j in v_l:
            if j in arr:
                count+=1
        if count != check_ans[i]:
            # print("out")
            return 0
    global r_count
    r_count +=1
    return 0

def recursion_f(index, n=0):
    if index == 4:
        # print("index=4")
        for i in range(n, 4, -1):
            r_arr[index]  = i
            # print(f"r_arr:{r_arr}")
            recursion_f(3)
        
    elif index == 0:
        # print(f"index={index}")
        for i in range(r_arr[index+1]-1,0,-1):
            r_arr[0] = i
            check_f(r_arr)
        
        return 0
        
    else :
        # print(f"index={index}")
        for i in range(r_arr[index+1]-1,index,-1):
            r_arr[index] = i
            # print(f"r_arr:{r_arr}")
            recursion_f(index-1)

def solution(n, q, ans): 
    
    check_q.extend(q)
    check_ans.extend(ans)
    recursion_f(4, n)
    global r_count
    return r_count


"""
import itertools 

def solution(n, q, ans):
    f = list(itertools.combinations(range(1, n + 1), 5))

    for g, cnt in zip(q, ans):
         f = [code for code in f if len(set(code) & set(g)) == cnt]

    return len(f)"""
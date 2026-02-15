def solution(number, limit, power):
    arr = []
    for i in range(number):
        count=0
        num = i+1
        for j in range(1,int(num**(1/2))+1):
            if float(num) / float(j) == float(j):
                count+=1
            elif num % j ==0:
                count+=2
            
                
            
        arr.append(count)
    # print(arr)
    answer=0
    for i in arr:
        if i > limit:
            answer+= power
        else:
            answer+=i
        
    
    return answer



# def cf(n): # 공약수 출력
#     a = []
#     for i in range(1,int(n**0.5)+1):
#         if n%i == 0:
#             a.append(n//i)
#             a.append(i)
#     return len(set(a))
# def solution(number, limit, power):
#     return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])
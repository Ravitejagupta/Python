def solution(A):
    for i in range(len(A)):
        if A[i] in A[i+1:]:
            pass
        else:
            start = i
            break
    if i == len(A)-1:
        return 1
    
        
    for i in range(len(A)-1,1,-1):
        print(A[start:i])
        if A[i] in A[start:i]:
          print("Yes")  
          pass
        else:   
            end  = i
            break
    print(end,start)
    return  (end - start + 1)
    
print(solution([1,2]))

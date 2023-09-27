def solution(A):
    max_no = A[0]  
    min_no = A[0]  

    for num in A:
        if num > max_no:
            max_no = num
        elif num < min_no:
            min_no = num
    
    return max_no - min_no


A = [70, 24, 44, 15, 39, 20]
print(solution(A))  

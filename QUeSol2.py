def Solution(A):

    A.sort()

    return A[-1] - A[0] 

A = [10, 2, 44, 15, 39, 20]
print(solution(A)) 
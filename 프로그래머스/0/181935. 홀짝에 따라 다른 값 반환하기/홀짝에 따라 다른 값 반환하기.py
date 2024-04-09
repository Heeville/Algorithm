def solution(n):
    if n%2==1:
        answer = sum([i for i in range(n+1) if i%2==1])
    else:
        answer=sum([i*i for i in range(n+1) if i%2==0])
    return answer
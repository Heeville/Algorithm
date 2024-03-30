def solution(names):
    answer = []
    for i,val in enumerate(names):
        if i%5==0:
            answer.append(val)
    return answer
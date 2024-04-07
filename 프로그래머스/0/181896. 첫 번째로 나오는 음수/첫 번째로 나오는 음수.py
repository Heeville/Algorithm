def solution(num_list):
    answer = -1
    for k,v in enumerate(num_list):
        if v<0:
            answer=k
            break
    return answer
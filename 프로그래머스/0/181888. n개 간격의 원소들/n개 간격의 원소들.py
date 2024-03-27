def solution(num_list, n):
    answer = []
    answer.append(num_list[0])
    for i in range(1,len(num_list)):
        if i%n==0:
            answer.append(num_list[i])
        
    return answer
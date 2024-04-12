def solution(arr, delete_list):
    sss=arr.copy()
    for i in sss:
        if i in delete_list:
            arr.remove(i)
    
    return arr
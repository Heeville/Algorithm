def solution(s):
    strr=["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in strr:
        if i in s:
            s=s.replace(i,str(strr.index(i)))
    
    
    return int(s)
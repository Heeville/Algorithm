from math import *

def solution(number, n, m):
    nu=n*m//gcd(n,m)
    answer = 0
    if number%nu==0:
        answer=1
    return answer
from collections import *
from itertools import *
from copy import *

#바이러스 확산과정 -> bfs ㄱㄱ
def sambfs(li,start):
    row=len(li)
    col=len(li[0])
    #print(start)
    visited=[[False]*col for _ in range(row)]
    directions=[[-1,0],[1,0],[0,-1],[0,1]] #방향 - 상하좌우
    visited[start[0]][start[1]]=True
    qq=deque()
    qq.append(start)
    while qq:
        curr,curc=qq.popleft()
        for i in range(4):
            tempr=curr+directions[i][0]
            tempc=curc+directions[i][1]
            if 0<=tempr < row and 0<=tempc<col and visited[tempr][tempc]==False:
                if li[tempr][tempc]==0:
                    qq.append((tempr,tempc))
                    visited[tempr][tempc]=True
                    li[tempr][tempc]=2

    return li


N,M=map(int,input().split()) #N은 가로, M은 세로
lili=[]
for _ in range(N):
    lili.append(list(map(int,input().split())))
#0: 빈칸, 1: 벽, 2: 바이러스
#세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
safe=[] #안전영역갯수 리스트 -> 모든경우 탐색할 예정

wall=deque()
#0. 벽 세울 수 있는 공간 찾기
for i in range(N):
    for q in range(M):
        if lili[i][q]==0:
            wall.append((i,q))

#1. 벽 세워놓기 단계
for t in combinations(wall,3):
    w1,w2,w3=t
    #print(w1,w2,w3)
    templi = deepcopy(lili)
    templi[w1[0]][w1[1]]=1
    templi[w2[0]][w2[1]]=1
    templi[w3[0]][w3[1]]=1

    #2.바이러스 확산 단계
    for i in range(N):
        for q in range(M):
            if lili[i][q]==2:
                templi=sambfs(templi, (i, q))

    #3. 안전지대 탐색 단계
    tempsafe=0
    for i in range(N):
        for w in range(M):
            if templi[i][w]==0:
               # print(i,w)
                tempsafe+=1

    #4. 해당 케이스의 안전지대
    safe.append(tempsafe)
print(max(safe))

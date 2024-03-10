from collections import *

def bfs(maps,start):
    que=deque()
    maxrow=len(maps)
    maxcol=len(maps[0])
    visited=[[False]*maxcol for _ in range(maxrow)]
    visited[0][0]=True
    
    if maps[maxrow-1][maxcol-2]==0 and maps[maxrow-2][maxcol-1]==0:
        return -1
    
    que.append(start)
    directions=[(0,1),(0,-1),(1,0),(-1,0)]  #동,서,남,북
    longest=-1
    
    while que:
        curr,curc,curstat=que.popleft()
        if curr==maxrow-1 and curc==maxcol-1:
            longest=curstat
            break
        code=0
        for i,j in directions:
            tempr=curr+i
            tempc=curc+j
            if (tempr>=0 and tempr<maxrow) and (tempc>=0 and tempc<maxcol):
                if maps[tempr][tempc]==1 and visited[tempr][tempc]==False:
                    #print(tempr,tempc)
                    que.append((tempr,tempc,curstat+1))
                    visited[tempr][tempc]=True
                    code=1
                
    return longest
                    

def solution(maps):
    answer=bfs(maps,(0,0,1))
    return answer
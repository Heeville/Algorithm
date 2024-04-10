## 백준: 뱀
from collections import *

N=int(input()) #격자 크기
K=int(input()) #사과 갯수

Bam=[[0]*N for _ in range(N)]  #뱀 이동경로
lili=[] #방향 전환 시간,정보
dir=[[-1,0],[0,1],[1,0],[0,-1]] #방향, 상우하좌

for i in range(K):
    r,c=map(int,input().split())
    Bam[r-1][c-1]=1

D=int(input()) #뱀의 방향 전환 횟수
for i in range(D):
    #게임 시작 시간으로부터 x초가 끝난 뒤에 왼쪽 or 오른쪽 90방향 회전 -> direction
    x,ST=map(str,input().split())
    lili.append((int(x),ST))

dirtime=[]
for i in range(len(lili)):
    if i==0:
        dirtime.append(lili[i][0])
    else:
        dirtime.append(lili[i][0]-lili[i-1][0])

dirtime.append(N)

qqq=deque() #뱀 몸 있는 위치
def pan(r,c):
    return 0<=r<N and 0<=c<N and (Bam[r][c]==0 or Bam[r][c]==1)

def bamiter(idx,ddx,curr,curc,gcount):
    for i in range(dirtime[idx]):
        tempr=curr+dir[ddx][0]
        tempc=curc+dir[ddx][1]
        gcount += 1
        if not pan(tempr,tempc):
            return gcount,curr,curc,-1
        if Bam[tempr][tempc]==1: #사과를 만났을때
            qqq.append((tempr,tempc))
            Bam[tempr][tempc] =0

        else:
            remover,removec=qqq.popleft()
            qqq.append((tempr,tempc))
            Bam[remover][removec]=0 #꼬리 부분 지움
        curr,curc=tempr,tempc

    for k in range(len(qqq)):
        if k==0:
            Bam[qqq[k][0]][qqq[k][1]]=3
        else:
            Bam[qqq[k][0]][qqq[k][1]] = 2

    return gcount,curr,curc,0

def returning(idx,ddx):
    # 방향 전환 단계
    if lili[idx][1] == 'D':  # 오른쪽,시계방향
        ddx += 1
        if ddx > 3:
            ddx = 0
    elif lili[idx][1] == 'L':
        ddx -= 1
        if ddx < 0:
            ddx = 3
    idx += 1
    if idx==len(lili)+1:
        return -1,ddx
    return idx,ddx

#사과:1, 뱀 몸:2, 뱀 꼬리: 3 아무것도 없음: 0
flag=True
while(flag):
    #초기 단계
    curr,curc=0,0
    Bam[curr][curc]=3
    idx =0 # 방향 전환 시간 인덱스
    ddx=1 #방향 전환 방향 인덱스
    gcount=0
    qqq.append((curr,curc))
    for i in range(len(lili)+1):
        gcount2,turr,turc,fig=bamiter(idx, ddx, curr, curc,gcount)
        if fig==-1:
            flag=False
            gcount =gcount2
            print(gcount)
            break
        gcount=gcount2
        idx,ddx=returning(idx,ddx)
        if idx==-1:
            print(gcount)
            flag=False
            break
        curr,curc=turr,turc

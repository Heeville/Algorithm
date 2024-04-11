from collections import *

R,C,T=map(int,input().split())
lili=[]
for _ in range(R):
    lili.append(list(map(int,input().split())))

directions=[[0,1],[0,-1],[1,0],[-1,0]] #방향계수 우 0 ,좌 1, 하 2,상 3

#복사본을 만들어서 대체를 할까?
deq=deque() # 업데이트 할 데큐 (행,열,업데이트 값)

for i in range(T):
    #1-1: 미세먼지 찾기
    for row in range(len(lili)):
        for col in range(len(lili[0])):
            if lili[row][col]>0:  #미세먼지가 있을 때,  동시에 확산!!!!
                for e in range(4): #방향
                    temprow=row+directions[e][0]
                    tempcol=col+directions[e][1]
                    if 0<=temprow<R and 0<=tempcol<C and lili[temprow][tempcol]!=-1:
                        deq.append((temprow,tempcol,int(lili[row][col]/5))) #해당 위치에 미세먼지 확산
                        deq.append((row,col,-(int(lili[row][col]/5)))) #원래위치 미세먼지 양 업데이트
    #1-2: 미세먼지 업데이트
    for q in range(len(deq)):
        qr,ql,qu=deq.popleft()
        lili[qr][ql]+=qu

    recir=[]
    cir=[]
    rq = deque() #반시계 꼭짓점들 (넣을 행, 넣을 열, 꼭짓점 값)
    cq=deque() # 시계 꼭짓점들
    recirt=0 #반시계 공기 청정기 위치
    cirt=0 #시계 공기 청정기 위치
    #2-1: 공기청정기 작동 범위 나누기(시계,반시계)
    for w in range(len(lili)):
        if lili[w][0]==-1:
            recir=lili[:w+1][:]
            rq.append((w,len(recir[0])-1,3,recir[w][len(recir[0])-1]))  #오른쪽 아래 꼭짓점 추가 (행,열,상,꼭짓점 값)
            recirt=w
            cirt=w+1
            cir=lili[w+1:][:]
            cq.append((0,len(cir[0])-1,2,cir[0][len(cir[0])-1])) #오른쪽 위 꼭짓점 추가(
            break

    #print(recir,rq[0])
    #print(cir,cq[0])

    for r in range(len(recir)):
        if recir[r][0]==-1:
           # rq.append((r-1,len(recir[0])-1,lili[r][-1])) #오른쪽 아래 꼭짓점 추가
            recir[r][2:]=recir[r][1:-1] #바람 이동 -> 오른쪽으로 한 칸씩 옮기기
            recir[r][1]=0

    if(len(recir)!=1): #반시계 방향으로 회전할 수 있다면
        rq.append((0,0,2, recir[0][0]))  # 왼쪽 위 꼭짓점 추가 (하,꼭짓점 값)
        recir[0][:-1] = recir[0][1:]  # 바람 이동 -> 왼쪽으로 한 칸씩 옮기기
        #cir[len(cir) - 1][:-1] = cir[len(cir) - 1][1:]
        rq.append((0,len(recir[0])-1,1,recir[0][len(recir[0])-1])) #오른쪽 위 꼭짓점 추가 (좌,꼭짓점 값)
        for w in range(1,len(recir)):
            recir[w-1][-1]=recir[w][-1] #바람 이동 -> 위쪽으로 한 칸씩 옮기기'''
        for j in range(len(recir)-1,0,-1):
            if recir[j][0]!=-1:
                recir[j][0]=recir[j-1][0] #바람 이동 -> 아랫쪽으로 한 칸씩 옮기기


    for d in range(len(rq)):
        curr,curc,dirn,v=rq.popleft()
        tempr=curr+directions[dirn][0]
        tempc=curc+directions[dirn][1]
        if 0<=tempr<len(recir) and 0<=tempc<len(recir[0]) and recir[tempr][tempc]!=-1:
            recir[tempr][tempc]=v

    cir[0][2:] = cir[0][1:-1]  # 바람 이동 -> 오른쪽으로 한 칸씩 옮기기
    cir[0][1] = 0

    if(len(cir)!=1): #시계 방향으로 회전할 수 있다면
        cq.append((len(cir)-1,0,3, cir[len(cir)-1][0]))  # 왼쪽 아래 꼭짓점 추가 (상,꼭짓점 값)
        cir[len(cir)-1][:-1] = cir[len(cir)-1][1:]  # 바람 이동 -> 왼쪽으로 한 칸씩 옮기기
        cq.append((len(cir)-1,len(cir[0])-1,1,cir[len(cir)-1][len(cir[0])-1])) #오른쪽 아래 꼭짓점 추가 (좌,꼭짓점 값)

        for w in range(1,len(cir)-1):
            if cir[w-1][0]!=-1:
                cir[w-1][0]=cir[w][0] #바람 이동 -> 위쪽으로 한 칸씩 옮기기'''

        for w in range(len(cir)-1,1,-1):
            cir[w][-1] = cir[w - 1][-1]  # 바람 이동 -> 아랫쪽으로 한 칸씩 옮기기


    for d in range(len(cq)):
        curr,curc,dirn,v=cq.popleft()
        tempr=curr+directions[dirn][0]
        tempc=curc+directions[dirn][1]
        if 0<=tempr<len(cir) and 0<=tempc<len(cir[0]) and cir[tempr][tempc]!=-1:
            cir[tempr][tempc]=v


    # 2-3: 공기청정기 작동 범위 합치기
    for w in range(len(lili)):
        if lili[w][0]==-1:
            lili[:w+1][:]=recir
            lili[w+1:][:]=cir

su=0
for q in range(len(lili)):
    for w in range(len(lili[0])):
        if lili[q][w]>0:
            su+=lili[q][w]

print(su)
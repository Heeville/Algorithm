#드래곤 커브 - 골드3
from collections import *
from itertools import *

#첫째 줄에는 드래곤 커브의 개수 n
#둘째 줄부터 n개의 줄에는 드래곤 커브의 정보가 주어진다. 드래곤 커브의 정보는 네 정수 x,y,d,g로 이루어져 있다.
# x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다.
#드래곤 커브는 서로 겹칠 수 있다.
#d=0 -> 우, d=1 -> 상, d=2 -> 좌 , d=3 -> 하
#출력은 크기가 1X1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력

n=int(input()) #드래곤 커브의 개수 n
direction=[[0,1],[-1,0],[0,-1],[1,0]] # 방향정보- 우 상 좌 하

lili=[[0]*101 for _ in range(101)]


#K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것이다.
#끝의 꼭짓점을 반드시 체크! 끝 꼭짓점 기준으로 시계방향 회전
def plusdir(curx,cury,tempd):
    tempx=curx+direction[tempd%4][1]
    tempy=cury+direction[tempd%4][0]  #%4 하는 이유는 방향 범위가 0~3이기 때문, dir을 +1 씩 계속 증가시킬거임
    #print(tempd%4, direction[tempd%4][1],direction[tempd%4][0])
    #print(tempx,tempy,23232323)
    return tempx,tempy

for i in range(n):
    x,y,d,g=map(int,input().split())
    if g==0:
        lili[y][x]+=1  #x는 열방향, y는 행방향
        lili[y+direction[d][0]][x+direction[d][1]] += 1
        #lili[x+direction[d][0]][y+direction[d][1]]+=1
    else:
        #print(x,y,d,g)
        qq = deque()  # qq는 방향을 담을 덱. 매우 중요한 역할을 할 것 이다!!!!!
        lili[y][x] += 1
        #print(x,y)
        tempgen=0 #0 -> g 세대까지 카운팅! 0세대부터 g세대 까지 순서대로 진행하것슴돠
        templist = []  # 좌표방향 임시로 담을 친구
        qq.append(d)
        lastx, lasty = x, y  #마지막 꼭짓점 좌표
        while qq:
                curx,cury,tempd=lastx,lasty,qq.pop() #qq는 선입선출
                #print(curx,cury,tempd,tempgen, 9999)
                tempx,tempy=plusdir(curx,cury,tempd)
                lili[tempy][tempx]+=1
                #print(tempx, tempy, tempd, tempgen, 34343)
                templist.append(tempd+1)
                #templist.append((tempx,tempy,tempd+1))
                lastx, lasty = tempx, tempy
                #print(lastx, lasty, tempd, tempgen)
                if len(qq)==0:
                    #print(templist)
                    for i in templist:
                        qq.append(i)
                    #print(qq,lastx,lasty,i)
                    tempgen+=1
                if tempgen>g:
                    #print(lastx, lasty, tempd, tempgen)
                    break
        '''for i in range(len(lili)):
            for w in range(len(lili[0])):
                print(lili[i][w], end=' ')
            print()'''

'''for i in range(len(lili)):
    for w in range(len(lili[0])):
        print(lili[i][w],end=' ')
    print()'''

#마지막: 크기가 1X1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력
#현재 꼭짓점 기준,자기 자신과 자신으로 부터 (0,1),(1,0),(1,1) 떨어진 곳이 모두 1일 경우 정사각형 갯수 추가!

square=0
pointdir=[[0,1],[1,0],[1,1]]
for q in range(len(lili)):
    for w in range(len(lili[0])):
        if lili[q][w]>0:
                #print(lili[q][w],(q,w))
                tempcount=0
                templi=[]
                for i in range(3):
                    tempr=q+pointdir[i][0]
                    tempc=w+pointdir[i][1]
                    if 0<=tempr<101 and 0<=tempc<101:
                        if lili[tempr][tempc]>0:
                            templi.append(lili[tempr][tempc])
                            tempcount+=1
                if tempcount==3:
                        square+=1

print(square)
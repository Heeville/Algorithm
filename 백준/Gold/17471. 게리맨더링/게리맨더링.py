from collections import *

N=int(input()) #구역의 갯수
#둘째 줄에 구역의 인구가 1번 구역부터 N번 구역까지 순서대로 주어진다. 인구는 공백으로 주어진다.
area=defaultdict(list) #인접 구역 사전
lili=list(map(int,input().split())) #각 구역에 대한 인구수 리스트
# -> lili 인덱스와 area 키 값의 관계    area 키 -1 =lili 인덱스

#셋째 줄부터 N개의 줄에 각 구역과 인접한 구역의 정보가 주어짐.
#첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호가 주어진다.
#구역 A가 구역 B와 인접하면 구역 B도 구역 A와 인접하다. 인접한 구역이 없을 수도 있다.

#선거구가 이어져 있는 지 확인하는 bfs 코드

#구역 A와 B가 인접하면 B와 A도 인접하다. 라는 조건 때문에 유효하지 않은 입력입니다.
def gbfs(grid,arr):
    q=deque()
    start=arr[0]
    arr.remove(start)
    visited={start:True}
    q.append(start)
    while q:
        cur=q.popleft()
        for i in grid[cur]:
            if i not in visited and i in arr:
                visited[i]=True
                if i in arr:
                    arr.remove(i)
                q.append(i)
    if len(arr)==0:
        return True
    else:
        return False
#and cur in grid[i]
#itertools 안쓴 조합 코드
def combinations(arr,k):
    result=[]

    def combine(current,start):
        # 현재 조합의 길이가 k라면, 결과에 추가
        if len(current)==k:
            result.append(current[:])
            return
        # start부터 원소를 하나씩 추가하며 재귀 호출
        for i in range(start,len(arr)):
            current.append(arr[i])
            combine(current,i+1)
            current.pop() # 재귀 호출이 끝나면 원소를 다시 제거

    combine([],0)
    return result

flag=0
for i in range(len(lili)):
    nearest=list(map(int,input().split()))
    if nearest[0]==0: #연결된 구역이 없을 때 ->
        flag+=1
    else:
        for w in range(1,len(nearest)):
            area[i+1].append(nearest[w])

#if flag>1 and N!=2:   #단절된 구역이 2개 이상 존재할 때(전체 구역이 2개인 경우는 제외)
    #print(-1)
if N==2: #전체 구역이 2개인 경우
    print(abs(lili[0]-lili[1]))
else:
    idx=[i+1 for i in range(N)]
    #1. 선거구 나누기
    count=0
    nocount=0
    sumlist=[]
    for a in range(1,int(N/2)+1):    # ex) n=6 이면 a 범위는 1~3
        partition=combinations(idx, a)
        for w in range(len(partition)):
            count += 1
            part2=idx.copy()
            part1=partition[w]
            for e in part1:
                part2.remove(e)
            #2. 선거구가 이어져 있는 지 확인
            bpart1=part1.copy()
            bpart2=part2.copy()
            sig1=gbfs(area,bpart1)
            sig2=gbfs(area,bpart2)
            #print(sig1,sig2,part1,part2)
            if sig1 and sig2:
                su1=0
                su2=0
                nocount=1
                for i in part1:   # idx 키 -1 =lili 인덱스
                    su1+=lili[i-1]
                for i in part2:  # idx 키 -1 =lili 인덱스
                    su2 += lili[i - 1]
                sumlist.append(abs(su1-su2))
                #print(sig1,sig2,part1,part2,abs(su1-su2))
    #print(nocount,count)
    if nocount==0:
        print(-1)
    else:
        print(min(sumlist))
    #print(count)
#print(gbfs(area,1))
#print(area)
#print(combinations(lili,3))
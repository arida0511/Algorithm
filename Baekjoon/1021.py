#1021

from collections import deque

n, m = map(int, input().split())
arr = [0 for _ in range(n)]
order = list(map(int, input().split()))
cur_order = 1       #현재 순서를 저장할 변수
cnt = 0         #이동 횟수를 저장할 변수
for i in range(m):
    #order[i] 저장해야하는 값의 위치
    arr[order[i]-1] = i+1       #해당 값의 위치에 1, 2, 3,..같은 순서 저장

queue = deque(arr)      #리스트를 큐로 변경
while cur_order <= m:
    cur_position = queue.index(cur_order) #찾으려는 값의 위치
    if cur_position == 0:		#찾으려는 값이 맨 앞이면 꺼내고 현재 찾는 순서 증가시키기
        queue.popleft()		#맨 앞에서 꺼내기
        cur_order += 1
        continue
    if cur_position <= len(queue)/2:		#위치가 큐 길이의 절반보다 작으면 왼쪽으로 회전
        queue.rotate(-1)
    else:		#크면 오른쪽으로 회전
        queue.rotate(1)
    cnt += 1		#회전 카운트 증가
print(cnt)
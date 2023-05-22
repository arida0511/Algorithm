#1260

n,m,begin = map(int, input().split())
arr=[[] for _ in range(n+1)]      #노드 개수만큼 선언(0은 사용하지 않음)
for _ in range(m):
    start, end = map(int, input().split())
    arr[start].append(end)      #start 리스트에 end 값 넣어주기
    arr[end].append(start)      #양방향이므로
for i in range(n+1):
    arr[i].sort(reverse=True)       #같은 레벨의 노드가 여러개인 경우, 낮은 노드부터 방문해야하므로 내림차순으로 정렬(stack에 순서대로 저장하고, 뒤부터 뽑기 때문)

stack = [begin]
visited = []        #패스 기록

while stack:        #stack이 빌때까지
    current = stack.pop()       #stack의 제일 뒤의 값 뽑기
    if current not in visited:      #방문하지 않은 곳이면 방문한 곳에 넣어주기
        visited.append(current)
    for dest in arr[current]:       #현재 방문 노드에서 갈 수 있는 노드 모두 탐색
        if dest not in visited:     #갈 수 있는 노드가 방문하지 않은 곳이면
            stack.append(dest)      #stack에 목록 추가
print(*visited)

for i in range(n+1):
    arr[i].sort()       #같은 레벨의 노드가 여러개인 경우, 낮은 노드부터 방문해야하므로 오름차순으로 정렬(queue에 순서대로 저장하고, 앞에서부터 뽑기 때문)

queue = [begin]
visited = []

while queue:        #queue가 빌때까지
    current = queue.pop(0)       #queue의 제일 앞의 값 뽑기
    if current not in visited:      #방문하지 않은 곳이면 방문한 곳에 넣어주기
        visited.append(current)
    for dest in arr[current]:       #현재 방문 노드에서 갈 수 있는 노드 모두 탐색
        if dest not in visited:     #갈 수 있는 노드가 방문하지 않은 곳이면
            queue.append(dest)      #queue에 목록 추가

print(*visited)
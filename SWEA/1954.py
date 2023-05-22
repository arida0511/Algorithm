#d2 1954

x_seq = [1, 0, -1, 0]		#x의 증감 순서 나타내기
y_seq = [0, 1, 0, -1]		#y의 증감 순서 나타내기
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    x_idx = 0		#x 증감순서 인덱스
    y_idx = 0		#y 증감순서 인덱스

    for i in range(1, n*n+1):
        arr[y][x] = i  # 배열에 값 설정

        x_step = x_seq[x_idx % 4]     # 다음 더할 값 넣어주기
        y_step = y_seq[y_idx % 4]
        if x + x_step >= n or y + y_step >= n or arr[y + y_step][x + x_step] != 0: #이동하려는 위치가 아니면 방향 전환
            x_idx += 1		# 증감 순서 인덱스 변경
            y_idx += 1
            x_step = x_seq[x_idx % 4]		# 증감 정도 더해주기
            y_step = y_seq[y_idx % 4]
        x += x_step     # 다음 단계로 이동
        y += y_step

    print(f"#{test_case}")
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print(end='\n')
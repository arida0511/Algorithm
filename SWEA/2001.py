#d3 1208

T = int(input())
for test_case in range(1, T + 1):
    max = 0
    n, m = map(int, input().split())
    mx, my = 0, 0			#m 영역의 시작 값 변수 설정
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n):           	#2차원배열 입력받기
        arr[i] = list(map(int, input().split()))
    for my in range(0, n-m+1):     	 #m 영역의 시작 값 -> 0부터 n에서 m만큼의 크기를 뺀 값 까지 탐색
        for mx in range(0, n-m+1):
            sum = 0     		#m 영역의 합
            for i in range(my, m+my):	 #m 영역 전개 -> m의 크기와, m영역의 시작 값 더해서 탐색
                for j in range(mx, m+mx):
                    sum += arr[i][j]
            if max < sum:
                max = sum
    print(f"#{test_case} {max}")
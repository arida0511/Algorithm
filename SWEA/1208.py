#d3 16800

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    start = 1		#탐색 시작
    end = n			#탐색 끝
    while True:
        if n % start == 0:		#n이 start로 나누어 떨어지면 소인수라는 뜻
            end = n / start
        if start >= end or start >= n**(1/2):		#소인수분해는 제곱근이면 끝남
            break;
        start += 1			#탐색 시작 값 더해주기
    print(f"#{test_case} {int(n/end+end-2)}")			#마지막에 찾은 end값으로 나누어 떨어지는 값을 구해서 2 빼주기
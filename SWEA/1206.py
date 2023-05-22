#1206

for iter in range(1,11):
    T = int(input())
    apart= list(map(int, input().split()))			#아파트 층 수를 담을 배열
    cnt=0					#조망 확보한 층 수를 담을 배열
    for i in range(2, T-2):				#3번째부터 n-2번째까지 탐색
        max=0
        for j in range(i-2, i+3):		#해당 아파트에서 양옆 두 수 파악
            if j==i:				#해당 아파트이면 패스
                continue
            if apart[j]>max:			#양옆 2개씩의 아파트 중에 가장 높은 아파트 찾기
                max=apart[j]
        if max < apart[i]:				#가장 높은 아파트가 해당 아파트 보다 작으면
            cnt += apart[i]-max				#해당 아파트의 층 수에서 주변에서 가장 높은 아파트의 층 수 빼기
    print(f"#{iter} {cnt}")
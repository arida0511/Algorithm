#d3 14555

T = int(input())
for test_case in range(1, T+1):
    arr = input()
    cnt = 0
    flag = 0
    for i in arr:
        if flag == 1:			#앞 인덱스가 '('였다면 패스
            flag = 0
            continue
        if i == '|' or i == '.':		#'|'나 '.'일 경우 패스
            continue
        elif i == '(':			#'('라면 flag 세우고 개수 증가
            flag = 1
            cnt += 1
        elif i == ')':			#')'라면 개수 증가 -> '()'인 공은 앞의 flag로 이미 걸렀음
            cnt += 1
    print("#{} {}".format(test_case, cnt))
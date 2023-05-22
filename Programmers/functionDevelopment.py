#기능개발

import math

def solution(progresses, speeds):
    answer = []
    days = []
    time =0 #앞의 값
    cnt = 1
    for i in range(len(progresses)):		#소요 날짜 구하는 배열
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    for i in range(len(days)):
        if time == 0:		#맨 앞 값이면 time에 넣어준뒤 계속 진행
            time = days[i]
            continue
        elif time >= days[i]:		#앞의 값이 현재 날짜보다 크면 cnt 증가
            cnt += 1
        else:			#앞의 값이 현재 날짜보다 작으면
            answer.append(cnt)		#현재 값 넣어주고
            cnt = 1			#카운트 초기화
            time = days[i]		#현재값을 time으로 설정
    answer.append(cnt)			#마지막 cnt값까지 넣어주기
    return answer
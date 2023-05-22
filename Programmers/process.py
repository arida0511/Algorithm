#level2 프로세스

def solution(priorities, location):
    answer = 0
    processes = [0 for _ in range(len(priorities))]     #priorities 큐만큼의 리스트 선언후 0으로 초기화
    processes[location] = 1     #목표 인덱스에만 값을 1로 설정
    while(priorities):
        exe_prior = priorities.pop(0)
        exe_proce = processes.pop(0)
        if not priorities:      #더이상 비교할 값이 없으면 break
            answer += 1
            break
        if exe_prior < max(priorities):   #만약 대기중인 프로세스 중 우선순위가 더 높은 것이 있다면
            priorities.append(exe_prior)
            processes.append(exe_proce)
        else:   #더 높은 것이 없다면
            answer += 1
            if exe_proce == 1:      #뽑은 값이 1이라면
                break
    return answer
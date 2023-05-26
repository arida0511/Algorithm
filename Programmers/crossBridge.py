#다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    dest = 0
    car_num = len(truck_weights)
    time = 0
    cur_weight = 0
    flag = 1 #출발할 차를 뽑아와야하는지라는 표시
    arr = [0 for _ in range(bridge_length)]
    bridge = deque(arr)
    truck_weights = deque(truck_weights)
    while dest < car_num:
        if truck_weights and flag == 1:      #출발 안한 트럭이 존재하고
            car = truck_weights.popleft()
        time += 1

        dest_car = bridge.popleft()
        if dest_car:  # 도착한 값이 0이 아니라면
            dest += 1
            cur_weight -= dest_car

        if cur_weight + car <= weight:
            bridge.append(car)
            cur_weight += car
            flag = 1
        else:
            bridge.append(0)
            flag = 0

    return time
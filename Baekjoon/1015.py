#1015

n = int(input())
A = list(map(int, input().split()))
P = [0 for _ in range(n)]
P_idx=0       #P에 저장할 값

while P_idx < n:
    A_idx = A.index(min(A))
    A[A_idx] = 1001     #큰 수로 초기화
    P[A_idx] = P_idx
    P_idx += 1
print(*P)
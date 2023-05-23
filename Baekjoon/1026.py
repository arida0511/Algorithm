#1026

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum=0
while(max(b)>0):
    sum += max(b)*min(a)
    b[b.index(max(b))] = 0
    a[a.index(min(a))] = 101
print(sum)
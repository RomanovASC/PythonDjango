a = list(map(int, input().split()))
N = len(a)
b = []
for i in range (N):
    if a[i] % 2 == 0:
        b.append(a[i])
    if a[i] == 237:
        break
print(b)
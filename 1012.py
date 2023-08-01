import sys
sys.setrecursionlimit(10000)

def changetozero(x, y):
    global arr
    if x >= M or y >= N or x < 0 or y < 0:
        return
    if arr[x][y] == 1:
        arr[x][y] = 0
        changetozero(x - 1, y)
        changetozero(x + 1, y)
        changetozero(x, y - 1)
        changetozero(x, y + 1)

r = int(input())
ans = []

for _ in range(r):
    worm = 0
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(N)] for _ in range(M)]  # Swap M and N for correct dimensions.
    for _ in range(K):
        i, j = map(int, input().split())
        arr[i][j] = 1
    for x in range(M):
        for y in range(N):
            if arr[x][y] == 1:
                changetozero(x, y)
                worm += 1
    ans.append(worm)

for i in ans:
    print(i)

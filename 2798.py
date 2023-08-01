N , M = map(int,input().split())

# N장의 카드 중 3장을 골라서 M 에 최대한 가깝게 만들어야함

# 브루트포스 알고리즘 인거같다.
cards = input().split()
total_sum = []
ans = []

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i != j and i != k  and j != k:
                total_sum.append(int(cards[i]) + int(cards[j]) + int(cards[k]))

for a in range(len(total_sum)):
    if total_sum[a] <= M:
        ans.append(total_sum[a])
    else:
        ans.append(0)

print(max(ans))




num_country , country = map(int,input().split())
info_country = []
ans = []
rank = 1
for _ in range(num_country):
    info = list(map(int,input().split()))
    if info[0] == country:
        ans = info
    info_country.append(info)

for val in info_country:
    if ans[1] < val[1]:
        rank+=1
    elif ans[2] < val[2] and ans[1] == val[1]:
        rank+=1
    elif ans[3] < val[3] and ans[2] == val[2] and ans[1] == val[1]:
        rank+=1
print(rank)

many , price = map(int,input().split())
cnt = 0
coins = []
for _ in range(many):
    coins.append(int(input()))
for i in range(many):
    cnt += int(price/coins[many-i-1])
    price -= int(price/coins[many-i-1]) * coins[many-i-1]
    if(price == 0):
        break
print(cnt)

# Greedy 알고리즘

''' 
눈앞의 이익만 추구하는 알고리즘 
knapsack , 동전 문제에서 쓰인다 단 , 동전은 작은 동전의 배수여야한다.

---코드---
    n,k = map(int,input().split())
    a = []
    coin = 0
    for _ in range(n):
        a.append(int(input()))
    a.sort(reverse=True)
    
    # GREEDY
    for i in a:
        coin += k//i
        k = k%i << 여기서 만약 i 가 k 보다 크다면 그대로 k 가 나올것이기때문에 , 이게 훨씬 쉽다. 
    print(coin)
'''
# 보드를 잘라서 8 * 8 크기의 체스판을 만들어야한다.
# 체스판은 검은색과 흰색이 번갈아 사용되어야한다.
# 최소 몇개를 칠해야 체스판이 만들어질까?

col , row = map(int,input().split())
chess = []
mini_chess = []

# 일단 chess 판을 만들수있는 구성은 W로 시작하거나 , B 로 시작하거나 둘중하나임

# 부르트포스 문제인듯???
# 행,열 에 대한 특정한 규칙이 보인다. col + row 를 더한값에 /2 해서 나누어 떨어지는곳과 , 아닌 곳을 나눠서 생각하자
for _ in range(col):
    chess.append(input())

for a in range(col-7):
    for b in range(row-7):
        idx1 = 0
        idx2 = 0
        for c in range(a,a+8):
            for d in range(b,b+8):
                if((c+d)%2 == 0):
                    if chess[c][d] == 'B':
                        idx1+=1
                    if chess[c][d] == 'W':
                        idx2+=1
                else:
                    if chess[c][d] =='B' :
                        idx2+=1
                    if chess[c][d] == 'W':
                        idx1+=1
        mini_chess.append(idx1)
        mini_chess.append(idx2)

print(min(mini_chess))

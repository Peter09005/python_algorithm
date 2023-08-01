one = [0,1]
zero = [1,0]
ans = []
r = int(input())
for _ in range(r):
    N = int(input())
    op1 = [0, 0]
    op2 = [0, 0]
    n = 2
    if N == 0:
        ans.append(str(1)+" "+str(0))
    elif N == 1:
        ans.append(str(0)+" "+str(1))
    else:
        while(n <= N):
            if n == 2:
                op1[0] = one[0] + zero[0]
                op1[1] = one[1] + zero[1]
            elif n ==3:
                op2[0] = op1[0] + one[0]
                op2[1] = op1[1] + one[1]
            else:
                if n%2 == 0:
                    op1[0] = op2[0] + op1[0]
                    op1[1] = op2[1] + op1[1]
                else:
                    op2[0] = op2[0] + op1[0]
                    op2[1] = op2[1] + op1[1]
            n+=1
        if N%2 == 0:
            ans.append(str(op1[0])+" "+str(op1[1]))
        else:
            ans.append(str(op2[0])+" "+str(op2[1]))

for i in ans:
    print(i)


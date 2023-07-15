
from sys import stdin
def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0) # int(num)은 아예 뒷자리가 없어짐.

d_level = 0
d_list = []
ppl = int(stdin.readline())
if ppl != 0:
    ppl_1 = round2(ppl*0.15)
    for i in range(0,ppl):
        d_list.append(int(stdin.readline()))
    d_list.sort();
    for j in range(ppl_1,ppl-ppl_1):
        d_level += d_list[j]

    answer = round2(d_level/(ppl-ppl_1*2))
    print(answer)
else:
    print(0)

# round 함수는 앞자리가 홀수면 올리고 앞자리가 짝수면 버리는 방법)을 기반으로 실행된다. ex) 0.5 > 0 1.5 > 2


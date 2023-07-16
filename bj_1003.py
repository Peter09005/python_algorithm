'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}

----------------------------------------------------------------------------------------------------

import sys
def fibonacci(n):
    if n == 0 :
        # print 0
        global cnt_zero
        cnt_zero += 1
        return 0
    elif n == 1:
        global cnt_one
        cnt_one += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(sys.stdin.readline())
ans_list = []
for _ in range(n):
    N = int(sys.stdin.readline())
    cnt_zero = 0
    cnt_one = 0
    fibonacci(N)
    ans_list.append((str(cnt_zero) + " " + str(cnt_one)))
for i in range(n):
    print(ans_list[i])
'''
import sys

# 시간초과


def find(n, col, row):
    global num
    if n == 1:
        print(int(num))
        return
    if col >= n/2:
        if row >= n/2:
            num += n/2 * n/2 * 3
            find(n / 2, col - n/2, row - n/2)
        else:
            num += n/2 * n/2 *2
            find(n / 2, col-n/2, row)
    else:
        if row >= n/2:
            num+= n/2 * n/2 * 1
            find(n / 2, col, row-n/2)
        else:
            num += 0
            find(n / 2, col, row)



n,col,row = map(int,input().split()) # 10 * 10 > 1024 * 1024
nn = 2**n
num = 0
find(nn,col,row)

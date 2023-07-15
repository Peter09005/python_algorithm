cnt_i = int(input())
cnt_i_list = []
cnt_j_list = []
str_i = input()
cnt_j = int(input())
str_j = input()
for i in range(0,cnt_i*2):
    if i % 2 == 0:
        cnt_i_list.append(str_i[i])
for j in range(0,cnt_j*2):
    if j % 2 == 0:
        cnt_j_list.append(str_j[j])
for k in range(0,len(cnt_j_list)):
    if cnt_i_list.count(cnt_j_list[k]) > 0:
        print("1")
    else :
        print("0")


# RunTimeError > A RuntimeError is raised when attempting to perform an invalid operation of some kind,
# which doesn't meet the criteria of a more specific error classification. Don't be surprised if you come across this error within your code.

# 아마  4 1 5 2 3 이렇게 넣어야하는데 내가 이렇게 안넣어서 그런듯

# 시간 초과가 뜬다.


#sol-1
N = int(input())
A = set(map(int,input().split())) #map(function, iterable)
M = int(input())
arr = list(map(int,input().split()))
for num in arr:
    print(1) if num in A else print(0)

# sol-2
n = int(input())
a = set(input().split())
m = int(input())
b = input().split()

answer = '\n'.join('1' if x in a else '0' for x in b)
print(answer)
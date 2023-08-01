import sys

a = set()

cnt = int(sys.stdin.readline())
for _ in range(cnt):
    command = sys.stdin.readline().split()
    if len(command) == 1:
        if command[0] == "all":
            a = set([i for i in range(1,21)])
        else:
            a = set()
    else:
        func , x = command[0] , int(command[1])
        if func == "add":
            a.add(x)
        elif func == "check":
            if x in a:
                print(1)
            else:
                print(0)
        elif func == "remove":
            a.discard(x)
        else:
            if x in a:
                a.discard(x)
            else:
                a.add(x)


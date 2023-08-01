def empty(queue):
    if len(queue) > 0:
        return 0
    else:
        return 1
import sys
queue = []

num = int(sys.stdin.readline())
for i in range(num):
    oper = sys.stdin.readline().split()
    if oper[0] == "push":
        queue.append(int(oper[1]))
        continue
    elif oper[0] == "pop":
        if empty(queue) == 1:
            print(-1)
            continue
        else:
            print(queue[0])
            queue.remove(queue[0])
            continue
    elif oper[0] == "size":
        print(len(queue))
        continue
    elif oper[0] == "empty":
        print(empty(queue))
        continue
    elif oper[0] == "front":
        if empty(queue) == 1:
            print(-1)
            continue
        else:
            print(queue[0])
    elif oper[0] == "back":
        if empty(queue) == 1:
            print(-1)
            continue
        else:
            print(queue[-1])
            continue
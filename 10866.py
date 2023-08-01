import sys
def empty(queue):
    if len(queue) > 0:
        return 0
    else:
        return 1

queue = []
num = int(sys.stdin.readline())


for i in range(num):
    oper = sys.stdin.readline().strip().split()
    if oper[0] == "push_back":
        queue.append(int(oper[1]))
    elif oper[0] == "push_front":
        queue.insert(0,int(oper[1]))
    elif oper[0] == "pop_front":
        if empty(queue) == 1:
            print(-1)
        else:
            print(queue[0])
            queue.pop(0)
    elif oper[0] == "pop_back":
        if empty(queue) == 1:
            print(-1)
        else:
            print(queue[-1])
            queue.pop(-1)
    elif oper[0] == "size":
        print(len(queue))
    elif oper[0] == "empty":
        print(empty(queue))
    elif oper[0] == "front":
        if empty(queue) == 1:
            print(-1)
        else:
            print(queue[0])
    elif oper[0] == "back":
        if empty(queue) == 1:
            print(-1)
        else:
            print(queue[-1])
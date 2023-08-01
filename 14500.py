
def num_ways(co , ro):
    global col
    global row
    if (co == 0 or co == col-1) and (ro == 0 or ro == row-1):
        return 2
    elif (co == 0 or ro == 0) or (co == col-1 or ro == row-1):
        return 1
    else:
        return 4


col,row = map(int,input().split())
field = []
for _ in range(col):
    field.append(input().split())
print(field)

def check(value_n):
    temp2 = 0
    for k in range(value_n):
        for elem in range(value_n):
            temp2 += Matrix[k][elem]
    return temp2

no_queries = int(input())

for i in range(no_queries+1):
    value_n = int(input())
    r,c = 2*value_n,2*value_n
    Matrix = [[0 for x in range(c)] for y in range(r)]
    for j in range(2*value_n):
        temp = input().split()
        for elements in range(len(temp)):
            Matrix[j][elements] = int(temp[elements])

    values = 0
    temp = check(value_n)
    if temp > values:
        values = temp
    elif:
        Matrix[]

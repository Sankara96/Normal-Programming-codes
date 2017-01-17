file = open('prepare.in','r')
line = 1
result = 0


for lines in file:
    if line ==1:
        days = int(lines)
        line= 2
        if len(lines)<1:
            break
    elif line ==2:
        p = map(int,lines.split())
        line = 3
    elif line == 3:
        t = map(int,lines.split())
        for i in range(days):
            if p[i]>t[i]:
                result+=p[i]
            else:
                result+=t[i]
        line = 1
with open('prepare.out','a+') as result1:
    result1.write('{0}\n'.format(result))

current_configuration = raw_input().split()
final_configuration = raw_input().split()
result = 0
current_configuration = [int(x) for x in current_configuration]
final_configuration = [int(y) for y in final_configuration]
for i in range(5):
    if int(current_configuration[i])==int(final_configuration[i]):
        continue
    else:
        if int(current_configuration[i] < final_configuration[i]):
            temp1 = final_configuration[i]-current_configuration[i]
            condition = True
            c = int(current_configuration[i])
            count = 1
            while condition:
                if c==0:
                    c=9
                else:
                    c-=1
                if c!=int(final_configuration[i]):
                    count+=1
                elif c == int(final_configuration[i]):
                    temp2 = count
                    condition = False
            if temp1<temp2:
                result+=temp1
            elif temp1>temp2:
                result+=temp2
            else:
                result+=temp1
        else:
            temp1 =current_configuration[i]-final_configuration[i]
            condition = True
            c = int(current_configuration[i])
            count = 1
            while condition:
                if c == 9:
                    c = 0
                else:
                    c += 1
                if c != int(final_configuration[i]):
                    count += 1
                elif c == int(final_configuration[i]):
                    temp2 = count
                    condition = False
            if temp1 < temp2:
                result += temp1
            elif temp1 > temp2:
                result += temp2
            else:
                result += temp1


print "{0}".format(result)
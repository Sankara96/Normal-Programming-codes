import threading

n,b = map(int,raw_input().split())
resultant = []
bucket = {}
for i in range(n):
    temp = map(float, raw_input().split())
    temp[0] = int(temp[0])
    resultant.append(temp)

resultant.sort(key=lambda x: x[3],reverse=True)

for item in xrange(b):
    bucket[resultant[0][0]]=resultant[0]
    resultant = resultant[1:]

def procedure(temp):
    try:
        global resultant
        control = temp[0].lower()
        id_value = int(temp[1])
        try:
            elements = bucket[id_value]
        except:
            print "Point doesn't exist in the bucket."
            raise Exception
        if control == 'f':
            print "{0} = ({1},{2},{3})".format(elements[0], format(elements[1], '.3f'), format(elements[2], '.3f'),
                                               format(elements[3], '.3f'))
            raise Exception
        elif control == 'r':
            if len(resultant) > 0:
                print "Point id {0} removed.".format(elements[0])
                bucket.pop(elements[0])
                bucket[resultant[0][0]] = resultant[0]
                resultant = resultant[1:]
                raise Exception
            else:
                print "No more points can be deleted."
                raise Exception
        else:
            raise Exception
    except:
        pass
while True:
    try:
        temp = raw_input().split()
        a = threading.Thread(target=procedure(temp))
        a.run()
    except EOFError:
        break



from itertools import permutations

no_test_cases = int(input())
for i in range(no_test_cases):
    temp = raw_input()
    a = [''.join(p) for p in permutations(temp)]
    a = sorted(a)
    index = a.index(temp)
    length = len(a)
    while(index<=length):
        try:
            if a[index] == a[index+1]:
                index = index+1
            else:
                print a[index+1]
                break
        except IndexError:
            index = length+1
    else:
        print "no answer"

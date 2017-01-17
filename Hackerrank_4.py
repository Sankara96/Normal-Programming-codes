no_queries = int(input())
for i in range(no_queries):
    a = raw_input()
    b = raw_input()
    temp_a = a
    pointer = 0
    length_b=len(b)
    array_a = []
    condition = False
    for x in temp_a:
        array_a.append(x)
    temp = array_a
    for letters in array_a:
        if letters.upper()==b[pointer]:
            pointer+=1
            n = array_a.index(letters)
            array_a[n] = letters.upper()
            if pointer>=length_b:
                condition = True
                break
            elif pointer<length_b and condition is False:
                condition = False
        else:
            if letters.isupper():
                continue
            else:
                index = array_a.index(letters)
                array_a[int(index)] = 0

    actual = filter(lambda a: a!=0,array_a)
    for elements in actual:
        if elements.isupper():
            continue
        else:
            num = actual.index(elements)
            actual[num] = 0
    actual_filtered = filter(lambda a: a!=0,actual)
    str = ''
    for elements in actual_filtered:
        str = ''.join((str,elements))

    if str==b:
        print "YES"
    else:
        print "NO"
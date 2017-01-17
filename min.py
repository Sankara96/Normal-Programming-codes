size = input()
a = raw_input().split()
b = raw_input().split()
a = [int(x) for x in a]
b = [int(x) for x in b]
result = None
result_list = []
for elements in a:
    index_a = a.index(elements)
    index_b = b.index(elements)
    diff = abs(index_a-index_b)
    if diff<=result or result is None:
        if diff==result:
            result_list.append(elements)
        elif diff<result:
            result_list = []
            result_list.append(elements)
        result = diff
        result_list.append(elements)
print min(result_list)
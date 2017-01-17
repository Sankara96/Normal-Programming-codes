no_test_cases = input()
result = []
for i in range(no_test_cases):
    no_buildings = input()
    buildings = raw_input().split()
    buildings = [int(x) for x in buildings]
    count = 0
    temp = buildings[0]
    for building in buildings:

        if temp<=building:
            temp = building
            count+=1
    result.append(count)
for elements in result:
    print elements

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


if __name__ == '__main__':

    input = raw_input().split()
    n = int(input[0])
    m = int(input[1])
    items = raw_input().split()
    items = [int(x) for x in items]
    for i in range(m):
        temp = raw_input().split()
        temp = [int(x) for x in temp]
        if len(temp)== 2:
            duplicate = list_duplicates_of(items,0)
            try:
                index = duplicate[temp[1]-1]
                print index
            except:
                print "NO"
        elif len(temp)== 3:
            items[temp[1]] = temp[2]


no_times_to_store = int(input())

for i in range(no_times_to_store):
    temp = raw_input().split()
    no_sticks = int(temp[0])
    no_box = int(temp[1])
    no_boxes_choose = int(temp[2])
    boxes = []
    box_available = list(range(1,no_box+1))
    for c in range(no_boxes_choose):
        if len(boxes)==0:
            boxes.append(box_available[0])
            box_available = box_available[1:]
        else:
            for j in range(2,no_box+1):
                if (no_sticks-(boxes[0]+j)) in box_available:
                    boxes.append(j)
                    boxes.append(no_sticks-(boxes[0]+j))
                    break
            if len(boxes)>=no_boxes_choose:
                print "{0} {1} {2}".format(boxes[0],boxes[1],boxes[2])
                break
            else:
                print "-1"
                break



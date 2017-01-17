
def pattern(n):

    square_n = n**2
    original_number_list = []
    original_number_list = list(range(1,square_n+1))
    front = []
    back = []
    temp =[]
    count = 1
    inverse = 0
    original_number_list.append(0)
    for elements in original_number_list:
        if count <= n:
            temp.append(elements)
            if count == n:
                if inverse == 0:
                    inverse = 1
                else:
                    inverse = 0
            count += 1
        elif count > n:
            if inverse == 1:
                front.append(temp)
                temp = []
                temp.append(elements)
                count = 2
            elif inverse == 0:
                back.append(temp)
                temp = []
                temp.append(elements)
                count = 2
    for num in front:
        for n in range(len(num)):
            if n == len(num)-1:
                print "{0}".format(num[n]),
            else:
                print "{0}*".format(num[n]),
        print ""
    for num in back[::-1]:
        for n in range(len(num)):
            if n == len(num) - 1:
                print "{0}".format(num[n]),
            else:
                print "{0}*".format(num[n]),
        print ""


if __name__ == '__main__':
    n = raw_input("Enter something:")
    pattern(int(n))
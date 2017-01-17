import sys
def pattern(n):
    square = n**2
    num_list = range(1,square+1)
    back = []
    temp =[]
    change = 0
    for numbers in num_list:
        if numbers%n==0:
            temp.append(numbers)
            if change == 1:
                back.append(temp)
                change = 0
                temp = []
            elif change == 0:
                for no in range(len(temp)):
                    if no == len(temp) - 1:
                        sys.stdout.write("{0}".format(temp[no]))
                    else:
                        sys.stdout.write("{0}*".format(temp[no]))
                print ""
                change = 1
                temp = []
        elif numbers%n != 0:
            temp.append(numbers)
    for elements in back[::-1]:
        for no in range(len(elements)):
            if no == len(elements)-1:
                sys.stdout.write("{0}".format(elements[no]))
            else:
                sys.stdout.write("{0}*".format(elements[no]))
        print ""
if __name__ == '__main__':
    loop = True
    while loop:
        try:
            n = int(raw_input("Enter a number: "))
            pattern(n)
            loop = False
        except:
            print "You did not enter a number"





class Watson_permutation(object):
    def __init__(self):
        self.lines = 1

    def start(self,file):
        input_file = open(file, "r")
        for lines in input_file:
            if self.lines == 1:
                self.no_test_cases = int(lines)
                self.lines = 2
                self.cases = 0
            else:
                temp = lines.split()
                temp =[int(x) for x in temp]
                mini = min(temp)
                self.cases+=1
                if temp[1] == 0:
                    answer = 0
                else:
                    answer = mini+1
                print "Case #{0}: {1}".format(self.cases, answer)
                with open(r"C:\Users\ADMIN\Desktop\Output.out", "a+") as result:
                    result.write("Case #{0}: {1}\n".format(self.cases, answer))
if __name__ == '__main__':

    hey = Watson_permutation()
    hey.start(r'C:\Users\ADMIN\Downloads\A-small-attempt0.in')

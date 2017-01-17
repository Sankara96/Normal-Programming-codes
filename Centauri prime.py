
class rulers(object):

    def __init__(self,file):
        self.lines = 1
        self.input = file
        with open(r"C:\Users\ADMIN\Desktop\Output.out", "a+") as result:
            result.truncate()
        self.no_test_cases = 0
        self.test_case = 0
        self.vowel = ['a','e','i','o','u']
        self.start()

    def start(self):

        input = open(self.input,"r")

        for lines in input:

            if self.lines == 1:
                self.no_test_cases = int(lines)
                self.lines = 2
            elif self.lines == 2:
                temp = lines
                self.calculate(temp)
                if self.test_case == self.no_test_cases:
                    break

    def calculate(self,temp):

        length = len(temp)
        print temp
        temp = temp[:length-1]
        temp1 = temp
        temp = temp.lower()
        print temp
        if temp[length-2] in self.vowel:
            self.test_case+=1
            print "Case #{0}: {1} is ruled by a queen.".format(self.test_case,temp1)
            with open(r'C:\Users\ADMIN\Desktop\Output.out', 'a+') as output:
                output.write("Case #{0}: {1} is ruled by a queen.\n".format(self.test_case,temp1))
        elif temp[length-2] is 'y':

            self.test_case+=1
            print "Case #{0}: {1} is ruled by nobody.".format(self.test_case,temp1)
            with open(r'C:\Users\ADMIN\Desktop\Output.out', 'a+') as output:
                output.write("Case #{0}: {1} is ruled by nobody.\n".format(self.test_case, temp1))
        else:
            self.test_case+=1
            print "Case #{0}: {1} is ruled by a king.".format(self.test_case,temp1)
            with open(r'C:\Users\ADMIN\Desktop\Output.out', 'a+') as output:
                output.write("Case #{0}: {1} is ruled by a king.\n".format(self.test_case, temp1))


if __name__ == '__main__':

    party = rulers('C:\Users\ADMIN\Downloads\A-small-practice-2.in')
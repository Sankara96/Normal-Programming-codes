
class reverse_words(object):
    def __init__(self):
        self.item_list = []
        self.items =[]
        self.lines = 1
        self.test_cases = 1
        self.case = 1
    def start(self,file):
        with open(file,'r') as input_file:
            for lines in input_file:
                if self.lines == 1:
                    self.test_cases = int(lines)
                    print self.test_cases
                    self.lines += 1
                else:
                    if self.lines<=self.test_cases+1: # adding one since the lines start from 2
                        self.item_list = lines.split()
                        print self.item_list
                        self.items = self.item_list.reverse()
                        print self.item_list
                        with open(r'C:\Users\ADMIN\Desktop\Output.out',"a") as output:
                            output.write("Case #{0}:".format(self.case))
                            for elements in self.item_list:
                                output.write(" {0}".format(elements))
                            output.write("\n")
                            self.case += 1
                        self.lines += 1

if __name__ == '__main__':
    revers = reverse_words()
    revers.start(r'C:\Users\ADMIN\Downloads\B-large-practice.in')
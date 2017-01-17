
class rain(object):
    def __init__(self):
        self.lines = 1
        self.island_size = []
        self.no_test_Case = 0
        self.test_case = 0
        self.count = 0
        self.island = []
        self.increase = 0
    def start(self,file):
        input_file = open(file,"r")

        for lines in input_file:
            if self.lines == 1:
                self.no_test_Case = int(lines)
                self.lines = 2
            elif self.lines == 2:
                self.island_size.append(lines.split())
                self.lines = 3
            elif self.lines == 3:
                if self.count<=self.island_size[0][0]:
                    #print lines.split()
                    self.island.append(lines.split())
                    self.count += 1
                    if self.count == int(self.island_size[0][0]):
                        self.calculate()
                        self.lines = 2
                        self.island = []
                        self.count = 0

    def calculate(self):
        self.max_num = []
        for rows in self.island:
            self.max_num.append(max(rows))

        max_num = max(self.max_num)
        max_result = int(max_num) - 4
        print max_result
        self.island = []

if __name__ == '__main__':
    islands = rain()
    islands.start(r'C:\Users\ADMIN\Desktop\test_1.txt')

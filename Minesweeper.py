
class Game(object):

    def __init__(self,file):
        self.input = file
        self.lines = 1
        self.no_test_cases = 0
        self.test_cases = 0
        self.rows = 0
        self.column = 0

    def start(self):

        input = open(self.input,"r")

        for lines in input:

            if self.lines == 1:

                self.no_test_cases = int(lines)
                self.lines = 2
            elif self.lines == 2:
                self.row = int(lines)
                self.lines = 3
            elif self.lines == 3:

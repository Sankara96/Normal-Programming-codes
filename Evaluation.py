import serial
class evaluation(object):

    def __init__(self,file):
        self.lines = 1
        self.input = file
        self.no_test_cases = 0
        self.no_expression = 0
        self.expressions = {}
        self.start()
    def start(self):
        input = open(self.input,'r')
        for lines in input:
            if self.lines ==1:
                self.no_test_cases = int(lines)
                self.lines = 2
            elif self.lines ==2:
                self.no_expression = int(lines)
                self.lines = 3
                i = 0
            elif self.lines == 3:
                self.expressions[str(i)] = lines
                i+=1
                if i>=self.no_expression:
                    self.calculate()
                    self.lines = 2


    def calculate(self):


        pass
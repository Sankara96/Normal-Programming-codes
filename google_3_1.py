
class pokemon(object):
    def __init__(self,file):
        self.lines = 1
        self.input=  file
        self.no_test_cases = 0


        self.start()
    def start(self):
        input = open(self.input,'r')
        for lines in input:
            if self.lines ==1:
                self.no_test_cases = int(lines)
                self.lines =2
            elif self.lines ==2:
                temp= map(int,lines.split())
                self.r, self.c, self.rs, self.cs, self.s = temp
                self.lines = 3
            elif self.lines == 3:
                self.P,self.Q = map(float, lines.split())
                self.lines = 4
                temp1 = []
            elif self.lines == 4:
                temp = map(str,lines.split())
                temp1.append(temp)
                if len(temp1)==self.r:
                    self.calculate(temp1)

                    self.lines = 2

    def calculate(self,temp):
        temp_rs = self.rs
        while True:
        try:
            index = temp[temp_rs].inde0.x('A')
        except ValueError:
            if temp_rs<self.r:
                temp_rs+=1
            elif temp_rs>=self.r:
                temp_rs-=1
        row_movement = temp_rs-self.rs
        col_movement = index
        total_movement = row_movement+col_movement
        if total_movement<self.s:
            diff = self.s-total_movement
            for i in range(diff):
                

if __name__ == '__main__':
    pika = pokemon(r'C:\Users\ADMIN\Desktop\input.in')
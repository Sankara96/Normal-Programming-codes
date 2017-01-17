from itertools import permutations,combinations
import threading
import thread
class gym(object):

    def __init__(self):
        self.lines = 1
        self.no_test_cases = 0
        self.cases = 0

    def start(self,file):
        input_file = open(file, "r")

        for lines in input_file:

            if self.lines == 1:
                self.no_test_cases = int(lines)
                self.lines = 2
            elif self.lines == 2:
                temp = lines.split()
                temp = [int(numbers) for numbers in temp]
                self.a = temp [0]
                self.b = temp[1]
                self.n = temp[2]
                self.k = temp[3]
                self.calculate()

    def calculate(self):
        self.answer = []
        num_list = range(1,self.n+1)
        self.c = combinations(num_list,2)
        tempo = []
        for elements in self.c:
            tempo.append(elements)
        print "Finished"
        prev = 0
        current = 0
        length_tempo = len(tempo)
        if length_tempo%2==0:
            length_tempo = length_tempo/2
        else:
            length = length_tempo/3
        for i in range(5):
            current = prev+length_tempo
            temp1 = tempo[prev:current]
            prev = current
            t = threading.Thread(self.find(temp1))
            t.start()
            t.join()

        self.answer_length = len(self.answer)
        self.cases += 1
        print "Case #{0}: {1}".format(self.cases, self.answer_length)
        with open(r"C:\Users\ADMIN\Desktop\Output.out", "a+") as result:
            result.write("Case #{0}: {1}".format(self.cases, self.answer_length))
        self.answer = []

    def find(self,c):
        for elements in c:
            temp = permutations(elements)
            for sets in temp:
                if (sets[0]**self.a+sets[1]**self.b)%self.k ==0:
                    self.answer.append(elements)
if __name__ == '__main__':
    watson = gym()
    watson.start(r'C:\Users\ADMIN\Desktop\input.in')
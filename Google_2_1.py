from itertools import permutations
class Watson_permutation(object):
    def __init__(self):
        self.lines = 1
        with open(r"C:\Users\ADMIN\Desktop\Output.out", "a+") as result:
            result.truncate()
    def start(self,file):
        input_file = open(file, "r")

        for lines in input_file:

            if self.lines == 1:
                self.no_test_cases = int(lines)
                self.lines = 2
            elif self.lines == 2:
                temp = lines.split()
                self.n = int(temp[0])
                self.m = int(temp[1])
                self.calculate(self.n,self.m)

    def calculate(self,n,m):
        number_list = range(1,n+1)
        if n==1:
            self.output_answer = 1
        else:
            data = permutations(number_list)
            answer = []
            temp = []
            count = 0
            for array in data:
                prev_elements = False
                current_elements = 0
                for element_index in range(len(array)):
                    current_elements = array[element_index]
                    if prev_elements is False:
                        prev_elements = current_elements
                        continue
                    else:
                        if prev_elements<current_elements:
                            temp.append(prev_elements)
                            count+=1
                        elif prev_elements>current_elements:
                            if count!=0:
                                answer.append(temp)
                                temp = []
                                count = 0
                                temp.append(current_elements)
                            elif count == 0:
                                temp = []
                                temp.append(prev_elements)
                                answer.append(temp)
                                temp = []

if __name__ == '__main__':
    watson = Watson_permutation()
    watson.start(r'C:\Users\ADMIN\Desktop\input.in')

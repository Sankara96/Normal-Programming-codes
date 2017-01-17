

class constitution(object):
    def __init__(self):
        self.lines = 1
        self.no_test_cases = 0
        self.test_Case = 0
        self.no_persons = 0
        self.person_count = 0
        self.person_value = []
        self.list_persons = []
        with open(r"C:\Users\ADMIN\Desktop\Output.out", "a+") as result:
            result.truncate()

    def start(self,file):
        input_file = open(file,"r")

        for lines in input_file:
            if self.lines == 1:
                self.no_test_cases = int(lines)
                self.lines = 2
            elif self.lines == 2:
                self.no_persons = int(lines)
                self.lines = 3
            elif self.lines == 3:
                if self.person_count<=self.no_persons:
                    self.list_persons.append(lines)
                    self.person_count += 1
                    if self.person_count == self.no_persons:
                        self.calculate()
                        self.person_count = 0
    def calculate(self):
        name_set = set({})
        m = [0,""]
        array = [0]
        for names in self.list_persons:
            for letters in names:
                if letters!='\n':
                    name_set.add(letters)
            cur_len = len(name_set)
            if m[0]<cur_len:
                m[0] = cur_len
                m[1] = names
                array = [0]
                array[0] = cur_len
                array.append(names)
            elif m[0]==cur_len:
                if array[0] == cur_len:
                    array.append(names)
            name_set.clear()
        array = array[1:]
        array.sort                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  )
        self.test_Case += 1
        print "Case #{0}: {1}".format(self.test_Case,array[0])
        with open(r"C:\Users\ADMIN\Desktop\Output.out", "a") as result:
            result.write("Case #{0}: {1}".format(self.test_Case, array[0]))
        name_set.clear()
        self.lines = 2
        m = [0,""]
        self.person_value = []
        max_list = 0
        self.list_persons = []




if __name__ == '__main__':
    name = constitution()
    name.start(r'C:\Users\ADMIN\Downloads\A-large-practice.in')
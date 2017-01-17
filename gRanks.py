
class ranks(object):

    def __init__(self,file):
        self.file = file
        self.lines = 1
        self.atheletes = {}
        with open(r"C:\Users\ADMIN\Desktop\Output.out", "a+") as result:
            result.truncate()
    def start(self):
        input_file = open(self.file, "r")
        for lines in input_file:
            if self.lines == 1:
                self.no_test_cases = int(lines)
                self.lines = 2
                self.cases = 0
            elif self.lines == 2:
                self.no_places = int(lines)
                self.lines = 3
            elif self.lines == 3:
                self.places_value = lines.split()
                self.places_value = [int(x) for x in self.places_value]
                self.lines = 4
            elif self.lines == 4:
                self.no_competitions = int(lines)
                self.competition = 0
                self.lines = 5
            elif self.lines == 5:
                temp = lines.split()
                if temp[1] in self.atheletes:
                    self.atheletes[temp[1]].append((int(temp[0])*self.places_value[0]))
                else:
                    self.atheletes[temp[1]] = []
                    self.atheletes[temp[1]].append((int(temp[0]) * self.places_value[0]))

                if temp[2] in self.atheletes:
                    self.atheletes[temp[2]].append((int(temp[0]) * self.places_value[1]))
                else:
                    self.atheletes[temp[2]] = []
                    self.atheletes[temp[2]].append((int(temp[0]) * self.places_value[1]))
                self.competition+=1
                if self.competition ==  self.no_competitions:
                    self.lines = 6
            elif self.lines == 6:
                self.top_values = int(lines)
                self.calculate()
                self.lines = 2
                self.atheletes = {}
    def getKey(self,item):
        return item[1]

    def getstr(self, item):
        return item[0]

    def calculate(self):
        result = []
        value = []
        for athelete in self.atheletes:
            temp = self.atheletes[athelete]
            temp2 = 0
            temp1 = 0
            if len(temp)>=self.top_values:
                for num in range(self.top_values):
                    temp1 = max(temp)
                    for n in range(len(temp)):
                        if temp[n] == temp1:
                            temp2+=temp[n]
                            temp.pop(n)
                            break
            else:
                temp2 = sum(temp)
            value.append(temp2)
            result.append(list([athelete,temp2]))
        a = sorted(result, key=self.getKey,reverse=True)
        st = set()
        duplicate_values = []
        for s in value:
            if s not in st:
                st.add(s)
            else:
                duplicate_values.append(s)
        go_ahead = 1
        duplicate = []
        count = 1
        print "Case #{0}:\n".format(self.cases+1)
        with open(r'C:\Users\ADMIN\Desktop\Output.out','a+') as output:
            output.write("Case #{0}:\n".format(self.cases+1))
        self.cases+=1
        for i in range(len(a)):
            temp = a[i]
            if temp[1] not in duplicate_values and go_ahead == 1:
                print "{0}: {1}".format(count,temp[0])
                                                                                  with open(r'C:\Users\ADMIN\Desktop\Output.out', 'a+') as output:
                    output.write("{0}: {1}\n".format(count,temp[0]))
                count+=1
            elif temp[1] in duplicate_values:
                duplicate.append(temp)
                go_ahead = 0
                try:
                    if a[i+1][1] not in duplicate_values:
                        b = sorted(duplicate, key=self.getstr)
                        t = len(b)
                        for elements in b:
                            print "{0}: {1}".format(count, elements[0])
                            with open(r'C:\Users\ADMIN\Desktop\Output.out', 'a+') as output:
                                output.write("{0}: {1}\n".format(count, elements[0]))
                        go_ahead = 1
                        duplicate = []
                        count+=t
                    else:
                        continue
                except:
                    continue





if __name__ == '__main__':
    ranking = ranks(r'C:\Users\ADMIN\Downloads\A-large-practice (1).in')
    ranking.start()

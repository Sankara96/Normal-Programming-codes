

class alien(object):
    def __init__(self):
        self.letters_in_wrd = set({})
        self.lines = 0
        self.no_test_cases = 0
        self.test_case = 0
    def start(self,file):

        input_file = open(file,"r+")

        for lines in input_file:
                if self.lines == 0 :
                    self.no_test_cases = int(lines)
                    self.lines+=1
                elif self.lines != 0:
                    self.test_case+=1
                    self.data = lines
                    self.calculate(self.data)

    def calculate(self,data):
        self.temp = ""
        self.num = 0
        self.wrd_dict = {}
        leng = len(data) - 1
        data = data[0:leng]
        if data.isdigit():
            max = 0
            for letter in data:
                if int(letter)> max:
                    max = int(letter)
            max = max+1
            self.result = int(data,max)

        elif data.isalpha() or data.isalnum():
            for characters in data:
                if characters in self.letters_in_wrd:
                    self.temp = ''.join((self.temp,str(self.wrd_dict[characters])))
                else:
                    self.letters_in_wrd.add(characters)
                    self.temp = ''.join((self.temp,str(self.num)))
                    self.wrd_dict[characters] = self.num
                    self.num += 1
            count = 1
            prev = 1
            for i in range(0,len(self.temp)):
                if len(self.temp)>1:
                    if int(self.temp[i]) == 0 and prev == 1:
                        count+=1
                        if int(self.temp[i+1]) != 0:
                            prev = 0
            if count !=1:
                self.md_temp = ''.join([self.temp[x:x+count][::-1] for x in range(0,len(self.temp),len(self.temp))])
                self.md_temp = ''.join((self.md_temp,self.temp[count:]))

                max = 0
                for n in self.md_temp:
                    if int(n) > max:
                        max = int(n)

                max = max+1
                self.result = int(self.md_temp,max)
            elif count == 1:
                self.result = int(1)
        print "Case #{0}: {1}\n".format(self.test_case,self.result)
        with open(r"C:\Users\ADMIN\Desktop\Output123.out", "a+") as result:
            result.write("Case #{0}: {1}\n".format(self.test_case, self.result))
        self.letters_in_wrd.clear()


if __name__ == '__main__':
    hey = alien()
    hey.start("C:\Users\ADMIN\Downloads\A-small-practice (2).in")

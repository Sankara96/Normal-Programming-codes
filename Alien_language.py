class Alien_language(object):
    def __init__(self):
        self.dict_words = {}
        self.no_letters = 0
        self.no_test_cases = 0
        self.case = 1
        self.words = {}
        self.words_words = []
        self.no_words = 0
        self.lines = 1
        self.count = 0
        self.word_num = 0
        self.start_stop = 0
        self.same_count = 0
        self.dict = {}
    def start(self,file_input):
        file = open(file_input,'r')

        for lines in file:
            #print lines
            if self.lines == 1:
                #print lines
                temp = lines.split()
                #print temp
                self.no_letters = int(temp[0])
                #print self.no_letters
                for i in range(self.no_letters):
                    self.words_words.append([])
                #print self.words_words
                self.no_words = int(temp[1])
                #print self.no_words
                self.no_test_cases = int(temp[2])
                #print self.no_test_cases
                self.lines+=1
            elif self.lines == 2:
                self.words[str(lines)] = 0
                #print self.words
                if self.count < self.no_words:
                    self.count+=1
                    #print self.count
                    #print self.lines
                if self.count == self.no_words:
                    self.lines = 3
                    self.count = 0

            elif self.lines == 3:

                if self.case <= self.no_test_cases+1:

                    for letters in lines:
                        #print letters
                        #print self.start_stop
                        if letters == "(":
                            self.start_stop = 1
                        elif letters == ")":
                            self.start_stop = 0
                            self.word_num+=1
                            #print self.word_num
                        elif self.word_num == self.no_letters:
                            self.check()
                            break
                        elif self.start_stop == 1:
                            self.words_words[self.word_num].append(letters)
                            #print self.words_words
                        elif self.start_stop == 0:
                            self.words_words[self.word_num].append(letters)
                            #print self.words_words
                            self.word_num += 1

                else:
                    break
    def check(self):
        temp_id = 0
        self.total_num = 1
        self.sample_string = ""
        self.temp_string = ""
        for i in range(len(self.words_words)):
            self.total_num = self.total_num*len(self.words_words[i])

        if self.total_num == 1:
            self.total_num = self.total_num*3
        #print str(self.total_num) + "Total_num"
        for num in range(self.no_letters):
            self.dict[num] = 0
        for i in range(len(self.words_words)):



        if self.sample_string+"\n" in self.words :
            if self.words[self.sample_string+"\n"] == 0:
                self.same_count += 1
                self.sample_string = ""

        self.lines = 3
        print 'Case #{0}: {1}'.format(self.case,self.count)
        with open(r"C:\Users\ADMIN\Desktop\Output.out","a") as result:
            result.write("Case #{0}: {1}\n".format(self.case,self.count))
        self.case+=1
        for i in range(self.no_letters):
           del self.words_words[i][:]
        self.word_num = 0
        self.total_num = 1
        self.count = 0
if __name__ == '__main__':
    alien = Alien_language()
    alien.start(r'C:\Users\ADMIN\Downloads\A-small-practice.in')
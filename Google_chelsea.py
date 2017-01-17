import  fractions
class Chelsea(object):

    def __init__(self):
        self.lines = 1
        self.no_test_cases = 0
        self.no_roads = 0
        self.no_cities = 0
        self.no_question = 0
        self.pair = 1
        self.no_pairs = 0
        self.path ={}
        self.pair_value = []
        self.answers = []
        self.question = 0
        self.starting_city = "1"
        self.start_availability = 1
    def start(self,file):
        input_file = open(file, "r")

        for lines in input_file:
            if self.lines == 1:
                self.no_test_cases = int(lines)
                self.lines = 2
            elif self.lines == 2:
                temp = lines.split()
                self.no_cities = int(temp[0])
                self.no_roads = int(temp[1])
                self.no_question = int(temp[2])
                self.lines = 3
            elif self.lines == 3:
                if self.pair == 1:
                    temp1 = lines.split()
                    if temp1[0] in self.path:
                        if temp1[1] in self.path[temp1[0]]:
                            self.path[temp1[0]][temp1[1]] =[]
                            self.pair = 2
                            self.pair_value = temp1
                        else:
                            self.path[temp1[0]][temp1[1]] = []
                            self.pair = 2
                            self.pair_value = temp1
                    else:
                        self.path[temp1[0]] = {}
                        if temp1[1] in self.path[temp1[0]]:
                            self.path[temp1[0]][temp1[1]] = []
                            self.pair = 2
                            self.pair_value = temp1
                        else:
                            self.path[temp1[0]][temp1[1]] = []
                            self.pair = 2
                            self.pair_value = temp1
                elif self.pair == 2:
                    temp2 = lines.split()
                    self.path[self.pair_value[0]][self.pair_value[1]].append(temp2)
                    self.pair = 1
                    self.no_pairs += 1
                    if self.no_pairs >= self.no_roads:
                        self.lines = 4
            elif self.lines == 4:

                temp3 = lines.split()
                self.simulate(temp3[0],temp3[1])
                self.question+=1
                if self.question >=self.no_question:
                    self.lines = 2



    def simulate(self,destination,clock):
        direct_route_availability = 0
        temp = 0
        first = 1
        try:
            if len(self.path[str(self.starting_city)][destination])>1:
                no_paths = len(self.path[str(self.starting_city)][destination])
                direct_route_availability = 1
            elif len(self.path[str(self.starting_city)][destination]) == 1:
                no_paths = 1
                direct_route_availability = 1

        except KeyError:
            try:
                if len(self.path[str(self.starting_city)]) > 0:
                    self.start_availability = 1
                    direct_route_availability = 0
            except KeyError:
                self.start_availability = 0
        if self.start_availability == 1:
            if direct_route_availability == 1:
                if no_paths == 1:
                    if first == 1:
                        temp = int(self.path[self.starting_city][destination][0][int(clock)])
                        first = 0
                    else:
                        if temp>int(self.path[self.starting_city][destination][0][int(clock)]):
                            temp = int(self.path[self.starting_city][destination][0][int(clock)])
                elif no_paths > 1:
                    for i in range(no_paths):
                        if first == 1:
                            temp = int(self.path[self.starting_city][destination][i][int(clock)])
                            first = 0
                        else:
                            if temp > int(self.path[self.starting_city][destination][i][int(clock)]):
                                temp = int(self.path[self.starting_city][destination][i][int(clock)])
            elif direct_route_availability == 0:
                route_available = False
                temp_city = int(self.starting_city)
                prev_city =self.starting_city
                while not(route_available):
                    temp_city+=1
                    if temp_city<=self.no_cities:
                        if str(temp_city) in self.path(prev_city):
                            if str(temp_city)!= destination:
                                if destination in self.path[prev_city][temp_city]:
                                    temp_value = int(self.path[prev_city][destination][0][int(clock)])


if __name__ == '__main__':
    chela = Chelsea()
    chela.start(r"C:\Users\ADMIN\Desktop\input.in")











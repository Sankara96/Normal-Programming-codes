t = raw_input()
p = raw_input().split()
count = 0
length = len(p)
word_dict = {}
word_details = []
j = 0
m = t
end_index = 0
start_index = 0
cost_count = 0
for no in range(length):
    if p[j] in m:
        temp = p[j]
        leng = len(temp)
        i = 0

        for letters_index in range(len(t)):
            if letters_index>=start_index:
                if t[letters_index]==temp[i]:
                    if i == 0:
                        start_index = letters_index
                    i+=1
                    if i ==leng:
                        end_index = letters_index
                        break
        word_details.append(start_index)
        word_details.append(end_index)
        word_dict[p[j]] = word_details
        m = t[start_index:]
        word_details = []
        j+=1
    else:
        j+=1
if len(word_dict)==len(p):
    print 'YES'
    final_count = set([])
    for words in p:
        print '{0} {1} {2}'.format(words,word_dict[words][0], word_dict[words][1]),
    for words in range(len(p)-1):
        lis1 = range(word_dict[p[words]][0],word_dict[p[words]][1]+1)
        lis2 = list(range(word_dict[p[words+1]][0],word_dict[p[words+1]][1]+1))
        for elements in lis1:
            final_count.add(elements)
        for elements in lis2:
            final_count.add(elements)
        temp = list(set(lis1).intersection(lis2))
        cost_count+=len(temp)
    cost_count = cost_count+len(p)-1
    for i in xrange(len(t)):
        if i not in final_count:
            cost_count+=1
    print "\n{0}".format(cost_count)
else:
    print 'NO'
    if len(word_dict)>0:
        for key in word_dict:
            print '{0} {1} {2}'.format(key,word_dict[key][0],word_dict[key][1])
    else:
        print 0
    print 0



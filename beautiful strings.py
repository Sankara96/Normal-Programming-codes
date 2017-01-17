'''string = raw_input()
string_list = []
for letters in string:
    string_list.append(letters)
temp  = string_list
result = set([])
for char1 in xrange(len(string_list)):
    i = [x for x in xrange(len(string_list)) if x!= char1]
    for char2 in i:
        st = ''
        for j in xrange(len(string_list)):
            if j==char1 or j==char2:
                continue
            else:
                st = ''.join((st,string_list[j]))
        result.add(st)

print len(result)
'''
s = raw_input().strip()
number = 1
if s[0] == s[1]:
    groups = 1
else:
    groups = 2
for i in xrange(2, len(s)):
    if s[i] == s[i-1]:
        inc = 1
    else:
        inc = groups
        groups += 1
    if s[i] == s[i-2]:
        inc -= 1
    number += inc
print number
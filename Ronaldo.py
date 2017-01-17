s = raw_input()
s_r = reversed(s)
s = list(s)
s_r = list(s_r)
leng = len(s)
count = 0
l = "linkedin"
for i in xrange(leng/2):
    if s[i]==s_r[i]:
        continue
    else:
        count+=1
        if s[i] in l:
            s_r[i]=s[i]
        elif s_r[i] in l:
            s_r[i] = s_r[i]
print count
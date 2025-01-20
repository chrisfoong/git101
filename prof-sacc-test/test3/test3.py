#Mn-rlnjhmf-hm-otakhb-okzbdr

lst = input().split('|')
#display 1
print(len(lst))

#display 2
maxx = 0
text = ''
word = ''
location = 0
idx = 0

for e in lst:
    e = e.strip()
    for i in e:
        if i != '-':
            text += i
    if len(text) > maxx:
        maxx = len(text)
        word = text
        location = idx
    text = ''
    idx += 1
print(len(word))

#display 3
long = lst[location].split('-')
for e in long:
    e = e.strip()
    print(e[0], end='')
print()
    



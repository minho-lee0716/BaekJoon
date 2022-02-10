import re
word, result = re.split('[<>]', input()), ''
for idx, w in enumerate(word):
    if idx % 2:
        result += '<'+word[idx]+'>'
    else:
        temp = ''
        #print(w)
        for k in word[idx].split(' '):
            if k == '':
                pass
                #temp += ' '
            else:
                temp += ';'+k[::-1]+';'
        result += temp.replace(';;', ' ').replace(';', '')

print(result)

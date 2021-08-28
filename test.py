def solution(n):
    share = n
    remainder = ''
    answer = 0

    while share != 0:
        share = n // 3
        remainder += str(n % 3)
        n = share

    remainder = remainder[::-1]
    for index, element in enumerate(remainder):
        if element != '0':
            answer += (3 ** index) * int(element)

    return answer

import re

def solution(new_id):
    print(new_id)
#    print(new_id.lower())
    temp = re.sub('[^a-z0-9-_.]', '', new_id.lower())
    print(temp)
    temp2 = re.sub('[.]+', '.', temp)
    print(temp2)
#    print(temp)
#    print(type(temp))

#    print(('[^a-z0-9-_.]', '', new_id.lower()).replace('.+', '.'))
#    print(re.sub('.+', '.', re.sub('[^a-z0-9-_.]', '', new_id.lower())))
    new_id = re.sub('.+', '.', re.sub('[^a-z0-9-_.]', '', new_id.lower()))[:15].rstrip('.')
    print(new_id)
    # new_id = 'aaa' if len(new_id) < 2 else
    if new_id == '':
            new_id = 'a'

    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

solution('...!@BaT#*..y.abcdefghijklm')

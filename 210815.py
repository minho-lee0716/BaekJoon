time = int(input())
print(f"게임의 횟수는 {t}회 입니다.")

answer = ''

def shortest(w, k):
    temp_idx = -1
    temp_element = ''

    if len(w) == 1:
        return 1

    for idx, element in enumerate(w):
        if idx == 0:
            temp_idx = idx
            temp_element = element

        if temp_element == element:

    return -1


def longest():
    return 0

for t in range(time):

    w = input()
    k = int(input())

    answer_s = shortest(w, k)


#for t in range(time):
#
#    w = input()
#    k = int(input())
#
#    s_temp = {'idx':-1, 'element':''}
#    s_length = 0
#
#    l_time = {'idx':-1, 'element':''}
#    l_length = 0
#    for idx, element in enumerate(w):
#
#        # When word's length is 1 charactor
#        if len(w) == 1:
#            answer += '-1#'
#            break
#
#        # When first index
#        elif s_temp['idx'] == -1:
#            l_temp['idx'], l_temp['temp'] = idx, element
#            l_temp['idx'], l_temp['temp'] = idx, element
#            continue
#
#        # When over second index

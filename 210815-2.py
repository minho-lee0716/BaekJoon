def solution(s):

    answer = ''
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    l3_word = ['one', 'two', 'six']
    l4_word = ['zero', 'four', 'five', 'nine']
    l5_word = ['three', 'seven', 'eight']

    while len(s) != 0:
        if s[0] in number:
            temp = int(s[0])
            answer += str(temp)
            if len(s) == 1:
                break
            s = s[1:]

        else:
            if s[:3] in l3_word:
                if s[:3] == 'one':
                    answer += '1'
                    s = s[3:]
                elif s[:3] == 'two':
                    answer += '2'
                    s = s[3:]
                elif s[:3] == 'six':
                    answer += '6'
                    s = s[3:]

            elif s[:4] in l4_word:
                if s[:4] == 'zero':
                    answer += '0'
                    s = s[4:]
                elif s[:4] == 'four':
                    answer += '4'
                    s = s[4:]
                elif s[:4] == 'five':
                    answer += '5'
                    s = s[4:]
                elif s[:4] == 'nine':
                    answer += '9'
                    s = s[4:]

            elif s[:5] in l5_word:
                if s[:5] == 'three':
                    answer += '3'
                    s = s[5:]
                elif s[:5] == 'seven':
                    answer += '7'
                    s = s[5:]
                elif s[:5] == 'eight':
                    answer += '8'
                    s = s[5:]

    return int(answer)


num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

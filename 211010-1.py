result = 0

for _ in range(int(input())):
    temp = ['']
    word = input()
    for i, w in enumerate(word):
        if w != temp[-1]:
            if w in temp:
                break
            temp.append(w)

        if len(word) == i+1:
            result += 1

print(result)

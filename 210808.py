x_list = []

for _ in range(100):
    x = input()
    if x == 'Was it a cat I saw?':
        break
    x_list.append(x)


for idx_i, word in enumerate(x_list):

    temp_idx = 0
    return_word = word[0]

    for idx_j, w in enumerate(word):
        if idx_j - (idx_i + 2) == temp_idx:
            temp_idx = idx_j
            return_word += w

    x_list[idx_i] = return_word

for x in x_list:
    print(x)

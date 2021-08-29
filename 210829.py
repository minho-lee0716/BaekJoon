def solution(priorities, location):
    temp_priorities = priorities
    for idx, element in enumerate(priorities):
        if element < max(priorities):
            temp_priorities.append(element)
            temp_priorities = temp_priorities[1:]
            if location == 0:
                location = len(temp_priorities) - 1
            else:
                location -= 1
            continue
        break
    return location + 1

solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)


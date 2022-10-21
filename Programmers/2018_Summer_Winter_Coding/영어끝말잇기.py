def solution(n, words):
    answer = [0, 0]
    last_word = words[0][-1]
    used_word = [words[0]]
    cur = 1
    
    for word in words[1:]:
        if word[0] != last_word or word in used_word:
            return [cur % n +1, cur//n + 1]
            break
        used_word.append(word)
        cur += 1
        last_word = word[-1]

    return answer
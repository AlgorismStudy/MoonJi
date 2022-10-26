def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        tmp = ''
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                tmp += skill_tree[i]
        if skill.startswith(tmp):
            answer += 1
    
    return answer
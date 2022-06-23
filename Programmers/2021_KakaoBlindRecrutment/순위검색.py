def solution(info, query):
    answer = []
    for q in query:
        lan, job, career, etc = q.split(" and ")
        food, score = etc.split()
        count = 0
        for i in info:
            i_lan, i_job, i_career, i_food, i_score = i.split()
            if (lan == "-" or lan == i_lan) and (job == "-" or job == i_job) and (career == "-" or career == i_career) and (food == "-" or food == i_food) and int(score) <= int(i_score):
                count += 1
        answer.append(count)
    return answer
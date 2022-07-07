def is_correct_parenthesis(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True

def solution(p):
    answer = ''
    
    def func(p):
        o, c = 0, 0
        u, v = "", ""
        for i in range(len(p)):
            if p[i] == "(":
                o += 1
            elif p[i] == ")":
                c += 1
            if o != 0 and o == c:
                u, v = p[:i+1], p[i+1:]
                break
        if v != "":
            v = func(v)
        if is_correct_parenthesis(u):
            return u + v
        else:
            u = u[1:-1]
            new_u = ""
            for i in u:
                if i == "(":
                    new_u += ")"
                else:
                    new_u += "("
            u = "(" + new_u + ")"
            return "(" + v + ")" + new_u
        
    answer = func(p)       
        
    return answer
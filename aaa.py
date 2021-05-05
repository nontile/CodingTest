A = "azABaabza"
# str_ = "TacoCat"
def solution(S):
    upp = []
    low = []
    for s in S:
        if s.isupper():
            upp.append(s)
        else:
            low.append(s)

    balance = 0
    for up in upp:
        for lo in low:
            if up.lower() == lo:
                balance += 1
            else: 
                balance -= 1
    if balance == 0:
        return -1
    return balance

print(solution(A))
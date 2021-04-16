

def solution(A):
    dict_ = {}
    for a in A:
        dict_[a] += 1
    print(dict_)
    for k in dict_:
        if dict_[k] % 2 == 1:
            return k

print(solution([9, 3, 9, 3, 9, 7, 9]))
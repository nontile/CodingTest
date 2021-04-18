A = [3, 4, 4, 6, 1, 4, 4]

N = [0] * 5 

N_len = len(N)
# print(N_len)
for i in A:
    if i -1 >= N_len:
        N = [max(N)] * 5
    
    else:
        N[ i -1 ] += 1
    print(N)


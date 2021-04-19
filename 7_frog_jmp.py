# A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

# Count the minimal number of jumps that the small frog must perform to reach its target.


# def sulution(X, Y, D):
#     count = 0
#     jump = True
#     move = X
#     while jump:
#         if move >= Y:
#             jump =False
#             return count
#         else:
#             count += 1
#             move += D

def sulution(X, Y, D):
    count = (Y-X) // D
    if D * count + X >= Y:
        return count
    else:
        return count + 1

print(sulution(10, 85, 30))

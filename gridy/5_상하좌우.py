#  5 * 5 배열 
# RRRUDD
N =5
plan = ['R', 'R', 'R', 'U', 'D', 'D']

x , y = 1, 1
for p in plan:
    # R: x + 1 
    if p == 'R' and y + 1 <= 5:
        y += 1

    # L: x - 1
    if p == 'L' and y - 1 > 0:
        y -= 1

    # U: y + 1
    if p == 'U' and x - 1 > 0:
        x -= 1

    # D: y - 1
    if p == 'D' and x + 1 <= 5:
        x += 1

print( x, y)

s = "K1KA5CB7"
strs = []
nums = []
for i in s:
    if i.isnumeric():
        
        nums.append(int(i))
    else:
        strs.append(i)

rs = "".join(strs) + str(sum(nums))
print(rs )
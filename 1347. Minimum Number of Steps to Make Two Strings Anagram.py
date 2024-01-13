def minSteps(s, t):
    min_steps = 0
    if s == t:
        return 0
    set_s = set(s)
    for i in set_s:
        if t.count(i) < s.count(i):
            min_steps += s.count(i) - t.count(i)
            #print(i, min_steps)
            
    return min_steps

output = minSteps("aaa", "bbb")
print(output)

#find the difference in frequencies of letters in s and t and add it to min_steps      
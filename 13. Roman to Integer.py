def romanToInt(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    value = 0
    for i in range(len(s)):
        if i < len(s) -1 and roman[s[i]]<roman[s[i+1]]: #only the romans with next greater value is subtracted (ex: IV "V" is greater than "I")
            value -= roman[s[i]]
        else:
            value += roman[s[i]] #add roman values
    return value

output = romanToInt("IV")
print(output)

def closeStrings(word1, word2):
    if word1 == word2 :
        return True
    if len(word1) != len(word2):
        return False
    a = {i: word1.count(i) for i in set(word1)}
    b = {i: word2.count(i) for i in set(word2)}
    for i in a:
        if i not in b:
            return False
    a = list(a.values())
    b = list(b.values())
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True
    
output = closeStrings("a", "aa")
print(output)

#find frequency of each letter sort them and check if they are equal in both strings

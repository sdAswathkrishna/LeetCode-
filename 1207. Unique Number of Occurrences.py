def uniqueOccurrences(arr):
    mapper = {} # value, count
    
    for n in arr:
        mapper[n] = 1 + mapper.get(n, 0)
        
    return len(set(mapper.values())) == len(mapper.values())

output = uniqueOccurrences([1,1,1,2,2,3])
print(output)

# use hashmap and count frequencies check the length of set of hashmap values and len hashmap
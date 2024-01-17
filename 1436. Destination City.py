def destCity(paths):
    if len(paths)==1:
        return paths[0][1]
    for i in range(len(paths)):
        path = paths[:i]+paths[i+1:]
        #print(path)
        for j in path:
            #print(paths[i][1])
            #print(j)
            if paths[i][1]!=j[0]:
                destination = True
                continue
            else:
                destination = False
                break
        if destination:
            return paths[i][1]
        
x = destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
print(x)

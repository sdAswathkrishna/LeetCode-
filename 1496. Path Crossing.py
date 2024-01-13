def isPathCrossing(path):
        visited = [(0,0)]
        x = 0
        y = 0
        for i in path:
            if i == 'N':
                y += 1
            if i == 'S':
                y -= 1
            if i == 'E':
                x += 1
            if i == 'W':
                x -= 1
            print(x,y)
            if (x,y) not in visited:
                visited.append((x,y))
            else:
                return True
            print(visited)
        return False
    
X = isPathCrossing("NESWW")
print(X)

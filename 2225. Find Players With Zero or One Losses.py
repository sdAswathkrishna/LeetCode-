def findWinners(matches):
    w_records = {}
    l_records = {}
    for winner, loser in matches:
        w_records[winner] = 1 + w_records.get(winner, 0)
        l_records[loser] = 1 + l_records.get(loser, 0)
        
    one_lost = []
    for player in l_records:
        if l_records[player] == 1:
            one_lost.append(player)
            
    no_lost = []
    for player in w_records:
        if l_records.get(player, 0) == 0:
            no_lost.append(player)
            
    return [sorted(no_lost), sorted(one_lost)]

output = findWinners[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(output)

#count the no of loses for each player two hashmap approach
def solution(players, callings):
    answer = []
    dic = {players[i]: i for i in range(len(players))}
    for i in callings:
        pre, now = dic[i] -1, dic[i]
        dic[players[pre]] = now
        dic[players[now]] = pre
        players[pre], players[now] = players[now], players[pre]
    return players
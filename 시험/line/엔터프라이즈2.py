import sys
sys.stdin = open('엔터프라이즈2.txt', 'r')

N = int(input())
team_dict = {}
for _ in range(N*(N-1)):
    team1, score1, team2, score2 = map(str, input().split())
    score1 = int(score1)
    score2 = int(score2)
    if score1 > score2:
        if team1 in team_dict.keys():
            team_dict[team1] = [team_dict[team1][0]+1, team_dict[team1][1] + score1 - score2]
        else:
            team_dict[team1] = [1, score1 - score2]
        if team2 in team_dict.keys():
            team_dict[team2] = [team_dict[team2][0], team_dict[team2][1] + score2 - score1]
        else:
            team_dict[team2] = [0, score2 - score1]
    elif score2 > score1:
        if team2 in team_dict.keys():
            team_dict[team2] = [team_dict[team2][0]+1, team_dict[team2][1] + score2 - score1]
        else:
            team_dict[team2] = [1, score2 - score1]
        if team1 in team_dict.keys():
            team_dict[team1] = [team_dict[team1][0], team_dict[team1][1] + score1 - score2]
        else:
            team_dict[team1] = [0, score1 - score2]
team_dict = sorted(team_dict.keys())

result = []
for i in team_dict:
    result.append([i, team_dict[i][0], team_dict[i][1]])


result = sorted(result, key= lambda x: (x[1], x[2], x[0]), reverse=True)

for answer in result:
    print(answer[0], answer[1], answer[2])
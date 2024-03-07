LEAGUE_RESULTS = [
    (('Liverpool', 2), ('Tranmere', 1)),
    (('Liverpool', 0), ('Ajax', 0)),
    (('Tranmere', 1), ('Ajax', 0)),
    (('Tranmere', 1), ('Everton', 4)),
    (('Liverpool', 5), ('Everton', 2))
]

def print_results():
    for home, away in LEAGUE_RESULTS:
        home_team, home_score = home
        away_team, away_score = away
        if home_score > away_score:
            print(f'{home_team} wins!')
        elif home_score < away_score:
            print(f'{away_team} wins!')
        else:
            print('Draw. :(')

def print_league_table():
    league_table = {}
    for home, away in LEAGUE_RESULTS:
        home_team, home_score = home
        away_team, away_score = away
        if home_score > away_score:
            if home_team not in league_table:
                league_table[home_team] = 0
            league_table[home_team] += 3
        elif home_score < away_score:
            if away_team not in league_table:
                league_table[away_team] = 0
            league_table[away_team] += 3
        else:
            if home_team not in league_table:
                league_table[home_team] = 0
            league_table[home_team] += 1
            if away_team not in league_table:
                league_table[away_team] = 0
            league_table[away_team] += 1

    items = [(team, points) for team, points in league_table.items()]
    items = sorted(items, key=lambda x: x[1], reverse=True)
    print(items)

if __name__ == '__main__':
    print_league_table()

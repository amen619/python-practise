teams = [ "Liverpool", "Chelsea", "Barcelona", "Real Madrid"]

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print (str(home_team) + " vs " + str(away_team))
    print()
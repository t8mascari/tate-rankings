from cfbd_setup import games_api

# Pull Week 1 games
games = games_api.get_games(year=2024, week=1)

# Print summary
for g in games:
    print(f"{g.week} - {g.home_team} {g.home_points} vs {g.away_team} {g.away_points}")

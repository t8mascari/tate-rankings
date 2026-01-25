import cfbd
from team import Team

def test():
    configuration = cfbd.Configuration(
        access_token = 'h1MAIiVr9gx/02m9CbWjbQp9kPld43ZrzGfGH9MWLWegl9dqq3pCZQqRWmBZc1/W'
    )

    with cfbd.ApiClient(configuration) as api_client:
        api_instance = cfbd.TeamsApi(api_client)
        #games = api_instance.get_games(year=2025)
        teams = api_instance.get_teams()
        fbs_teams = [team for team in teams if team.classification == 'fbs']
        print(len(fbs_teams))
        teams_list = []
        for team in fbs_teams:
            print(team)
            t = Team(name=team.school, short=team.abbreviation, conference=team.conference, year_founded=team.location.construction_year)
            teams_list.append(t)
        for team in teams_list:
            print(team.name, team.year_founded)
    return teams_list

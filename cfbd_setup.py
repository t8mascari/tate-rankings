import os
import cfbd

CFBD_API_KEY = "h1MAIiVr9gx/02m9CbWjbQp9kPld43ZrzGfGH9MWLWegl9dqq3pCZQqRWmBZc1/W"

config = cfbd.Configuration(
    api_key={
        "Authorization": CFBD_API_KEY
    },
    api_key_prefix={
        "Authorization": "BEARER"
    }
)

api_client = cfbd.ApiClient(config)

games_api = cfbd.GamesApi(api_client)
teams_api = cfbd.TeamsApi(api_client)
metrics_api = cfbd.MetricsApi(api_client)
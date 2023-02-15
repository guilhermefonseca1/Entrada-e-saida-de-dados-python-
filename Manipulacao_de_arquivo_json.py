import json

with open("video_games.json") as video_games_file:
    print(json.load(video_games_file)[3]["Title"])
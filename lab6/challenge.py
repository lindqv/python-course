from challenge_data import players_raw_data

players = [
    {
        "name": player.get("name", "").strip().title(),
        "team": player.get("team", "").strip().title(),
        "country": player.get("country", "").strip().title(),
        "score": player.get("score", 0),
        "matches_played": player.get("matches_played", 0),
        "wins": player.get("wins", 0),
        "is_active": player.get("is_active", False),
    }
    for player in players_raw_data]

active_players = [player for player in players if player["is_active"]]
three_wins = [player for player in players if player["wins"] >= 3]
score_threshold = 80
score_above_threshold = [player for player in players if player["score"] > score_threshold]
greek_players = [player for player in players if player["country"] == "Greece"]

unique_countries = {player["country"] for player in players}
unique_teams = {player["team"] for player in players}
names_to_scores = {player["name"]: player["score"] for player in players}
names_to_wins = {player["name"]: player["wins"] for player in players}
divide_by_threshold = {player["name"]: player for player in players if player["score"] > score_threshold}


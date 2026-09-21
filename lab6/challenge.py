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

print(players)
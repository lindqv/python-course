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
players_ranked_by_score = sorted(players, key=lambda player: player["score"], reverse=True)
players_ranked_by_wins = sorted(players, key=lambda player: player["wins"], reverse=True)
undefeated_players = [player for player in players if player["wins"] == player["matches_played"]]

total_score_per_team = dict()
for team in unique_teams:
    total_score_per_team[team] = sum([player["score"] for player in players if player["team"] == team])

def create_final_report(players: list[dict]) -> dict:
    final_report = dict()
    final_report["Total number of players"] = len(players)
    final_report["Number of active players"] = active_players
    final_report["Unique teams"] = unique_teams
    final_report["Unique countries"] = unique_countries
    final_report["Players above score threshold"] = score_above_threshold
    final_report["Players ranked by score"] = players_ranked_by_score
    final_report["Players ranked by wins"] = players_ranked_by_wins
    final_report["Undefeated players"] = undefeated_players
    final_report["Total scores per team"] = total_score_per_team
    print(type(total_score_per_team))

    return final_report

def print_final_report(report: dict):
    for label, value in report.items():
        print(f"{label}: ")
        try:
            for k, v in value.items():
                print(k, v)
        except:
            try:
                for v in value:
                    print(v)
            except TypeError:
                print(value)
        print("\n")
        

report = create_final_report(players)
print_final_report(report)
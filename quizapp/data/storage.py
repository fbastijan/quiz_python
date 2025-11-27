import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "questions.json"
PLAYER_FILE =Path(__file__).parent / "players.json"
def load_questions():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["questions"]


def add_new_question(question):
     with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        data["questions"].append(question)
     with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_player_and_score(player_name, score):
    with open(PLAYER_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Find and update or create player
    player = next((p for p in data["players"] if p["name"] == player_name), None)
    
    if player:
        player["score"] +=  score
    else:
        data["players"].append({"name": player_name, "score": score})
    
    with open(PLAYER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def load_players_and_scores():
    with open(PLAYER_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["players"]
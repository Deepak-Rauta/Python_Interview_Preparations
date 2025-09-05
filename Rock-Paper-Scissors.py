# rps_ai.py
import random
import collections

VALID = {"rock": "r", "r": "rock",
         "paper": "p", "p": "paper",
         "scissors": "s", "s": "scissors"}

BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def normalize_move(raw: str):
    raw = raw.strip().lower()
    if raw in VALID:
        # if user gave short form like 'r' return full name
        return VALID[raw] if raw in ("r", "p", "s") else raw
    return None

def computer_move_ai(player_history: list):
    """
    Simple AI:
    - If no history: pick uniformly at random.
    - Otherwise predict player's next move as the most frequent move they've used,
      then play the move that beats that prediction.
    """
    if not player_history:
        return random.choice(list(BEATS.keys()))
    freq = collections.Counter(player_history)
    predicted_player = freq.most_common(1)[0][0]   # most frequent player move
    # computer should choose the move that beats the predicted player move
    for move, beats in BEATS.items():
        if beats == predicted_player:
            return move
    return random.choice(list(BEATS.keys()))

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    if BEATS[player] == computer:
        return "player"
    return "computer"

def print_round_result(player, computer, result):
    print(f"\nYou -> {player.capitalize()}   |   Computer -> {computer.capitalize()}")
    if result == "tie":
        print("Result: It's a tie! 🤝")
    elif result == "player":
        print("Result: You win this round! 🎉")
    else:
        print("Result: Computer wins this round! 🤖")

def play_round(player_history):
    while True:
        raw = input("Your move (rock/r, paper/p, scissors/s) or 'quit' to stop: ").strip()
        if raw.lower() in ("quit", "q", "exit"):
            return None  # signal to end game
        player = normalize_move(raw)
        if player is None:
            print("Invalid input. Try 'rock', 'paper', or 'scissors' (or r/p/s).")
            continue
        comp = computer_move_ai(player_history)
        result = decide_winner(player, comp)
        return player, comp, result

def main():
    print("Welcome to Rock-Paper-Scissors with AI ✊🖐️✌️")
    print("The AI learns your most frequent moves and tries to counter them.\n")

    rounds_played = 0
    scores = {"player": 0, "computer": 0, "tie": 0}
    player_history = []  # track player's moves

    # ask if user wants fixed rounds or infinite
    mode = input("Play best-of [press Enter for infinite] or enter an odd number (e.g., 3,5,7) for best-of: ").strip()
    best_of = None
    if mode:
        try:
            n = int(mode)
            if n % 2 == 1 and n > 0:
                best_of = n
                print(f"Playing best of {best_of} (first to {(best_of//2)+1} wins).")
            else:
                print("Ignoring invalid number; starting infinite mode.")
        except ValueError:
            print("Invalid input; starting infinite mode.")

    while True:
        outcome = play_round(player_history)
        if outcome is None:
            print("\nQuitting the game. Thanks for playing!")
            break

        player, comp, result = outcome
        rounds_played += 1
        player_history.append(player)
        scores[result] += 1

        print_round_result(player, comp, result)
        print(f"Score -> You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['tie']}")
        print(f"Rounds played: {rounds_played}\n")

        # if best_of mode, check for winner
        if best_of:
            needed = (best_of // 2) + 1
            if scores["player"] >= needed:
                print(f"You reached {needed} wins — YOU WIN THE MATCH! 🏆")
                break
            if scores["computer"] >= needed:
                print(f"Computer reached {needed} wins — COMPUTER WINS THE MATCH! 🤖")
                break

    # final stats
    total = scores["player"] + scores["computer"] + scores["tie"]
    if total:
        win_rate = scores["player"] / total * 100
        print("\n=== Final Stats ===")
        print(f"Rounds: {total}")
        print(f"You won: {scores['player']} times")
        print(f"Computer won: {scores['computer']} times")
        print(f"Ties: {scores['tie']}")
        print(f"Your overall win rate: {win_rate:.1f}%")
        print("Player move frequencies:", dict(collections.Counter(player_history)))
    print("Goodbye!")

if __name__ == "__main__":
    main()

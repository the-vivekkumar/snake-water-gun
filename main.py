import random

def game_win(player, computer):
    if player == computer:
        return None
    if player == "snake":
        return True if computer == "water" else False
    elif player == "water":
        return True if computer == "gun" else False
    elif player == "gun":
        return True if computer == "snake" else False

print("Snake, Water, Gun Game!")
choices = ["snake", "water", "gun"]

player_score = 0
computer_score = 0

while True:
    player_choice = input("Choose Snake, Water, or Gun (or 'quit' to stop): ").lower()
    if player_choice == "quit":
        print("Final Scores:")
        print(f"You: {player_score} | Computer: {computer_score}")
        break
    
    if player_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = game_win(player_choice, computer_choice)

    if result is None:
        print("It's a draw!")
    elif result:
        print("You win this round! 🎉")
        player_score += 1
    else:
        print("Computer wins this round! 💻")
        computer_score += 1

    print(f"Score => You: {player_score} | Computer: {computer_score}")
    print("-" * 30)

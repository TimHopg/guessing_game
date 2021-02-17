from random import randrange

guess = ""
guess_count = 0
guess_limit = 3
game_over = False
clear = "\n" * 100
secret_number = "1000"
low_word: str = "low"
player_name = ["A", "B", "C", "D"]
player_1 = ""
player_2 = ""
player_3 = ""
player_4 = ""
players = "100"
game_type = ""
play = 1

player_guess = [200, 200, 300, 400]
player_1_guess = "200"
player_2_guess = "200"
player_3_guess = "200"
player_4_guess = "200"


chances_text = "! You have " + str(3 - guess_count) + " guesses remaining"
last_chance_text = "Incorrect, that's too "

while game_type not in ["1", "2"]:
    game_type = input("Choose game type\n\n"
                      "1 - Classic (1-2 players)\n"
                      "Computer or player one selects a number between 1-10, the other guesses\n\n"
                      "2 - Multiplayer (2-4 players)\n"
                      "Up to 4 players take it in turns to guess a number between 1-100\n\n"
                      "Choose game: ")

    print()

    if game_type == str(2):
        while int(players) not in range(2, 5):
            players = int(input("Choose 2 to 4 players: "))
            print()
        player_1 = input("Player 1, enter name: ")
        player_2 = input("Player 2, enter name: ")
        if int(players) >= 3:
            player_3 = input("Player 3, enter name: ")
        if int(players) >= 4:
            player_4 = input("Player 4, enter name: ")
        print()
        secret_number = randrange(1, 101)
        print("The computer has chosen a number between 1-100")
        print()

        if secret_number in player_guess:
            game_over = True

        while secret_number != any(player_guess):

            player_guess[0] = int(input(player_1 + ", guess a number between 1-100: "))
            if 0 < player_guess[0] < secret_number:
                low_word = "low"
            elif 101 > player_guess[0] > secret_number:
                low_word = "high"
            if player_guess[0] != secret_number:
                print("Too " + low_word + ".")
            if secret_number in player_guess:
                game_over = True
                break
            player_guess[1] = int(input(player_2 + ", guess a number between 1-100: "))
            if 0 < player_guess[1] < secret_number:
                low_word = "low"
            elif 101 > player_guess[1] > secret_number:
                low_word = "high"
            if player_guess[1] != secret_number:
                print("Too " + low_word + ".")
            if secret_number in player_guess:
                game_over = True
                break
            if players >= 3:
                player_guess[2] = int(input(player_3 + ", guess a number between 1-100: "))
                if 0 < player_guess[2] < secret_number:
                    low_word = "low"
                elif 101 > player_guess[2] > secret_number:
                    low_word = "high"
                if player_guess[2] != secret_number:
                    print("Too " + low_word + ".")
                if secret_number in player_guess:
                    game_over = True
                    break
            if players >= 4:
                player_guess[3] = int(input(player_4 + ", guess a number between 1-100: "))
                if 0 < player_guess[3] < secret_number:
                    low_word = "low"
                elif 101 > player_guess[3] > secret_number:
                    low_word = "high"
                if player_guess[3] != secret_number:
                    print("Too " + low_word + ".")
                if secret_number in player_guess:
                    game_over = True
                    break
        print()
        if int(player_guess[0]) == secret_number:
            print("Congratulations! " + player_1 + " is the winner!")
        if int(player_guess[1]) == secret_number:
            print("Congratulations! " + player_2 + " is the winner!")
        if int(player_guess[2]) == secret_number:
            print("Congratulations! " + player_3 + " is the winner!")
        if int(player_guess[3]) == secret_number:
            print("Congratulations! " + player_4 + " is the winner!")

    elif "1" == game_type:
        while players not in ["1", "2"]:
            players = input("Choose 1 or 2 players: ")
            if players == "2":
                print()
                player_name[0] = input("Player 1, enter name: ")
                player_name[1] = input("Player 2, enter name: ")
                two_player = "Player 2. "
            elif players == "1":
                player_name[0] = input("Enter name: ")
                two_player = ""

            print()

            if players == "1":

                secret_number = randrange(1, 11)

            elif players == "2":
                while int(secret_number) not in range(1, 11):
                    secret_number = int(input(player_name[0] + ", choose a number between 1 and 10 ("
                                              + player_name[1] + " look away): "))

                print(clear)
                # clears console

        print(player_name[1] + ", guess a number between 1 and 10")

        while guess != secret_number and not game_over:
            if guess_count < guess_limit:
                guess = int(input("Enter guess: "))
                guess_count += 1
                if guess < secret_number:
                    low_word = "low"
                    if guess_count <= 1:
                        print()
                        print("Too " + low_word + chances_text)
                    elif guess_count == 2:
                        print(last_chance_text + low_word + ". Last chance")
                elif guess > secret_number:
                    low_word = "high"
                    if guess_count <= 1:
                        print("Too " + low_word + chances_text)
                    elif guess_count == 2:
                        print(last_chance_text + low_word + ". Last chance")
            else:
                game_over = True

        print()

        if game_over:
            print("GAME OVER! Out of guesses\nThe correct number was " + str(secret_number))
            if players == "1":
                print("Computer wins!")
            else:
                print(player_name[0] + " wins!")
        else:
            print("Correct!")
            if players == "1":
                print("You win!")
            else:
                print(player_name[1] + " wins!")

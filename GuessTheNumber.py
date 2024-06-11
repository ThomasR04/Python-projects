import random
def start():
    logo = """
  ____  __ __    ___   _____  _____     ______  __ __    ___      ____   __ __  ___ ___  ____     ___  ____  
 /    ||  |  |  /  _] / ___/ / ___/    |      ||  |  |  /  _]    |    \ |  |  ||   |   ||    \   /  _]|    \ 
|   __||  |  | /  [_ (   \_ (   \_     |      ||  |  | /  [_     |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )
|  |  ||  |  ||    _] \__  | \__  |    |_|  |_||  _  ||    _]    |  |  ||  |  ||  \_/  ||     ||    _]|    / 
|  |_ ||  :  ||   [_  /  \ | /  \ |      |  |  |  |  ||   [_     |  |  ||  :  ||   |   ||  O  ||   [_ |    \ 
|     ||     ||     | \    | \    |      |  |  |  |  ||     |    |  |  ||     ||   |   ||     ||     ||  .  \
|___,_| \__,_||_____|  \___|  \___|      |__|  |__|__||_____|    |__|__| \__,_||___|___||_____||_____||__|\_|

"""
    print("Welcome to the number guessing game")
    print(logo)
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        Hard()

      
def Generate_Random():
   rand_num = random.randint(1, 101)
   return rand_num


def process_guess(guess, rand_num):
    if guess < rand_num:
        return "Too low\nGuess again"
    elif guess > rand_num:
        return "Too high\nGuess again"
    else:
        return f"You got it! The answer was {guess}"


def Hard():
 rand_num = Generate_Random()
 for times in range(5, -1, -1):
    if times == 0:
       print(f"You have {times} attempts remaining Hard luck")
       print(f"The number was {rand_num}")
       play_again()
       break
    print(f"You have {times} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    Correct = process_guess(guess, rand_num)
    if Correct == "Too low\nGuess again":
     print(Correct)
    elif Correct == "Too high\nGuess again":
      print(Correct)
    else:
      print(Correct)
      play_again()
      break


def easy():
  rand_num = Generate_Random()
  for times in range(10, -1, -1):
    if times == 0:
       print(f"You have {times} attempts remaining Hard luck")
       print(f"The number was {rand_num}")
       play_again()
       break
    print(f"You have {times} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    Correct = process_guess(guess, rand_num)
    if Correct == "Too low\nGuess again":
     print(Correct)
    elif Correct == "Too high\nGuess again":
      print(Correct)
    else:
      print(Correct)
      play_again()
      break
          


def play_again():
   play = input("Do you want to play again type 'y' to play or 'n' to not ").lower()
   if play == "y":
      start()
      



start()


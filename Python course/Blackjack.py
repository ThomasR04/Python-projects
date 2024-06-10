import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def blackjack():
     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
     dealercardselection = []
     dealercards = random.randint(1,6)
     print(dealercards)
     usercard = []
     start = input("Would you like to play a game of blackjack 'y' for yes or 'n' for no").lower()
     total = 0
     if start == "y":
      print(logo)
      userscards = random.choice(cards)
      usercard.extend([userscards])
      for i in range(dealercards):
        dealerschoice = random.choice(cards)
        dealersSum = 0
        if dealerschoice == cards[0] and dealersSum + cards[0] > 21:
          cards[0] = 1
          dealercardselection = dealercardselection + [dealerschoice]
          dealersSum = sum(dealercardselection)
          cards[0] = 11
      dealercardselection = dealercardselection + [dealerschoice]
      dealersSum = sum(dealercardselection)
     new_card = True 
     while new_card == True:
       userscards = random.choice(cards)
       if userscards == cards[0] and total + cards[0] > 21:
         cards[0] = 1
         usercard.extend([userscards])
         total = sum(usercard)
         cards[0] = 11
       usercard.extend([userscards])
       total = sum(usercard)
       print(f"Your cards {usercard}, current score: {total}")
       print(f"Computers first card is {dealercardselection[0]}")
       pickup = input(f"Type 'y' to pick up another card or 'n' to pass").lower()
  
       if pickup == "n":
        if total == 21 or total > dealersSum and dealersSum > 21:
          print(f"Your final hand {usercard} , final score {total}")
          total = sum(dealercardselection)
          print(f"Computers final hand {dealercardselection} final score {total}")
          print("You win")
          blackjack()
        elif dealersSum > total and dealersSum < 22:
          print(f"Your final hand {usercard} , final score {total}")
          total = sum(dealercardselection)
          print(f"Computers final hand {dealercardselection} final score {total}")
          print("you lose")
          blackjack()
        else :
          print(f"Your final hand {usercard} , final score {total}")
          total = sum(dealercardselection)
          print(f"Computers final hand {dealercardselection} final score {total}")
          print("its a draw")
          blackjack()
       elif pickup == "y":
         new_card = True






blackjack()
   







    


    









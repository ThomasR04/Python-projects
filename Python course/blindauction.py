logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program")
bidders = {}
Morebids = ""
shouldcontinue = True
while shouldcontinue == True:
 name = input("What is your name? ")
 bid = int(input("What's your bid? : £"))
 bidders[name] = bid
 Morebids = input("Are there any other bidders? Type 'yes' or 'no'").lower()
 if Morebids == "yes":
  shouldcontinue = True
 else:
  shouldcontinue = False
winner = ""
bidwin = 0
for bids in bidders:
 bid_amount = bidders[bids]
 if bid_amount > bidwin:
  bidwin = bid_amount
  winner = bids
print(f"The winner is {winner} With a bid of £{bidwin}")
 



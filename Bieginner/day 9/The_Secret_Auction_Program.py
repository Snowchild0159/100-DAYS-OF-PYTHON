from clear_screen import clear
logo = '''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
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
bidders_dictionary = {}

name = input("what is your name ? ")
bid = int(input("what is your bid? $"))

bidders_dictionary[name] = bid

    
is_there_another_bidders = input('is there another bidders ? "yes" or "no" ').lower()

while is_there_another_bidders == "yes" :
        clear()

        name = input("what is your name? ")
        bid = int(input("what is your bid? $"))

        bidders_dictionary[name] = bid

        is_there_another_bidders = input('is there another bidder? "yes" or "no": ').lower()
            
else :
    winner = ""
    highest_bid = 0
    for bidder in bidders_dictionary :
      bid = bidders_dictionary[bidder]
      if bid > highest_bid:
         highest_bid = bid
         winner = bidder

     

    print(f"the winner is {winner} with a bid of {highest_bid}$") 




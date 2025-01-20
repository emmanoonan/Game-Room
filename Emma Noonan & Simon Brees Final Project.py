import random as rand
import time
from random import *

#We were originally going to have another function to have a scoring system that saves the game even if you close the shell but it never ended up working,
# some of the code is a little inefficient due
# to the fact that the initial idea didn't work. 

#This function was originally meant to handle adding points to peoples accounts when they were being saved between instances but its utility is
# mostly lost now, it still works though so
# we are still using it. It now just adds the highlow score to the players balance
def balanceCheck(balance,payout,autoBet,betAmount,cg):
    balance = float(payout) + float(balance)
    for i in range(3):
        print(".",end="")
        time.sleep(0.2)
    print()
    print("Your new balance is", str(balance) + ".")
    print("----------------------------------------------------------------------------")
    print()

    #asks if you want to play again
    nxt = str(input("do you want to play again? >> "))
    print()

    #if you said yes then it plays agian
    if nxt[0].lower() == "y":
        if cg == "hl":
            highLow(balance, autoBet, betAmount)
            
    #if not, it sends you back to the game menu
    else:
        play(balance, autoBet, betAmount)


#this is the highlow game, it uses Random to generate 2 random number, stores them then displays one
def highLow(balance, autoBet, betAmount):
    currentBet = betAmount
    if autoBet[0].lower() == "n":
        currentBet = int(input("How much do you want to bet? >> "))
    #random number generation
    k = rand.randint(1,100)
    l = rand.randint(1,100)

    phrase = "is " + str(l) + " higher, lower, or equal to the mystery number? >> "
    p = str(input(phrase))
    #if the guess was higher then it sends you to the higher function and so on
    if p[0].lower() == "h":
        higher(k,l,currentBet,balance,autoBet,betAmount)
    elif p[0].lower() == "l":
        lower(k,l,currentBet,balance,autoBet,betAmount)
    elif p[0].lower() == "e":
        equal(k,l,currentBet,balance,autoBet,betAmount)
    else:
        #if you input an invalid answer then you lose your points
        print("sorry, thats not an option")
    balance -= betAmount
    balance = roundBal(balance)
    play(balance,autoBet,betAmount)
    
#if your highlow answer was high it takes you here
def higher(k,l,cbet,balance,autoBet,betAmount):
    
    #if you were right 
    if l > k:
        print("You Win,",end=" ")
        print("the mystery number was", k)

        #sends you to the payout function
        payoutHL(cbet,balance,"h",l,autoBet,betAmount)
        
    #if you were wrong 
    elif l<=k:
        print("You Lose,",end=" ")
        print("the mystery number was", k)
        
        balance = float(balance) - float(cbet)
        print("your new balance is " + str(balance) + ".")
        
#if your highlow answer was low it takes you here
def lower(k,l,cbet,balance,autoBet,betAmount):

    #if you were right
    if l < k:
        print("You Win,",end=" ")
        print("the mystery number was", k)

        #sends you to the payout function
        payoutHL(cbet,balance,"l",l,autoBet,betAmount)

    #if you were wrong
    elif l>=k:
        print("You Lose,",end=" ")
        print("the mystery number was", k)
        
        balance = float(balance) - float(cbet)
        print("your new balance is " + str(balance) + ".")

#if your highlow answer was equal it takes you here
def equal(k,l,cbet,balance,autoBet,betAmount):

    #if you were right
    if k == l:
        print("You Win,",end=" ")
        print("the mystery number was", k)

        #sends you to the payout function
        payoutHL(cbet,balance,"e",l,autoBet,betAmount)

    #if you were wrong
    elif k != l:
        print("You Lose,",end=" ")
        print("the mystery number was", k)

        balance = float(balance) - float(cbet)
        print("your new balance is " + str(balance) + ".")

#the app really starts here, this program tells you what to input to do different things, then takes you to other games based on what you input.
        
def play(balance, autoBet, betAmount):
    #tells you what to input
    print()
    print("to go to settings enter 0")
    print("to play high-low enter 1")
    print("to play slots enter 2")
    print("to play blackjack enter 3")
    print("to play hangman enter 4")
    print()
    play = str(input("what game do you want to play? >> "))
    #takes you to other games 
    if play == "1":
        import random
        print()
        highLow(balance, autoBet, betAmount)
    elif play == "2":
        import random
        slots(balance,autoBet,betAmount)
    elif play == "3":
        
        play_round(balance,autoBet,betAmount) 
    elif play == "4":
        hang(balance,autoBet,betAmount)
    elif play == "0":
        settings(balance)
    else:
        #if someone inputs a number with no game assigned then it tells them that
        print("sorry, there is no game assigned to that number", end="")
        for i in range(3):
            time.sleep(0.5)
            print(".",end="")
        print(" yet")
        play(balance, autoBet, betAmount)

#This function handles the score payout for the highlow game  
def payoutHL(bet,balance,HL,num,autoBet,betAmount):
    
    #if the highlow answer was low and correct it sets this as the value for num
    if HL == "l": 
        num = 100-num
        
    #if the highlow answer was high and correct it sets this as the value for num
    elif HL == "h":
        num = num - 1
        
    #if the highlow answer was equal and correct it sets this as the value for num
    elif num == "e":
        num = -1

    #the function now performs calculations on the hidden value to find how likely you were to guess correctly and gives you a greater or lesser reward acordingly
    num = num/100
    num = 1 - num
    payout = float(bet)*(float(num)*2.0)
    balanceCheck(payout,balance,autoBet,betAmount,"hl")

#this function lets you reset your settings, not much to it
def settings(balance):
    print("your balance is", str(balance) + ".")
    player = input("what's your name? >> ")
    autoBet = input("do you want autobet on?: ")
    if autoBet[0].lower() == "y":
        betAmount = input("what do you want the autobet to be?: ")
    else:
        betAmout = 0
        
    #sends the user back to the game menu
    play(balance,autoBet,betAmount)

#this is the slots game, it generates 3 numbers and shows them in a row, then gives you a certain payout depending on what numbers were generated 
def slots(balance, autoBet, betAmount):
    #random numbers
    s1 = rand.randint(1,6)
    s2 = rand.randint(1,6)
    s3 = rand.randint(1,6)
    cb = betAmount
    if autoBet[0].lower() == "n":
        cb = input("what do you want to bet? >> ")
    #makes 6s into 7s, making it a 1-6 chance to get one 
    if s1 == 6:
        s1+=1
    if s2 == 6:
        s2+=1
    if s3 == 6:
        s3+=1
        
    #prints the machine
    print("{["+str(s1)+"]"+"["+str(s2)+"]"+"["+str(s3)+"]}")
    
    #checking for if you won
    if s1 == s2 == s3 and s1 == 7:
        print("JACKPOT!!!")
        balance = slotsCalc(balance,cb,"J")
    elif (s1 == s2 and s1 == 7) or (s1 == s3 and s1 == 7) or (s3 == s2 and s3 == 7):
        print("Big Win")
        balance = slotsCalc(balance,cb,"B")
    elif s1 == s2 == s3 and s1 != 7:
        print("Major Win")
        balance = slotsCalc(balance,cb,"M")
    elif (s1 == s2 != s3 and s1 != 7) or (s1 != s2 == s3 and s2 != 7) or (s1 == s3 != s2 and s1 != 7):
        print("Minor Win")
        balance = slotsCalc(balance,cb,"m")
    elif s1 == 7 or s2 == 7 or s3 == 7:
        print("Tiny Win")
        balance = slotsCalc(balance,cb,"T")
    else:
        print("no win :(")
        balance = slotsCalc(balance,cb,"no")
        
    #gets are more pretty number for your balance so you dont get huge decimals 
    balance = roundBal(balance)
    print("Your new balance is", balance)

    #asks if you wanna play again
    again = input("do you want to play again? >> ")
    if again[0].lower() == "n":
        play(balance,autoBet,betAmount)
    elif again[0].lower() == "y":
        slots(balance, autoBet, betAmount)
    else:
        #I got bored and did this
        print("are you dumb?")
        time.sleep(2)
        print("like seriously...", end="")
        time.sleep(1.2)
        print("you might wanna get that checked out")
        time.sleep(2)
        print("and by that I mean you didn't answer with a yes OR a no, try again next time I guess")

#I didn't like how the python round function worked to I made my own
def roundBal(balance):
    balance = balance *100
    balance = round(balance)
    balance = balance /100
    return balance
        
#This function calculates your payout for slots 
def slotsCalc(balance,cb,win):
    if win == "no":
        balance -= cb
    elif win == "m":
        balance += cb*1.5
    elif win == "M":
        balance += cb*4
    elif win == "J":
        balance += cb*100
    elif win == "B":
        balance += cb*20
    elif win == "T":
        balance += cb/6
    return balance


#-------------------------------------------




# Create deck of cards
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# Initialize & shuffle deck
def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    # Use random's shuffle (don't have to put random. bc I imported *
    # * = all contents inside random
    shuffle(deck)
    return deck
# Function to deal random card from deck
def deal_card(deck):
    if len(deck) == 0:
        print("The deck is empty.")
        return None
    else:
        # Removes index of random card selected
        # Prevents same cards from being reused within a round
        return deck.pop()
# Calculate value of hand
def calculate_hand(hand):
    total_val = 0
    num_aces = 0
    for card in hand:
        rank = card[0]
        # Face cards have a value of 10 in blackjack
        if rank in ['J', 'Q', 'K']:
            total_val += 10
        # If card is ace, add to num_aces
        elif rank == 'A':
            num_aces += 1
        # Number cards have the same value as their number in blackjack
        else:
            total_val += rank
    # Bring aces into the mix
    for i in range(num_aces):
        if total_val + 11 <= 21:
            total_val += 11
        else:
            total_val += 1
    return total_val
# Display cards in hand
def display_hand(hand):
    for card in hand:
        # Can also format using .format(), but this is another way I learned
        # how to do it from DATA 101
        print(f"{card[0]} of {card[1]}")
# Check to see if an ace is in hand
def ace_present(hand):
    for card in hand:
        rank, suit = card
        if rank == 'A':
            return True
    return False
# Total earnings (when choose to play again)
total_earnings = 0
# Blackjack game
def play_round(balance,autoBet,betAmount):
    # Did research into global vs local variables
    # (learned in AP CSA but this was in the Java language, not Python)
    # This statment means that the total_earnings variable is being modified
    # inside the function
    global total_earnings
    play_again = True
    while play_again == True:
        # Create game_total to calculate earnings at end
        game_total = 0
        deck = create_deck()
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        # User input for buy-in
        # (Assuming scoring system would use ints, not floats)
        buy_in = int(input("Enter buy-in: "))
        # Display player hand
        print("\nYour hand: ")
        display_hand(player_hand)
        # Display dealer's first card            
        print("\nDealer's first card: ", dealer_hand[0][0], "of", dealer_hand[0][1])
        # Creating user choice for ace value
        if ace_present(player_hand):
            ace_val = int(input("\nChoose the value for Ace (1 or 11): "))
            # Noticed that program was doing this and did not know how
            # to fix
            # Realized this is pretty similar to real-world playing,
            # so decided to just alert user of its occurrence
            print("If you choose to hit and hand > 21 b/c Ace is 11, program will change Ace back")
            print("to 1 automatically")
        else:
            ace_val = None
        # Creating hand calculations for player and dealer
        player_val = calculate_hand(player_hand)
        dealer_val = calculate_hand(dealer_hand)
        print("\nPlayer's total value:", player_val)
        # Loop created for hit or stand (set to True by default)
        while True:
            # .lower() in case user capitalizes first letter of word
            # or if user types in all caps
            hit_or_stand = input("Do you want to hit or stand? ").lower()
            if hit_or_stand == "hit":
                # Gives player another card & calculates hand
                new_card = deal_card(deck)
                player_hand.append(new_card)
                player_val = calculate_hand(player_hand)
                print("\nPlayer's hand: ")
                display_hand(player_hand)
                print("\nPlayer's total value: ", player_val)  
                if player_val > 21:
                    print("Busted! You lose.")
                    game_total = -(buy_in)
                    print("\nYour earnings this round: ", game_total)
                    total_earnings += game_total
                    print("\nYour total earnings: ", total_earnings)
                    # u_i = user input
                    u_i = int(input("Do you want to play again (0 for no, 1 for yes)? "))
                    print()
                    if u_i == 0:
                        play_again = False
                    elif u_i == 1:
                        play_again = True
                    else:
                        print("Invalid input. Please enter either 0 or 1.")
                    # Exit inner loop if player busts
                    break
            # If user decides to stand, no longer have to be in the while
            # loop that gives player another car
            elif hit_or_stand == "stand":
                 break
        if player_val <= 21:
            # Stand switches game  to dealer's turn
            print("\nDealer's turn: ")
            print("\nDealer's hand: ")
            display_hand(dealer_hand)
            print("\nDealer's total value", dealer_val)
            # In blackjack, the dealer must hit if his/her hand <= 16
            while dealer_val <= 16:
                dealer_hand.append(deal_card(deck))
                dealer_val = calculate_hand(dealer_hand)
                print("\nDealer hits!")
                print("\nDealer's hand: ")
                display_hand(dealer_hand)
                print("\nDealer's total value: ", dealer_val)
            # Determine winner
            if dealer_val > 21:
                print("\nDealer busts! You win!")
                game_total = buy_in + buy_in*1
                print("\nYour earnings this round: ", game_total)
                total_earnings += game_total
            elif dealer_val <= 21:
                if dealer_val == player_val:
                    print("\nPush")
                    game_total = buy_in + buy_in*1
                    print("\nYour earnings this round: ", game_total)
                    total_earnings += game_total
                elif dealer_val > player_val:
                    print("\nDealer wins!")
                    game_total = -(buy_in)
                    print("\nYour earnings this round: ", game_total)
                    total_earnings += game_total
                elif dealer_val < player_val:
                    print("\nYou win!")
                    game_total = buy_in + buy_in*1
                    print("\nYour earnings this round: ", game_total)
                    total_earnings += game_total
                elif player_val == 21 and dealer_val !=21:
                    print("\nBlackjack!")
                    game_total = buy_in + buy_in*(3/2)
                    print("\nYour earnings this round: ", game_total)
                    total_earnings += game_total
            # Cumulative earnings (from playing again)
            print("\nYour total earnings: ", total_earnings)
            balance = balance + total_earnings
            balance = roundBal(balance)
            # Play again option
            u_i = int(input("Do you want to play again (0 for no, 1 for yes)? "))
            print()
            if u_i == 0:
                play_again = False
                
                play(balance,autoBet,betAmount)
            elif u_i == 1:
                play_again = True
            # Used in case a user inputs something other than 0 or 1
            # Always important to try to predict user error!
            else:
                print("Invalid input. Please enter either 0 or 1.")
                continue



def blackjack():
    global total_earnings
    play_again = True
    while play_again:
        play_again = play_round()
        if not play_again:
            break
            

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter
        else:
            displayed += "-"
    return displayed
# Main function to play games
def hang(balance,autoBet,betAmount):
    # CSCI 220 relevant words
    words = ("PYTHON", "CONDITIONAL", "BINARY", "LOOP", "GRAPHICS",
             "BOOLEAN")
    # Uses random's choice to select a random word from words
    word_choice = choice(words)
    # Creates blank spaces based on length of word
    guessed = ["_"] * len(word_choice)
    already_guessed = []
    user_attempts = 0
    print("Hangman")
    # Six attempts chosen bc when drawing a stick figure, 6 wrong answers
    # will make full hangman
    print("\nYou have six attempts.")
    while user_attempts < 6:
        print("\nWord:", display_word(word_choice, guessed))
        # .upper() used in case user input lowercase letter
        # (Elements in lists are case sensitive)
        letter_guess = input("Guess a letter: ").upper()
        if letter_guess in guessed:
            print("Letter already guessed.")
        if letter_guess in word_choice:
            already_guessed.append(letter_guess)
            # for loop gets index of letter
            for i in range(len(word_choice)):
                if word_choice[i] == letter_guess:
                    # empty spaces[letter_index] = letter_guess
                    # append letter_guess to proper index in string
                    guessed[i] = letter_guess
        else:
            user_attempts += 1
            print("Incorrect! Attempts left:",6 - user_attempts)
        # If there are no more blank spaces
        # AKA user has completed the word/solved the game
        if "_" not in guessed:
            print("Congratulations! You guessed the word:", word_choice)
            break
    # Hypothetical hangman is fully drawn and user loses
    if user_attempts == 6:
        print("Out of attempts!")
        print("\nWord:", word_choice)
    play(balance,autoBet,betAmount)


def main():
    autoBet = input("do you want autobet on?: ")
    if autoBet[0].lower() == "y":
        betAmount = float(input("what do you want the autobet to be?: "))
    else:
        betAmout = 0
    play(100,autoBet,betAmount)

# Conditional statement to execute main function
if __name__ == "__main__":
    main()

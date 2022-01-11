import json
import random

##cards = tarot.DrawCards.return_fortune()
#data file
data = 'tarot_data/tarot.json'

# Loads input file
def load_deck(input_file):
    f = open(input_file)
    tarot_cards = json.load(f)
    f.close()
    return tarot_cards

# Shuffles order 
def shuffle(deck):
    print("Shuffling Tarot Deck...")
    random.shuffle(deck)

# Selects 4 cards for each state in the spread
def select_cards(deck):
    print("Selecting spread cards..")
    cards = []
    states = ['Past', 'Present', 'Future', 'Inspiration']
    for state in states:
        num = random.randint(0, len(deck) -1 )
        card = deck[num]
        #delete num so we don't get same twice
        del(deck[num])
        # add state to dictionary
        card["state"] = state
        cards.append(card)
    return cards
        
def main():
    ## Get users name
    user_name = input("Enter your name: ")
    print("Hello " + user_name + ", welcome to your Past-Present-Future-Inspiration spread tarot reading... ")
    # load data
    card_data = load_deck(data)
    # shuffle 
    shuffle(card_data)
    # get tarot cards
    selected_tarot = select_cards(card_data)
    # print outputs for each state 
    for tarot in selected_tarot:
        print("The " + tarot["state"] + " you got is: " + tarot["name"] + ". This card is described to relate to: " + tarot["rdesc"] + ". " + tarot["desc"] )

if __name__ == "__main__":
    main()


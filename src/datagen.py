import numpy as np
import json
import seaborn as sns
import matplotlib.pyplot as plt

choices = {'BBB': np.array([0,0,0]),
             'RRR': np.array([1,1,1]),
             'BRB': np.array([0,1,0]),
             'RBR': np.array([1,0,1]),
             'BBR': np.array([0,0,1]),
             'RRB': np.array([1,1,0]),
             'BRR': np.array([0,1,1]),
             'RBB': np.array([1,0,0])}


def get_decks(seed: int,
              num_decks: int,
              num_cards: int = 52
             ) -> np.ndarray:
    """
    This function generates random decks based on the inputted seed.
    It saves the seeds and decks to a local folder named 'data'.
    
    Arguments:
        seed: an integer that ensures reproducability and determindes the order of randomly generated numbers
        num_decks: the number of decks you wish to create
        deck_size: the number of cards in each deck (default is 52)
    """
    rng = np.random.default_rng(seed)
    arr = rng.integers(low=0, high=2, size=(num_decks,num_cards))
    np.save('data/decks_'+str(seed)+'.npy', arr)
    state = rng.bit_generator.state
    with open('data/state.json', 'w') as f:
        json.dump(state, f)
    return arr


# THIS CODE DOES WORK!!!
def game(p1_choice: str,
         p2_choice: str,
         decks: np.ndarray
         ) -> list[list, list]:
    """
    Simulate the game of Penney and store results.

    Arugments:
        p1_choice: player 1's card selection
        p2_choice: player 2's card selection,
        deck: chosen deck to simulate the game
    
    """
    p1_choice, p2_choice = choices[p1_choice], choices[p2_choice]

    # Initialize counters
    p2_wins_tricks, p2_wins_cards = 0, 0,
    draw_tricks, draw_cards = 0, 0

    # PLAY THE GAME
    for deck in decks: # Loop through each deck
        p1_tricks, p2_tricks, p1_cards, p2_cards = 0, 0, 0, 0
        trick = np.array([])
        trick = deck[:2] # Add first 2 cards to trick
        for i in range(2, len(deck)):
            trick = np.append(trick, deck[i]) # Add the 3rd (then next) card
            
            # CHECK FOR A P1 WIN
            if np.array_equal(trick[-3:], p1_choice): # If p1 wins, update p1's trick and card counts and refresh trick
                p1_tricks += 1
                p1_cards += len(trick)
                trick = np.array([])

            # CHECK FOR A P2 WIN
            elif np.array_equal(trick[-3:], p2_choice): # If p2 wins, update p1's trick and card counts and refresh trick
                p2_tricks += 1
                p2_cards += len(trick)
                trick = np.array([])
                    
        # SCORE THE GAME BY TRICKS
        if p2_tricks > p1_tricks:
            p2_wins_tricks += 1
        elif p2_tricks == p1_tricks:
            draw_tricks += 1
        
        # SCORE THE GAME BY CARDS 
        if p2_cards > p1_cards:
            p2_wins_cards += 1
        elif p2_cards == p1_cards:
            draw_cards += 1
    
    return [[p2_wins_tricks, draw_tricks], [p2_wins_cards, draw_cards]]


def simulate(deck: np.ndarray) -> list:
    """
    Produce simulations of Penney's game and save the results.
    Output: A list storing Player 1 and 2's tricks and cards.
    
    Arguments:
        deck = Array of decks to be simulated   
    """
    # Initalize external counters for the probabilities
        # annot_tricks and annot_cards hold the same probabilities but with the draw percentage in parentheses
    games_tricks, games_cards, annot_tricks, annot_cards = [], [], [], []
    
    # Loop through each choice for Player 1
    for p1_choice in choices:
        
        # Internal counter initializations but for each of Player 1's choices
        prob_tricks, prob_cards, prob_tricks_annot, prob_cards_annot = [], [], [], []
        
        # Play the game against Player 1's choice with every option for Player 2         
        for p2_choice in choices:
            outcome = game(p1_choice, p2_choice, deck)

            ### CALCULATE THE PROBABILITIES ###
            # Calculate the prob. of winning and of a draw based on number of TRICKS, and add to internal counters
            prob_win_tricks = round((outcome[0][0]/len(deck))*100)
            prob_tricks.append(prob_win_tricks)
            prob_draw_tricks = round((outcome[0][1]/len(deck))*100)
            prob_tricks_annot.append(str(prob_win_tricks) + '%\n(' + str(prob_draw_tricks) + '%)')
            
            # Calculate the prob. of winning and of a draw based on number of CARDS, and add to internal counters
            prob_win_cards = round((outcome[1][0]/len(deck))*100)
            prob_cards.append(prob_win_cards)
            prob_draw_cards = round((outcome[1][1]/len(deck))*100)
            prob_cards_annot.append(str(prob_win_cards) + '%\n(' + str(prob_draw_cards) + '%)')

        # Add the probabilities for Player 1's choice to the external counters
        games_tricks.append(prob_tricks)
        games_cards.append(prob_cards)
        annot_tricks.append(prob_tricks_annot)
        annot_cards.append(prob_cards_annot)

    tricks_map = sns.heatmap(data=games_tricks, annot=annot_tricks, fmt = '', annot_kws={"size": 8}, cmap='Blues', xticklabels=choices.keys(), yticklabels=choices.keys())
    tricks_map.set_title('Probability of Winning Based on Tricks')
    plt.xlabel("Player 2's Choice") # x-axis label with fontsize 15
    plt.ylabel("Player 1's Choice") # y-axis label with fontsize 15
    plt.savefig('data/tricks_heatmap.png')
    plt.show()
    
    cards_map = sns.heatmap(data=games_cards, annot=annot_cards, fmt = '', annot_kws={"size": 8}, cmap='Blues', xticklabels=choices.keys(), yticklabels=choices.keys())
    cards_map.set_title('Probability of Winning Based on Cards')
    plt.xlabel("Player 2's Choice") # x-axis label with fontsize 15
    plt.ylabel("Player 1's Choice") # y-axis label with fontsize 15
    plt.savefig('data/cards_heatmap.png')
    plt.show()

    return
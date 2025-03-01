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


def game(p1_choice: str,
         p2_choice: str,
         decks: np.ndarray
         ) -> list[list, list]:
    """
    This function simulates the game of Penney for the inputted decks and returns the results.

    Arugments:
        p1_choice: Player 1's card selection
        p2_choice: pPlayer 2's card selection,
        deck: the chosen decks to simulate the game
    """
    p1_choice, p2_choice = choices[p1_choice], choices[p2_choice]

    # Initialize counters
    p1_wins_tricks, p2_wins_tricks, p1_wins_cards, p2_wins_cards = 0, 0, 0, 0
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
        if p1_tricks > p2_tricks:
            p1_wins_tricks += 1
        elif p2_tricks > p1_tricks:
            p2_wins_tricks += 1
        else:
            draw_tricks += 1
        
        # SCORE THE GAME BY CARDS
        if p1_cards > p2_cards:
            p1_wins_cards += 1  
        elif p2_cards > p1_cards:
            p2_wins_cards += 1
        else:
            draw_cards += 1

    #print(f'Player 1 Wins by Tricks: {p1_wins_tricks}')
    #print(f'Player 2 Wins by Tricks: {p2_wins_tricks}')
    #print(f'Draws by Tricks: {draw_tricks}')
    #print('\n')
    #print(f'Player 1 Wins by Cards: {p1_wins_cards}')
    #print(f'Player 2 Wins by Cards: {p2_wins_cards}')
    #print(f'Draws by Cards: {draw_cards}')
    
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
            prob_win_tricks = outcome[0][0]/len(deck)
            prob_tricks.append(prob_win_tricks)
            prob_draw_tricks = outcome[0][1]/len(deck)
            prob_tricks_annot.append(str(prob_win_tricks) + '(' + str(prob_draw_tricks) + ')')
            
            # Calculate the prob. of winning and of a draw based on number of CARDS, and add to internal counters
            prob_win_cards = outcome[1][0]/len(deck)
            prob_cards.append(prob_win_cards)
            prob_draw_cards = outcome[1][1]/len(deck)
            prob_cards_annot.append(str(prob_win_cards) + '(' + str(prob_draw_cards) + ')')

        # Add the probabilities for Player 1's choice to the external counters
        games_tricks.append(prob_tricks)
        games_cards.append(prob_cards)
        annot_tricks.append(prob_tricks_annot)
        annot_cards.append(prob_cards_annot)

    tricks_map = sns.heatmap(data=games_tricks, annot=True, cmap='Blues', xticklabels=choices.keys(), yticklabels=choices.keys())
    tricks_map.set_title('Probability of Winning Based on Tricks')
    plt.xlabel("Player 2's Choice") # x-axis label with fontsize 15
    plt.ylabel("Player 1's Choice") # y-axis label with fontsize 15
    plt.show()
    
    cards_map = sns.heatmap(data=games_cards, annot=True, cmap='Blues', xticklabels=choices.keys(), yticklabels=choices.keys())
    cards_map.set_title('Probability of Winning Based on Cards')
    plt.xlabel("Player 2's Choice") # x-axis label with fontsize 15
    plt.ylabel("Player 1's Choice") # y-axis label with fontsize 15
    plt.show()

    print(annot_tricks)
    print(annot_cards)
    
    return
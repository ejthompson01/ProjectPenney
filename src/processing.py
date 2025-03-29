import numpy as np
choices = {'BBB': [0,0,0],
             'RRR': [1,1,1],
             'BRB': [0,1,0],
             'RBR': [1,0,1],
             'BBR': [0,0,1],
             'RRB': [1,1,0],
             'BRR': [0,1,1],
             'RBB': [1,0,0]}

# THIS CODE DOES WORK!!!
def game(p1_choice: str,
         p2_choice: str,
         decks: np.ndarray
         ) -> list[list, list]:
    """
    This function plays Penney's Game over multiple decks for 2 chosen card sequences,
    then computes the probability of Player 2 winning and drawing by tricks and cards.

    Arugments:
        p1_choice: Player 1's card selection.
        p2_choice: Player 2's card selection.
        deck: A deck to simulate the game.
    
    Returns:
        A list of the probabilities of Player 2 winning and drawing by tricks and cards.
    
    """
    # Convert the string choices to numpy arrays
    p1_choice, p2_choice = choices[p1_choice], choices[p2_choice]

    # Initialize counters for wins by tricks, wins by cards, draws by tricks, and draws by cards
    p2_wins_tricks, p2_wins_cards, draw_tricks, draw_cards = 0, 0, 0, 0

    # Play the game
    for deck in decks: # Loop through each deck
        p1_tricks, p2_tricks, p1_cards, p2_cards = 0, 0, 0, 0
        trick = list(deck[:2]) # Add the first two cards to the trick

        for i in range(2, len(deck)): # Loop through the rest of the deck
            trick.append(deck[i]) # Add the 3rd (then next) card

            if len(trick) >= 3: # If the trick has 3 cards, check for a win
                last_three = trick[-3:]
            
                # Check for a Player 1 trick
                if last_three == list(p1_choice): # If p1 wins, update p1's trick and card counts and refresh trick
                    p1_tricks += 1
                    p1_cards += len(trick)
                    trick = [] # Refresh the trick

                # Check for a Player 2 trick
                elif last_three == list(p2_choice): # If p2 wins, update p1's trick and card counts and refresh trick
                    p2_tricks += 1
                    p2_cards += len(trick)
                    trick = [] # Refresh the trick
                    
        # Score the game by tricks
        if p2_tricks > p1_tricks: # Add 1 to Player 2's win count if they won the game
            p2_wins_tricks += 1
        elif p2_tricks == p1_tricks: # Add 1 to the draw count if they tied
            draw_tricks += 1
        
        # Score the game by cards
        if p2_cards > p1_cards: # Add 1 to Player 2's win count if they won the game
            p2_wins_cards += 1
        elif p2_cards == p1_cards: # Add 1 to the draw count if they tied
            draw_cards += 1

    # Compute the probabilities ((number of games won / total number of games) * 100) for percentage form and rounded to 2 decimal places
    total_games = len(decks)
    prob_win_tricks = round((p2_wins_tricks / total_games) * 100, 2)
    prob_draw_tricks = round((draw_tricks / total_games) * 100, 2)
    prob_win_cards = round((p2_wins_cards / total_games) * 100, 2)
    prob_draw_cards = round((draw_cards / total_games) * 100, 2)
    
    return [prob_win_tricks, prob_draw_tricks, prob_win_cards, prob_draw_cards]


def simulate(deck: np.ndarray) -> list[list, list, list, list, int]:
    """
    This function simulates Penney's Game for all combinations of Player 1 and Player 2's choices.

    Produce simulations of Penney's game and save the results.
    Output: A list storing Player 1 and 2's tricks and cards.
    
    Arguments:
        deck = Array of decks to be simulated   
    """
    # Initalize external counters for the probabilities
        # annot_tricks and annot_cards hold the same probabilities but with the draw percentage in parentheses
    n_decks = len(deck)
    games_tricks, games_cards, annot_tricks, annot_cards = [], [], [], []
    
    # Loop through each choice for Player 1
    for p1_choice in choices:
        
        # Initialize internal counters for each of Player 2's choices
        prob_tricks, prob_cards, prob_tricks_annot, prob_cards_annot = [], [], [], []
        
        # Play the game against Player 1's choice with every option for Player 2         
        for p2_choice in choices:
            
            # If Player 1 and Player 2 choose the same option,
            # automatically set the probabilities and annotations to NaN
            if p1_choice == p2_choice:
                    prob_tricks.append(np.nan)
                    prob_cards.append(np.nan)
                    prob_tricks_annot.append("")
                    prob_cards_annot.append("")

            # If Player 1 and Player 2 choose different options,
            # play the game and add the probabilities to the internal counters
            elif p1_choice != p2_choice:
                    win_tricks, draw_tricks, win_cards, draw_cards = game(p1_choice, p2_choice, deck)

                    # Add probabilities to the internal counters
                    prob_tricks.append(win_tricks)
                    prob_cards.append(win_cards)

                    # Create annotations for the probabilities
                    prob_tricks_annot.append(str(win_tricks) + '%\n(' + str(draw_tricks) + '%)')
                    prob_cards_annot.append(str(win_cards) + '%\n(' + str(draw_cards) + '%)')

        # Add the probabilities for Player 1's choice to the external counters
        games_tricks.append(prob_tricks)
        games_cards.append(prob_cards)
        annot_tricks.append(prob_tricks_annot)
        annot_cards.append(prob_cards_annot)

    return [games_tricks, annot_tricks, games_cards, annot_cards, n_decks]
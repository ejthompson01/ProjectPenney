import seaborn as sns
import matplotlib.pyplot as plt
from src.processing import choices

def visualize(scores, filename):
    """
    Produce 2 heatmaps that represent the probability of Player 2 winning Penney's Game
    by cards and tricks based on Player 1 and Player 2's choices.
    
    Output: a png with 2 heatmaps, one scored by tricks and one scored by cards.
    
    Arguments:
        score: A list containing the scores from the game simulation. The list contains:
            - games_tricks: A 2D list of the probabilities of Player 2 winning based on tricks.
            - annot_tricks: A 2D list of the heatmap annotations for winning based on tricks.
            - games_cards: A 2D list of the probabilities of Player 2 winning based on cards.
            - annot_cards: A 2D list of the heatmap annotations for winning based on cards.
        filename: The name of the file to save the heatmaps as a PNG.
        
    """
    # Unpack the scores
    games_tricks, annot_tricks, games_cards, annot_cards, n_decks = scores

    # Create a figure with 2 subplots
    fig, (tricks_map, cards_map) = plt.subplots(1, 2, figsize=(13,5))

    # Create the heatmap for tricks
    sns.heatmap(data=games_tricks, ax=tricks_map, annot=annot_tricks, fmt = '', annot_kws={"size": 8},
                             cmap='Blues', xticklabels=choices.keys(), yticklabels=choices.keys(), square=True)
    # tricks_map.set(xlabel="Player 2's Choice", ylabel="Player 1's Choice", title='Probability of Winning Based on Tricks')
    tricks_map.set_title(f"Probability of Player 2 Winning Based on Tricks\nn_decks: {n_decks}")
    tricks_map.set_xlabel("Player 2's Choice") # x-axis label with fontsize 15
    tricks_map.set_ylabel("Player 1's Choice") # y-axis label with fontsize 15
    
    # Create the heatmap for cards
    sns.heatmap(data=games_cards, ax=cards_map, annot=annot_cards, fmt = '', annot_kws={"size": 8},
                            cmap='Blues', xticklabels=choices.keys(), yticklabels=choices.keys(), square=True)
    #cards_map.set(xlabel="Player 2's Choice", ylabel="Player 1's Choice", title='Probability of Winning Based on Cards')
    cards_map.set_title(f"Probability of Player 2 Winning Based on Cards\nn_decks: {n_decks}")
    cards_map.set_xlabel("Player 2's Choice") # x-axis label with fontsize 15
    cards_map.set_ylabel("Player 1's Choice") # y-axis label with fontsize 15
    
    plt.tight_layout()
    plt.savefig(f'heatmaps/{filename}.png')
    plt.show()
    return
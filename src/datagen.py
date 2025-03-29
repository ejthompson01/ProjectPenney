import numpy as np
import os
import json

HALF_DECK_SIZE = 26


def get_decks(n_decks: int,
              seed: int,
              half_deck_size: int = HALF_DECK_SIZE) -> np.ndarray:
    """
    Efficiently generates `n_decks` shuffled decks using NumPy.
    Saves the details of the deck in a dictionary in a separate .npy file.

    Arguments:
        n_decks: Number of decks to generate.
        seed: Seed for random number generation.
        half_deck_size: Half of the number of cards in the deck (default is 26).
    
    Returns:
        decks (np.ndarray): 2D array of shape (n_decks, num_cards), each row is a shuffled deck.
    """
    # Create a filename based on the seed
    filename = f'decks_{seed}.npy'

    # Check if the file already exists
    if filename in os.listdir('data/'):
        print(f"A file with seed {seed} already exists. Choose another seed.")
        return
    else:
        init_deck = [0]*half_deck_size + [1]*half_deck_size
        decks = np.tile(init_deck, (n_decks, 1))
        rng = np.random.default_rng(seed)
        rng.permuted(decks, axis=1, out=decks)
        np.save(f'decks/{filename}', decks)

        # Save the deck information in a dictionry and write it to a JSON file
        deck_dict = dict(n_decks = n_decks,
                        seed = seed,
                        half_deck_size = half_deck_size,
                        decks = filename)
        with open(f'data/decks_{seed}_dict.json', 'w') as file:
            json.dump(deck_dict, file, indent=4)
        return decks

def sample_decks(n_decks: int = None,
                 filename: str = 'data/test_decks.npy'
                 )-> np.ndarray:
    """
    Takes a sample of size 'n_decks' from previously generated decks.
    Users can use the testing_decks.zip file instead of creating new decks.

    Arguments:
        n_decks: The sample size of decks. If nothing is passed, it will default to the all decks in the file.
        filename: The name of the file holding the decks (default is 'testing_decks.zip').

    Returns:
        np.ndarray: A sample of decks.
    """
    data = np.load(filename, allow_pickle=True)
    # Check if a n_decks value is provided
    if n_decks is None:
        n_decks = len(data)
    
    index = np.random.choice(data, n_decks, replace=False)  
    return data[index]

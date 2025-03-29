import numpy as np
import os
import zipfile
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
    filename = 'data/decks_'+str(seed)+'.npy'
    if filename in os.listdir('data/'):
        print(f"A file with seed {seed} already exists. Choose another seed.")
        return
    else:
        init_deck = [0]*half_deck_size + [1]*half_deck_size
        decks = np.tile(init_deck, (n_decks, 1))
        rng = np.random.default_rng(seed)
        rng.permuted(decks, axis=1, out=decks)
        np.save(filename, decks)
        deck_dict = dict(n_decks = n_decks,
                        seed = seed,
                        half_deck_size = half_deck_size,
                        decks = decks)
        np.save('data/deck_dict_'+str(seed)+'.npy', decks)
        return decks


def sample_decks(n_decks: int = None,
                 filename: str = 'testing_decks.zip'
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
    # Check if a n_decks value is provided
    if n_decks is None:
        n_decks = len(np.load(filename, allow_pickle=True))

    # Check if the user wants to use the testing_decks.zip file
    if filename == 'testing_decks.zip':
        with zipfile.ZipFile(filename, 'r') as myzip:
            with myzip.open('testing_decks.npy') as myfile:
                data = np.load(myfile)
    else:
        data = np.load(filename, allow_pickle=True)
    
    index = np.random.choice(data.shape[0], n_decks, replace=False)  
    return data[index]

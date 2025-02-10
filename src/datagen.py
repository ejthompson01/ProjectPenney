import numpy as np

HALF_DECK_SIZE = 26

def get_decks(n_decks: int,
              seed: int,
              half_deck_size: int = HALF_DECK_SIZE,) -> tuple[np.ndarray, np.ndarray]:
    """
    Efficiently generate `n_decks` shuffled decks using NumPy.
    
    Returns:
        decks (np.ndarray): 2D array of shape (n_decks, num_cards), each row is a shuffled deck.
    """
    init_deck = [0]*half_deck_size + [1]*half_deck_size
    decks = np.tile(init_deck, (n_decks, 1))
    rng = np.random.default_rng(seed)
    rng.permuted(decks, axis=1, out=decks)
    return decks
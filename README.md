# Project Penney
## ProjectPenney Overview

The purpose of this code is to create a heatmap displaying the probabilities of winning the card version of Penney's game given each player's sequence selection. The intent is to create a heatmap users can reference when playing the game in real life to maximize their chances of winning. If you are new to Penney's game, please read [this Wikipedia page](https://en.wikipedia.org/wiki/Penney%27s_game) for an introduction.


### How to Play
This version of Penny's Game is played with 2 people. Each player begins by choosing a 3 card color sequence, for example, Black Red Black or Red Red Black. Then a standard 52 card deck is well shuffled. One-by-one each card is delt while the player look for their card sequence. Deal the cards while looking for each player's sequence. When a player's sequence appears, that player wins the trick and the cards that led to it. The cards of the trick are set aside in a pile for the player who won it. Continue to deal the deck in this fashion until the cards run out with separate pile for each trick.

To score by tricks, count the pile of tricks each player has. The player with more tricks wins. To score by cards, count the cards in each player's tricks. The player with more total cards win.


## Quick Start

To begin using the code, clone the repository and ensure that Python and the following libraries are installed:
- Numpy
- Seaborn
- Matplotlib.pyplot

The repository is already initalized with 1 million decks, so to just see the code work, execute the following lines of code. These are also found in the *final_heatmaps.ipynb* file.

```
from src.datagen import sample_decks
from src.processing import simulate
from src.visualize import visualize
import numpy as np

decks = sample_decks('data/decks_test.npy', 100000)
vizualize(simulate(decks))
```


## How to Use/Understanding the Code
### 1. Create or augment decks

If you wish to use the code, the first step is to create the decks of cards to use in the simulation. There are 2 ways to go about this: create new decks or select a sample from stored decks. If you would like to create new decks use the `get_decks` function. Then call `sample_decks` to access the decks. Information about the created decks are stored in a dictionary in a corresponding .npy file. Both the deck and dictionary files end in the seed used to create the decks and are saved in the *data* folder. If you don't wish to make new decks, there are 1 million already stored in *decks_test.npy* in the *data* folder. Pass this file and the desired number of decks into `sample_decks` to acces the decks.


### 2. Simulate the games and create the heatmaps

Once you have created the decks with your specifications, the next step is to simulate the games and produce the heatmaps. Create a variable by calling the `simulate` function in the *processing.py* file in the *src* folder. Pass this variable into the `visualize` function from the *visualize.py* file in the same folder to create the heatmaps.
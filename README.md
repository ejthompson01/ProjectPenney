# Project Penney
## ProjectPenney Overview

The purpose of this code is to create a heatmap displaying the probability of winning based on your opponents choice in the card version of Penney's game. The intent is to create a heatmap users can reference when playing the game in real life to maximize their chances of winning. If you are new to Penney's game, please read [this Wikipedia page](https://en.wikipedia.org/wiki/Penney%27s_game) for more information.

There are two ways of winning Penney's game: by tricks or by cards. To win by tricks, you must have more tricks than your opponent. To win by cards, you count up the number of cards in all of your tricks then compare. The winner by cards has more cards than their opponent. It is possible for one player to win by tricks and the other to win by cards, so the code produces two heatmaps: one displaying the proabilities for winning by tricks and one by cards.

**DISCLAIMER: The code is designed to only help the player who chooses their card sequence SECOND. To use the heatmap, you must choose the sequence of cards second, as the probabilities are based on the opponents selection. If you are the player who chooses their card sequence first, the heatmap will not aid in your selection. If you really want to beat your opponent, choose second and reference the heatmap!**


## Quick Start

To begin using the code, clone the repository and ensure that Python and the following libraries are installed:
- Numpy
- Json
- Seaborn
- Matplotlib.pyplot

The repository is already initalized with functional examples, so to just see the code work, execute the following lines of code. These are also found in the *final_heatmaps.ipynb* file.

```
from src.datagen import get_decks, game, simulate
import numpy as np
decks = np.load('data/decks_1.npy')
simulate(decks)
```


## How to Use/Understanding the Code
### 1. Create decks

If you wish to use the code, the first step is to create the decks of cards to use in the simulation. This is done through the **get_decks** function in the *datagen.py file*. **get_decks** takes 3 arguments, seed, num_decks, and num_cards, and creates a .npy file in the 'data' folder named *decks_*(the seed number)*.npy*. It also produces a *state.json* for the random number generator to ensure reproducibility in the same folder.

- seed: This is an integer that determines the order and values of the random numbers generated to create the decks. This value is saved in the name of the .npy file.
- num_decks: This represents the number of decks you wish to create. I recommend producing at least 1,000,000 for accurate probabilities.
- num_cards: This is the number of cards you wish to have in each deck. The default is 52.


### 2. Simulate the games

Once you have created the decks with your specifications, the next step is to simulate the games and produce the heatmaps. This is done through the **simulate** function in the *datagen.py* file. The **simulate** function takes one argument, deck, which are the decks created in step one. To properly use the **simulate** function you must load the .npy file into a variable with the np.load() function. An example of how to do this is below:
```
import numpy as np
decks = np.load('data/decks_1.npy')
```
From there you pass the variable containing the loaded decks into **simulate** which produces the heatmaps. The heatmaps are saved in a folder called *heatmaps*.


Here is an example of how you can use the code. Fill in the arguments left blank.


```
from src.datagen import get_decks, game, simulate

seed = 
num_decks = 
num_cards = 

get_decks(seed, num_decks, num_cards)
decks = np.load(f'data/decks_{seed}.npy')
simulate(decks)
```




# Project Penney
## ProjectPenney Overview

The purpose of this code is to create a heatmap displaying the probabilities of winning the card version of Penney's game given each player's sequence selection. The intent is to create a heatmap users can reference when playing the game in real life to maximize their chances of winning. If you are new to Penney's game, please read [this Wikipedia page](https://en.wikipedia.org/wiki/Penney%27s_game) for an introduction.

### How to Play
This version of Penny's Game is played with 2 people. Each player begins by choosing a 3 card color sequence, for example, Black Red Black or Red Red Black. One player is deemed the Dealer who then thoughroughly shuffles a standard 52 card deck. The Dealer deals each card one-by-one and side-by-side while both players watch for their card sequence to appear. When a player's sequence appears, the cards are compiled into a pile and set aside near that player. One of these piles is called a trick. The Dealer continues to deal the deck beginning a new trick. Players continue to look for their sequence and create new piles for each trick until the deck runs out. If neither player wins the final trick after dealing all the cards, the remaining cards are set aside and not counted in scoring. To score by tricks, count the piles of tricks each player has. The player with more tricks wins. To score by cards, count the total number of cards in each player's trick piles. The player with more total cards wins.


### Tabel of Contents
**data** folder
- Purpose: This folder holds all data for the project. Any new data created by users will get stored here.
- Contains: *test_decks.npy* (a zip file containing 1 million previously generated decks) and *test_deck_dict.json* (a npy file containing the metadata for testing_decks.zip)
**heatmaps** folder
- Purpose: This folder holds all heatmap .png's for the project. Any new heatmaps created by the user will get stored here.
- Contains: *test_heatmaps.png* (a png file containing the heatmaps using the decks in test_decks.npy)
**src** folder
- Purpose: This folder holds the modules used for creating this project.
- Contains: *datagen.py* (a python file that contains functions for data generation and access), *processing.py* (a python file that contains functions for simulating the game), and *visualize.py* (a python file that contains functions for producing heatmaps)


## Quick Start
To begin using the code, clone the repository and ensure that Python and the following libraries are installed:
- Numpy
- Seaborn
- Matplotlib.pyplot

The repository is already initalized with 1 million decks, so to just see the code work, execute the following lines of code. These are also found in the *testing.ipynb* file.

```
from src.datagen import sample_decks
from src.processing import simulate
from src.visualize import visualize

decks = sample_decks(1000000, 'data/test_decks.npy')
visualize(simulate(decks), 'heatmaps')
```


## How to Use/Understanding the Code
### 1. Create or augment decks
The first step to using the code is accessing decks to use when simulating the Penney's Game. Users can either create a new set of decks or use the previously created decks stored in the data folder. To create new decks, call the `get_decks` function. Information about the created decks are stored in a dictionary in a corresponding .npy file. Both the deck and dictionary files end in the seed used to create the decks and are saved in the *data* folder. To use the loaded decks, call the `sample_decks` function and pass in 'testing_decks.zip' and the number of desired decks. The `sample_decks` function can also be used to access decks after users create them.


### 2. Simulate the games and create the heatmaps

Once you have created the decks with your specifications, the next step is to simulate the games and produce the heatmaps. Create a variable by calling the `simulate` function in the *processing.py* file in the *src* folder. Pass this variable into the `visualize` function from the *visualize.py* file in the same folder to create the heatmaps.
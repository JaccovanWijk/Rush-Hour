# Rush-Hour
In this project we tried to solve the Rush Hour game with multiple algorithms, some provided with multiple heuristics. Rush Hour is a pretty simplistic boardgame with rules that are easy to understand. However, solving this problem with algorithms becomes quite complex.

The board is a square of six by six, nine by nine or twelve by twelve squares with cars of length two or three spread out across the board. Cars are only allowed to go straight; forward an backwards. The goal of the game is to move a certain car, the red car, to the exit, which is positioned on respectively the third, fifth or seventh row on the right side.

Our goal is to use different algorithms to solve the seven given beginstates of a board in the shortest amount of time possible, or the shortest amount of moves possible.

```(maybe foto)```

[Our assignment can be find here](http://heuristieken.nl/wiki/index.php?title=Rush_Hour)

## Getting Started
The code is written in Python3.6.5. To run this code you can install the requirements.txt with pip. You can do this with the following command:
```
pip install -r requirements.txt
```

## Structure
All code except for main.py is positioned in de "code"-directory. All beginstates are stored in the data folder as text files. Some images that are (mostly) irrelivant are stored in the "images"-directory.

## Testing
If all modules from ```requirements.txt``` are installed, you can run the code by using the following instruction:
```
python main.py
```
Now a userinterface will pop up ```(maybe foto)```. If you follow the instructions the algorithms will run automaticly. Don't panic if the popup screen freezes, python is busy with the algorithm. With some algorithms you can see the progress, with others this isn't possible.

### Tips for running our code in a decent timespan
* If you want to run the **Random algorithm** a lot of times, choose a board of size 6 by 6. If you want to see the larger boards in action you should consider running it less times;
* If you want to run the **Breadth First algorithm**, **Astar**, or **Branch and Bound**, choose board 1, 2, or 3;


## Authors
* Ian Epping
* Dylan Wellner
* Jacco van Wijk

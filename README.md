# ECM2423 Coursework

This repo holds the source code used to answer questions from the coursework for my module ECM2423

Items in the project include:
- Implementation of K-means clustering alogrithm to determine hand written numbers from imagines and search for patterns in a Pokemon data set for my written report
- 8 puzzle game implemenation that plays where my algorithm solves the puzzles its self for any N sized puzzle.  

Here contains information on how to run implemented code from coursework specification

## Installation

Naviagte to the directory with source code in

For Question 1 follow instructions below:
Copy and paste into terminal
```
cd eight_puzzle
```
For Questiont 2 follow instructions below:
Copy and paste in to terminal
```
cd k_means
pip3 install numpy
pip3 install matplotlib
pip3 install sklearn
pip3 install scipy
pip3 install pandas
```


## Usage and description
### Question 1

For question 1, copy and paste the below text in to the terminal
```
python3 a_star.py
```
Here you will be asked if you would like to do a demo or add in your own unique start and end state of the puzzle (Question 1.3). After that you be asked which heuristic you want to use. Then your puzzle will be solved. The demo puzzle 2 is the one given in the specification and runs in 17 seconds for Manhattan function and 24 minutes for hammering function. If you input unsolvable puzzles you'll be asked to try again.

After that has run copy and paste the below text in to the terminal
```
python3 n_puzzle.py
```
Here you can input any given N-puzzle and A* algorithm will solve the puzzle using the hammering function.

### Question 2

For question 2,E copy and paste the below text in to the terminal
```
python3 k_means_digits.py
```
Here you will displayed the findings for question 2.2 as described in my answers report.
Next paste:
```
python3 k_means_function.py
```
This is code running my own K means clustering function on the digits data set to show the cendroid produced by my function.
Finally, paste the below into the terminal
```
python3 pokemon.py
```
Running this show my findings from using k means to explore the pokemon data which you can refer to question 2.4 in my report

## Contributing
Student number 670006710

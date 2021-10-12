import math
import time
from a_star import solvable, a_star, matrix_display

open_states = []
closed_states = []


def n_matrix_display(state):
    line = []
    N = int(math.sqrt(len(state)))
    for i in range(0, N):
        for j in range(i * N, (i + 1) * N):
            line.append(state[j])
        print(line)
        line = []


if __name__ == "__main__":
    states_chosen = False
    print("Welcome to my A* algorithm N-puzzle solver")
    print(
        "Enter a states a string of numbers like this : 0,1,2,3,4,5,6,7,8 to represent matrix below and press enter ("
        "Where 0 is the blank space).")
    print(matrix_display([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print("You can enter any N-puzzle size into this solver, it must be N + 1 in size")
    while states_chosen is False:
        demo = input("Would you like to see a demo? Enter '0' for no, '1' for yes.")
        if demo == "0":
            start_state = list(map(int, input("Enter start state like example shown above: ").split(",")))
            goal_state = list(map(int, input("Enter goal state like example shown above: ").split(",")))
            if solvable(start_state, goal_state):
                print("Puzzle is solvable!")
                states_chosen = True
            else:
                print("Puzzle isn't solvable, try another one or make sure if correct size with a 0 and same numbers")
        elif demo == "1":
            start_state = [5, 1, 2, 4, 0, 7, 3, 8, 9, 6, 14, 11, 13, 15, 10, 12]
            goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
            print("\nStart State: \n")
            n_matrix_display(start_state)
            print("\nEnd State: \n")
            n_matrix_display(goal_state)
            print("\nSolution: \n")
            states_chosen = True
        else:
            print("Please enter 0 or 1.")
    start_time = time.time()
    print("\nSearching...\n")
    ans = (a_star(start_state, goal_state, 0))
    n_matrix_display(start_state)
    for n in ans:
        print("\nMove the blank title " + n[1] + "\n")
        n_matrix_display(n[0])
    print("\nIt takes " + str((len(ans))) + " moves to solve the puzzle. Below you can see time taken:")
    print("--- %s seconds ---" % (time.time() - start_time))
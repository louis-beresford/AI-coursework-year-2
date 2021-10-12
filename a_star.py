import collections
import math
import time

open_states = []
closed_states = []


class Node():
    def __init__(self, parent=None, state=None):
        self.parent = parent
        self.state = state
        self.g = 0
        self.h = 0
        self.f = 0
        self.move = ""

    def __eq__(self, other):
        return self.state == other.state

    def __repr__(self):
        return "<current: %s parent: %s> g: %s" % (self.state, self.parent, self.g)


# determine if given and start and goal state are solvable
def solvable(start_state, goal_state):
    if len(start_state) != len(goal_state):
        return False
    elif not math.sqrt(len(start_state)).is_integer():
        return False
    elif collections.Counter(start_state) != collections.Counter(goal_state):
        return False
    start_inversions = 0
    goal_inversions = 0
    # number of inversions must be both either even or odd not different
    for i in range(1, len(start_state)):
        index_start = start_state.index(i)
        index_goal = goal_state.index(i)
        for j in start_state[:index_start]:
            if i < j != 0:
                start_inversions = start_inversions + 1
        for k in goal_state[:index_goal]:
            if i < k != 0:
                goal_inversions = goal_inversions + 1
    if 0 == (goal_inversions - start_inversions) % 2:
        return True
    else:
        return False


def out_of_place_tiles(current_state, goal_state):
    c = 0
    for i in current_state:
        if current_state.index(i) != goal_state.index(i) and current_state.index(i) != 0:
            c += 1
    return c


def manhattan_distance(current_state, goal_state):
    N = math.sqrt(len(current_state))
    distance = 0
    for i in current_state:
        difference = abs(goal_state.index(i) - current_state.index(i))
        if i != 0:
            x = difference % 3  # get how many move across needed
            y = difference / 3  # get how many moves down needed
            distance += x + int(math.floor(y))
            # account for going down a level when list is read
            # eg state is 012345678, 2 and next to each other in list but actually 2 moves part
            if abs(goal_state.index(i) % 2 - current_state.index(i) % 3) == 2 and difference % N == 1:
                distance += 2
    return distance


def neighbours(current_state):
    N = int(math.sqrt(len(current_state.state)))  # get width and height of grid

    # find the blank tile
    blank_tile = current_state.state.index(0)

    # list to store neighbours in
    neighbours = []

    # Can tile move left?
    if blank_tile % N != 0:
        left_move_state = current_state.state.copy()
        left_move_state[blank_tile], left_move_state[blank_tile - 1] = left_move_state[blank_tile - 1], left_move_state[
            blank_tile]
        left_node = Node(current_state.state, left_move_state)
        left_node.move = "left"
        neighbours.append(left_node)

    #  Can tile move right?
    if blank_tile % N != N - 1:
        right_move_state = current_state.state.copy()
        right_move_state[blank_tile], right_move_state[blank_tile + 1] = right_move_state[blank_tile + 1], \
                                                                         right_move_state[blank_tile]
        right_node = Node(current_state.state, right_move_state)
        right_node.move = "right"
        neighbours.append(right_node)

    # Can tile move up?
    if int(blank_tile / N) != 0:
        up_move_state = current_state.state.copy()
        up_move_state[blank_tile], up_move_state[blank_tile - N] = up_move_state[blank_tile - N], up_move_state[
            blank_tile]
        up_node = Node(current_state.state, up_move_state)
        up_node.move = "up"
        neighbours.append(up_node)

    # Can tile move down?
    if int(blank_tile / N) != N - 1:
        down_move_state = current_state.state.copy()
        down_move_state[blank_tile], down_move_state[blank_tile + N] = down_move_state[blank_tile + N], down_move_state[
            blank_tile]
        down_node = Node(current_state.state, down_move_state)
        down_node.move = "down"
        neighbours.append(down_node)

    return neighbours


# checks to see if the node has been searched already and if new node is a better opition
def neighbour_checker(neighbours, current_state, goal_state, heur):
    for neighbour in neighbours:
        neighbour.g = current_state.g + 1
        if heur == 0:
            neighbour.h = out_of_place_tiles(neighbour.state, goal_state.state)
        else:
            neighbour.h = manhattan_distance(neighbour.state, goal_state.state)
        neighbour.f = neighbour.g + neighbour.h

        for open_state in open_states:
            if neighbour == open_state and neighbour.g < open_state.g:
                open_states.remove(open_state)
                break

        for closed_state in closed_states:
            if neighbour == closed_state and neighbour.g < closed_state.g:
                closed_states.remove(closed_state)
                break

        if neighbour not in closed_states and neighbour not in open_states:
            open_states.append(neighbour)
    return open_states


def a_star(start, goal, heur):
    start_state = Node(None, start)
    start_state.g = start_state.h = start_state.f = 0
    end_state = Node(None, goal)
    end_state.g = end_state.h = end_state.f = 0

    open_states.append(start_state)

    # get current shortest node
    while len(open_states) > 0:
        current_state = open_states[0]
        current_index = 0
        for index, item in enumerate(open_states):
            if item.f < current_state.f:
                current_state = item
                current_index = index

        open_states.pop(current_index)
        closed_states.append(current_state)

        # if end state found find path to it
        if current_state == end_state:
            best_path = []
            current = []
            while current_state.parent is not None:
                current.append(current_state.state)
                current.append(current_state.move)
                best_path.append(current)
                current = []
                for closed in closed_states:
                    if closed.state == current_state.parent:
                        current_state = closed
            return best_path[::-1]  # return the path reserved

        children_paths = neighbours(current_state)
        neighbour_checker(children_paths, current_state, end_state, heur)


def matrix_display(state):
    return ('\n' \
            '+---+---+---+\n' \
            '| %s | %s | %s |\n' \
            '+---+---+---+\n' \
            '| %s | %s | %s |\n' \
            '+---+---+---+\n' \
            '| %s | %s | %s |\n' \
            '+---+---+---+\n' \
            % (state[0], state[1], state[2], state[3], state[4], state[5], state[6], state[7], state[8]))


if __name__ == "__main__":
    running = True
    states_chosen = False
    print("Welcome to my A* algorithm N-puzzle solver")
    print(
        "Enter a states a string of numbers like this : 0,1,2,3,4,5,6,7,8 to represent matrix below and press enter ("
        "Where 0 is the blank space).")
    print(matrix_display([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    while states_chosen is False:
        demo = input("Would you like to see a demo? Enter '0' for no, '1' for quick demo or '2' for slow demo ("
                     "specification demo).")
        if demo == "0":
            start_state = list(map(int, input("Enter start state like example shown above: ").split(",")))
            goal_state = list(map(int, input("Enter goal state like example shown above: ").split(",")))
            if solvable(start_state, goal_state):
                states_chosen = True
                print("Puzzle is solvable!")
            else:
                print("Puzzle isn't solvable, try another one or make sure if correct size with a 0 and same numbers")
        elif demo == "1":
            start_state = [3, 4, 1, 6, 8, 2, 7, 0, 5]
            goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            print("Start State:")
            print(matrix_display(start_state))
            print("End State:")
            print(matrix_display(goal_state))
            states_chosen = True
        elif demo == "2":
            start_state = [7, 2, 4, 5, 0, 6, 8, 3, 1]
            goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            print("Start State:")
            print(matrix_display(start_state))
            print("End State:")
            print(matrix_display(goal_state))
            states_chosen = True
        else:
            print("Please enter 0, 1 or 2 ")
    heur = input("Which heuristic function would you like to use? Enter '0' for Hammering distance and '1' "
                 "for Manhattan distance \n")
    start_time = time.time()
    print("\nSearching... \n")
    ans = (a_star(start_state, goal_state, heur))
    print(matrix_display(start_state))
    for n in ans:
        print("Move the blank title " + n[1])
        print(matrix_display(n[0]))
    print("\nIt takes " + str((len(ans))) + " moves to solve the puzzle. Below you can see time taken:")
    print("--- %s seconds ---" % (time.time() - start_time))
    running = False

"""
This class represents a maze made up of cell objects.

"""

from Cell import Cell
import math


class Maze:

    def __init__(self, n, list_of_chars):
        self.num_rows = n
        self.num_col = n
        self.maze = [['' for row in range(n)] for col in range(n)]
        self.prev_state = None
        list_index = 0
        for i in range(self.num_rows):
            for j in range(self.num_col):
                cost = 1
                if list_of_chars[list_index] == '*':
                    cost = 2
                self.maze[i][j] = Cell(i, j, list_index+1, list_of_chars[list_index], cost, 0, [])
                list_index += 1
        self.current_state = self.maze[0][0]
        self.goal_state = self.maze[n-1][n-1]

    """
    This method returns a list of valid cells to visit next. Searches cannot backtrack.
    :return: List of cells/states
    """
    def get_possible_states(self):
        state_list = []
        removed = []
        r = self.current_state.row
        c = self.current_state.col
        if r-1 >= 0:
            cell = self.maze[r-1][c]
            last = Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path)
            if len(self.current_state.path) > 1 and self.current_state.path[len(self.current_state.path) - 2].loc == cell.loc:
                pass
            else:
                if Maze.verify_neighbor(self.current_state, last):
                    state_list.append(last)
                    last = state_list[len(state_list)-1]
                    last.parent = self.current_state
                    if last.parent is not None:
                        last.path_cost = last.parent.path_cost + last.cost
                        last.path = last.parent.path + [last]
                    if r-2 >= 0:
                        cell2 = self.maze[r-2][c]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if c-1 >= 0:
                        cell2 = self.maze[r - 1][c - 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if c+1 < self.num_col:
                        cell2 = self.maze[r - 1][c + 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if state_list[len(state_list) - 1] is last:
                        removed.append(last)
        if r+1 < self.num_rows:
            cell = self.maze[r+1][c]
            last = Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path)
            if len(self.current_state.path) > 1 and self.current_state.path[len(self.current_state.path) - 2].loc == cell.loc:
                pass
            else:
                if Maze.verify_neighbor(self.current_state, last):
                    state_list.append(last)
                    last.parent = self.current_state
                    if last.parent is not None:
                        last.path_cost = last.parent.path_cost + last.cost
                        last.path = last.parent.path + [last]
                    if r + 2 < self.num_rows:
                        cell2 = self.maze[r + 2][c]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if c - 1 >= 0:
                        cell2 = self.maze[r + 1][c - 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if c + 1 < self.num_col:
                        cell2 = self.maze[r + 1][c + 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if state_list[len(state_list) - 1] is last:
                        removed.append(last)
        if c-1 >= 0:
            cell = self.maze[r][c-1]
            last = Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path)
            if len(self.current_state.path) > 1 and self.current_state.path[len(self.current_state.path) - 2].loc == cell.loc:
                pass
            else:
                if Maze.verify_neighbor(self.current_state, last):
                    state_list.append(last)
                    last.parent = self.current_state
                    if last.parent is not None:
                        last.path_cost = last.parent.path_cost + last.cost
                        last.path = last.parent.path + [last]
                    if c - 2 >= 0:
                        cell2 = self.maze[r][c - 2]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if r - 1 >= 0:
                        cell2 = self.maze[r - 1][c - 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if r + 1 < self.num_rows:
                        cell2 = self.maze[r + 1][c - 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if state_list[len(state_list) - 1] is last:
                        removed.append(last)
        if c+1 < self.num_col:
            cell = self.maze[r][c+1]
            last = Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path)
            if len(self.current_state.path) > 1 and self.current_state.path[len(self.current_state.path) - 2].loc == cell.loc:
                pass
            else:
                if Maze.verify_neighbor(self.current_state, last):
                    state_list.append(last)
                    last.parent = self.current_state
                    if last.parent is not None:
                        last.path_cost = last.parent.path_cost + last.cost
                        last.path = last.parent.path + [last]
                    if c + 2 < self.num_col:
                        cell2 = self.maze[r][c + 2]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if r - 1 >= 0:
                        cell2 = self.maze[r - 1][c + 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if r + 1 < self.num_rows:
                        cell2 = self.maze[r + 1][c + 1]
                        last2 = Cell(cell2.row, cell2.col, cell2.loc, cell2.value, cell2.cost, cell2.path_cost, cell2.path)
                        if Maze.verify_neighbor(last, last2):
                            state_list.append(last2)
                            last2.parent = last
                            last2.path_cost = last2.parent.path_cost + last2.cost
                            last2.path = last2.parent.path + [last2]
                    if state_list[len(state_list) - 1] is last:
                        removed.append(last)

        for i in state_list:
            cnt = 4
            j = 1
            if len(i.path) > self.num_rows**2:
                while cnt+2 <= len(i.path):
                    while j < cnt:
                        if i.path[len(i.path)-j].loc == i.path[len(i.path)-j-cnt].loc:
                            j += 1
                        else:
                            break
                    if j == cnt:
                        removed.append(i)
                    cnt += 2

        for i in removed:
            if i in state_list:
                state_list.remove(i)

        return state_list

    """
    This method updates the previous state to where we are, and the current to our next destination.
    :param prev: Where we are currently.
    :param current: Where we are going next.
    :return: None
    """
    def update_states(self, prev, current):
        self.prev_state = prev
        self.current_state = current


    """
    This is a helper method to verify that a neighbor is an appropriate next state.
    """
    @staticmethod
    def verify_neighbor(state, neighbor):
        i = neighbor

        if state.value is '*':
            state2 = state.interpreted_value
            if state2 is 'a' and i.value is not 'b':
                if i.value is '*':
                    i.interpreted_value = 'b'
                else:
                    return False
            elif state2 is 'b' and i.value is not 'c':
                if i.value is '*':
                    i.interpreted_value = 'c'
                else:
                    return False
            elif state2 is 'c' and i.value is not 'a':
                if i.value is '*':
                    i.interpreted_value = 'a'
                else:
                    return False
        elif state.value is 'a':
            if i.value is not 'b':
                if i.value is '*':
                    i.interpreted_value = 'b'
                else:
                    return False
        elif state.value is 'b':
            if i.value is not 'c':
                if i.value is '*':
                    i.interpreted_value = 'c'
                else:
                    return False
        elif state.value is 'c':
            if i.value is not 'a':
                if i.value is '*':
                    i.interpreted_value = 'a'
                else:
                    return False
        return True

    def manhattan_distance(self, state):
        x = abs(state.row - (self.num_rows - 1))
        y = abs(state.col - (self.num_col - 1))
        return x + y

    def euclidean_distance(self, state):
        x = state.row - (self.num_rows - 1)
        y = state.col - (self.num_col - 1)
        x = x**2
        y = y**2
        return math.sqrt(x+y)

    def display_maze(self):
        for i in range(self.num_rows):
            for j in range(self.num_col):
                print(self.maze[i][j].value, end=" ")
            print()

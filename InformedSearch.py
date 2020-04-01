from timeit import default_timer as timer


class InformedSearch:

    # evaluates based solely on h(n): closest to goal
    @staticmethod
    def greedy(m, h_func):
        t = timer()
        state = m.current_state
        goal = m.goal_state
        deadends = 0
        visited = list()
        frontier = PriorityQueue()
        state.path += [state]
        if h_func == 'm':
            cost = m.manhattan_distance(state)
        else:
            cost = m.euclidean_distance(state)
        frontier.push(Node(state, cost))
        if state.loc is goal.loc:
            return InformedSearch.display_solution("Greedy" + " " + h_func, 1, 0, [state], state.path_cost)
        while frontier.size() > 0:
            if timer()-t > 5:
                break
            node = frontier.pop()
            state = node.data
            if state is not m.current_state:
                m.update_states(m.current_state, state)
            if state.parent is not None and state.parent.loc is not visited[len(visited)-1].loc:
                visited.append(state.parent)
            visited.append(state)
            neighbors = m.get_possible_states()
            for i in neighbors:
                if i.loc is goal.loc:
                    if i.parent is not None and i.parent.loc is not visited[len(visited) - 1].loc:
                        visited.append(state.parent)
                    return InformedSearch.display_solution("Greedy" + " " + h_func, len(i.path), len(visited), i.path, i.path_cost)
                if h_func == 'm':
                    cost = m.manhattan_distance(i)
                else:
                    cost = m.euclidean_distance(i)
                frontier.push(Node(i, cost))
            if len(neighbors) == 0:
                deadends += 1
            if deadends > m.num_rows**5:
                break
        return InformedSearch.display_solution("Greedy" + " " + h_func, 0, len(visited), None, 0)

    @staticmethod
    def a_star(m, h_func):
        t = timer()
        state = m.current_state
        goal = m.goal_state
        deadends = 0
        visited = list()
        frontier = PriorityQueue()
        state.path += [state]
        if h_func == 'm':
            cost = m.manhattan_distance(state)
        else:
            cost = m.euclidean_distance(state)
        frontier.push(Node(state, cost + state.path_cost))
        if state.loc is goal.loc:
            return InformedSearch.display_solution("A*" + " " + h_func, 1, 0, [state], state.path_cost)
        while frontier.size() > 0:
            if timer()-t > 5:
                break
            node = frontier.pop()
            state = node.data
            if state is not m.current_state:
                m.update_states(m.current_state, state)
            if state.parent is not None and state.parent.loc is not visited[len(visited) - 1].loc:
                visited.append(state.parent)
            visited.append(state)
            neighbors = m.get_possible_states()
            for i in neighbors:
                if i.loc is goal.loc:
                    if i.parent is not None and i.parent.loc is not visited[len(visited) - 1].loc:
                        visited.append(state.parent)
                    return InformedSearch.display_solution("A*" + " " + h_func, len(i.path), len(visited), i.path, i.path_cost)
                if h_func == 'm':
                    cost = m.manhattan_distance(i) + i.path_cost
                else:
                    cost = m.euclidean_distance(i) + i.path_cost
                frontier.push(Node(i, cost))
            if len(neighbors) == 0:
                deadends += 1
            if deadends > m.num_rows**5:
                break
        return InformedSearch.display_solution("A*" + " " + h_func, 0, len(visited), None, 0)

    @staticmethod
    def gradient_descent(m, h_func):
        t = timer()
        state = m.current_state
        goal = m.goal_state
        deadends = 0
        visited = list()
        frontier = PriorityQueue()
        state.path += [state]
        if h_func == 'm':
            cost = m.manhattan_distance(state)
        else:
            cost = m.euclidean_distance(state)
        node = Node(state, cost)
        if state.loc is goal.loc:
            return InformedSearch.display_solution("Gradient Descent" + " " + h_func, 1, 0, [state], state.path_cost)
        while node is not None:
            if timer()-t > 5:
                break
            state = node.data
            if state is not m.current_state:
                m.update_states(m.current_state, state)
            if state.parent is not None and state.parent.loc is not visited[len(visited) - 1].loc:
                visited.append(state.parent)
            visited.append(state)
            neighbors = m.get_possible_states()
            for i in neighbors:
                if i.loc is goal.loc:
                    if i.parent is not None and i.parent.loc is not visited[len(visited) - 1].loc:
                        visited.append(state.parent)
                    return InformedSearch.display_solution("Gradient Descent" + " " + h_func, len(i.path), len(visited), i.path, i.path_cost)
                if h_func == 'm':
                    cost = m.manhattan_distance(i)
                else:
                    cost = m.euclidean_distance(i)
                frontier.push(Node(i, cost))
            node = frontier.pop()
            frontier.clear()
            if len(neighbors) == 0:
                deadends += 1
            if deadends > m.num_rows ** 5:
                break
        return InformedSearch.display_solution("Gradient Descent" + " " + h_func, 0, len(visited), None, 0)

    """
    This method returns a string of the values returned from the search methods to aid in file writing.
    """
    @staticmethod
    def display_solution(search, sol_length, visited, solution, cost):
        solution_str = "" + search + ", " + str(sol_length) + ", " + str(visited) + ", "
        if solution is not None:
            for i in solution:
                solution_str += str(i)
                solution_str += ", "
        else:
            solution_str += "Nil  "
        solution_str += " "
        solution_str += str(cost)
        return solution_str


class Node:

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.queue = list()

    def push(self, node):
        if self.size() == 0:
            self.queue.append(node)
        else:
            for i in range(self.size()):
                if node.priority <= self.queue[i].priority and node.data.loc == self.queue[i].data.loc:
                    self.queue[i] = node
                    return
                if node.priority >= self.queue[i].priority:
                    if i == self.size()-1:
                        self.queue.insert(i+1, node)
                        return
                    else:
                        continue
                else:
                    self.queue.insert(i, node)
                    return

    def pop(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = list()

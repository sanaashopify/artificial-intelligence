import sys


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        # no path cost because can be calculated later


class StackFrontier():  # stores all frontier data (LIFO)
    def __init__(self):
        self.frontier = []  # creates a list for the frontier

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):  # checks if frontier contains state
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]  # last item
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):  # inherits stack frontier

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]  # first item
            self.frontier = self.frontier[1:]
            return node


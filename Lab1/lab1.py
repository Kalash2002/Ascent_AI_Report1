# CS362 Artificial Intelligence
# Lab assignment 1: Combined code for problems (B) and (E)

from collections import defaultdict as dd
import copy
from guppy import hpy   # for memory requirement profiling
import time             # for runtime profiling

h = hpy()

class Node:

    distance = dd(lambda: None)

    def __init__(self, config):
        self.config = copy.deepcopy(config)
        if Node.distance[str(self.config)] == None:
            Node.distance[str(self.config)] = -1

    def set_distance(self, dist):
        Node.distance[str(self.config)] = dist

    def get_distance(self):
        return Node.distance[str(self.config)]

    # method to find the void/empty space in an 8-puzzle configuration
    def find_void(self):
        for i in range(3):
            for j in range(3):
                if self.config[i][j] == 0:
                    return i, j

    # methods to move the void in an 8-puzzle configuration

    def move_up(self, i, j):
        config = copy.deepcopy(self.config)
        config[i][j], config[i-1][j] = config[i-1][j], config[i][j]
        return Node(config)

    def move_down(self, i, j):
        config = copy.deepcopy(self.config)
        config[i][j], config[i+1][j] = config[i+1][j], config[i][j]
        return Node(config)

    def move_left(self, i, j):
        config = copy.deepcopy(self.config)
        config[i][j], config[i][j-1] = config[i][j-1], config[i][j]
        return Node(config)

    def move_right(self, i, j):
        config = copy.deepcopy(self.config)
        config[i][j], config[i][j+1] = config[i][j+1], config[i][j]
        return Node(config)

    # method to generate children nodes
    def get_children(self):
        i, j = self.find_void()
        children = []
        if i == 0:
            if j == 0:
                children.append(self.move_down(i, j))
                children.append(self.move_right(i, j))
            elif j == 1:
                children.append(self.move_down(i, j))
                children.append(self.move_right(i, j))
                children.append(self.move_left(i, j))
            else:
                children.append(self.move_down(i, j))
                children.append(self.move_left(i, j))
        elif i == 1:
            if j == 0:
                children.append(self.move_down(i, j))
                children.append(self.move_right(i, j))
                children.append(self.move_up(i, j))
            elif j == 1:
                children.append(self.move_down(i, j))
                children.append(self.move_right(i, j))
                children.append(self.move_left(i, j))
                children.append(self.move_up(i, j))
            else:
                children.append(self.move_down(i, j))
                children.append(self.move_left(i, j))
                children.append(self.move_up(i, j))
        else:
            if j == 0:
                children.append(self.move_right(i, j))
                children.append(self.move_up(i, j))
            elif j == 1:
                children.append(self.move_right(i, j))
                children.append(self.move_left(i, j))
                children.append(self.move_up(i, j))
            else:
                children.append(self.move_left(i, j))
                children.append(self.move_up(i, j))
        return children

# function to implement 8-puzzle instance generation
def eight_puzzle(config, depth):
    frontier, limit_reached = [], False
    print('\nStart state configuration:\n')
    for row in config:
        print(row)
    start_time = time.time()
    start_node = Node(config)
    start_node.set_distance(0)
    frontier.append(start_node)
    while len(frontier) != 0:
        parent = frontier.pop(0)
        children = parent.get_children()
        for child in children:
            if child.get_distance() == -1:
                child.set_distance(parent.get_distance() + 1)
                if child.get_distance() == depth + 1:
                    limit_reached = True
                    break
                else:
                    frontier.append(child)
        if limit_reached:
            instances = [x.config for x in [parent] + frontier]
            break
    end_time = time.time()
    runtime = end_time - start_time
    memory_required = h.heap().size

    # COMMENT/UNCOMMENT THE FOLLOWING SNIPPET TO TOGGLE PRINTING THE GENERATED INSTANCES
    print('\n')
    print(f'8-Puzzle instances generated at depth {depth}:')
    for instance in instances:
        print('\n')
        for row in instance:
            print(row)

    return runtime, memory_required

if __name__ == '__main__':
    print('\n8-Puzzle Instance Generation')
    print('\nNOTE:')
    print('1. Each of the following input lines for the configuration require 3 space separated entries.')
    print('2. Valid configuration values for entries are 0-8 (each entry should be unique), with 0 representing the void/empty space.')

    # COMMENT/UNCOMMENT THE FOLLOWING SNIPPET TO TOGGLE USER INPUT FOR START NODE CONFIGURATION
    config = []
    print('\nStart state input:\n')
    for i in range(3):
        row = [int(x) for x in input('Enter numbers for row ' + str(i + 1) + ': ').split()]
        config.append(row)

    # config = [[7, 2, 8], [6, 5, 3], [0, 1, 4]]  # COMMENT/UNCOMMENT THIS LINE TO TOGGLE HARD-CODED START STATE CONFIGURATION
    depth = int(input('\nEnter depth value: '))
    runtime, memory_required = eight_puzzle(config, depth)
    print('\nTotal execution time: ' + str(runtime) + ' seconds')
    print('Total size: ' + str(memory_required) + ' bytes\n')
from room import Room
from player import Player
from world import World
from util import Queue, Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# # map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

def traversePath(graph):
    # initialize empty maze and rooms array
    maze = []
    rooms = []

    # make a set to keep track of where we've been
    visited = set()

    # set maze starting point 0
    maze.append(0)

    # start until all rooms have been visited
    # while length of visited is less than length of map graph
    while len(visited) < len(graph):
        # pop the first item and set in current_room
        current_room = maze[-1]
        # add to set of visited rooms
        visited.add(current_room)
        # add to connections & declare free connects
        connect = graph[current_room][1]
        free_connections = []

        for curr_room, unchecked_room in connect.items():
            # if unchecked room is not in visited list
            if unchecked_room not in visited:
                # do thing and add in free_connections
                free_connections.append(unchecked_room)
        
        # if there are freee connections, add them to room and maze
        if len(free_connections) > 0:
            room = free_connections[0]
            maze.append(free_connections[0])
        else:
            room = maze[-2]
            maze.pop()
        
        # if no where else to go, go back to previous room
        for previous_room, exit_door in connect.items():
            if exit_door == room:
                rooms.append(previous_room)
        
    return rooms

traversal_path = traversePath(room_graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
print(f"MOVES MADE: {len(traversal_path)}")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

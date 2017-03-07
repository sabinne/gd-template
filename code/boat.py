#!/usr/bin/python
# filename: boat.py

room1 = ('room 1', 'a pale, modern, and metallic looking room', 'you awake in this cold room, no lights illuminate the surroundings, and you have no memory of your personal history, the area must be explored, to figure out what is going on')
centerRightWingHall = ('centerRightWingHall', 'a hallway with windows on the left wall, which is slightly askew angle-wise, outside a vast expanse of ocean is visible. I must be on a boat', 'nothing has changed in this hall')
room2 = ('room2', 'this room is identicle to room1, but there is a ripped up poster on the wall opossite to the door, its contents are not visible due to is rips', 'the room has not changed, the poster remains, and the bed is untouched')
aMap = ('a map', 'this map hangs on the wall, showing a diagram of the right side of the ship, it is huge, and weaponry is also identified in certain areas, the door to the right of the map is labeled centerRightWingHall exit, that must be my way outside', 'this map has not changed')
exit = ('exit', 'the door has an exit sign above it, when pushed it will only budge open enough to see that it is hopelessly blockaded by piles of rubble')

transitions = {
    room1: (centerRightWingHall,),
    centerRightWingHall: (aMap, exit, room2, room1),
    aMap: (centerRightWingHall, exit),
    exit: (centerRightWingHall, aMap),
    room2: (centerRightWingHall,),
}

location = room1

while True:
    print location[1]
    print 'you can explore these certain places:'

    for (i, t) in enumerate(transitions[location]):
        print i + 1, t[0]

    choice = int(raw_input('Choose one '))
    location = transitions[location][choice - 1]

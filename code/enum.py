#!/usr/bin/python3

import enum

class Weather(enum.Enum):
 rain = 1
 sun = 2
 wind = 3
 thunder = 4
 cloud = 5

print ("this is the enum string of one member of an enum class, and its class :", end="")
print (Weather.rain)

print ("this is the representation of one member of an enum class :", end="")
print repr(Weather.thunder))

print ("this is the type of one member of an enum class :", end="")
print type(Weather.sun))

print ("this is the name of one member of an enum class :", end="")
print (Weather.wind.name)

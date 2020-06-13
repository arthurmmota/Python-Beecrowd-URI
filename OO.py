import time
import sys
import os
import math
import random
import pickle
import urllib
import re
import cgi
import socket

class Player:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, carta(c1), age):
        self.name = name
        self.age = age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)



class Carta:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Jogo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))

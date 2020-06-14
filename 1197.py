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

while True:
    try:

        entrada = input()
        entrada2 = entrada.split(" ")

        v = int(entrada2[0])
        t = int(entrada2[1])

        print("{}".format(v * t * 2))

    except EOFError:
        break

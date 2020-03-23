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
flag = 1
while flag != 0:
    k = int(input())
    if k != 0:
        coord = input()
        coord = [int(s) for s in coord.split(' ')]
        for x in range(0,k):
            casa = input()
            casa = [int(s) for s in casa.split(' ')]
            if casa[0] == coord[0] or casa[1] == coord[1]:
                print("divisa")
            elif casa[0] > coord[0] and casa[1] > coord[1]:
                print("NE")
            elif casa[0] < coord[0] and casa[1] > coord[1]:
                print("NO")
            elif casa[0] > coord[0] and casa[1] < coord[1]:
                print("SE")
            elif casa[0] < coord[0] and casa[1] < coord[1]:
                print("SO")
    else:
        flag = 0
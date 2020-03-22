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
import statistics

entrada = int(input())
for x in range(0,entrada):
    idades = input()
    idades = [int(s) for s in idades.split(' ')]
    del(idades[0])
    print('Case %d: %d' % ((x+1),statistics.median(idades)))
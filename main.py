#!/usr/bin/python3.8

# MADE BY
# Kovács Norbert - mfw.kovcs.norbert@gmail.com
#  _____      _ _ _  __
# |  __ \    | | (_)/ _|
# | |  \/ ___| | |_| |_ _ __ ___  ___
# | | __ / _ \ | | |  _| '__/ _ \/ _ \
# | |_\ \  __/ | | | | | | |  __/  __/
#  \____/\___|_|_|_|_| |_|  \___|\___|
#
# &&
#    __   _____      _  _  _
#    \ \ |___ /   __| || || |
#     \ \  |_ \  / _` || || |_
#  /\_/ / ___) || (_| ||__   _|
#  \___/ |____/  \__,_|   |_|

import time, random
import os
from sys import platform



class progressBar_Signal():
    def __init__(self):
        self.barStatus = ["[*  ]","[ * ]", "[  *]"]
        self.indexer = 0
        self.position = 0


    def signal(self):
        self.indexer += 1
        if(self.indexer > 0 and self.indexer <= 200000):
            self.position = 0
        elif(self.indexer > 200000 and self.indexer <= 400000):
            self.position = 1
        elif(self.indexer > 400000 and self.indexer <= 600000):
            self.position  = 2

        if(self.indexer == 600000):
            self.indexer = 0
        print(self.barStatus[self.position], end="\r")

pb = progressBar_Signal()

def linearSearch(list, searched):
    for i in range(len(list)):
        pb.signal()
        if(list[i] == searched):
            print("\n Found!")
            return i
    print("\nNot found!")
    return -1

def generateList(length):
    result = []
    for i in range(length):
        pb.signal()
        result.append(random.randint(1,10000000))
    print("\n Generate Done")
    return result

if __name__ == '__main__':
    list = generateList(1000000)
    print(linearSearch(list, 5))

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

import time
import os


class progressBar():
    def Counter(self, *args):
        if args:
            for i in range(len(args) + 1):
                length = len(args)
                percent = i / length * 100
                print(">> Loading:", int(percent),
                      "%", i, "/", length, end="\r")
                time.sleep(0.05)
            print()
        else:
            print("Error, no arguments given.")

    def Bar(self, *args):
        if args:
            barStart = "["
            barEnd = "]"
            barFill = "-"
            barLoad = "#"
            barSize = 100

            for i in range(len(args) + 1):
                length = len(args)
                percent = i / length * 100
                print(barStart, end="")
                for j in range(int(percent)):
                    print(barLoad, end="")
                for k in range(barSize - int(percent)):
                    print(barFill, end="")
                print(barEnd, i, "/", length, end="\r")
                time.sleep(0.05)
            print()
        else:
            print("Error, no arguments given.")


if __name__ == '__main__':
    pb = progressBar()
    pb.Bar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "kiscica", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
           "kiscica", "anyad", 12, 12, 123, 3124, 12523)
    pb.Counter(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               "kiscica", "anyad", 12, 12, 123, 3124, 12523)

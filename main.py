#!/usr/bin/python3.8

# MADE BY
#  _____      _ _ _  __
# |  __ \    | | (_)/ _|
# | |  \/ ___| | |_| |_ _ __ ___  ___
# | | __ / _ \ | | |  _| '__/ _ \/ _ \
# | |_\ \  __/ | | | | | | |  __/  __/
#  \____/\___|_|_|_|_| |_|  \___|\___|
#
# Kovács Norbert - mfw.kovcs.norbert@gmail.com

import time, os

class progressBar():
    def draw(self, mode):
        if(mode == 0):
            for i in range(101):
                print(">> Betöltés:", i, "%", end="\r")
                time.sleep(0.01)
            print()
        elif(mode == 1):
            barStart = "["
            barEnd   = "]"
            barfill  = "-"
            barLoad  = "#"

            fillCounter = 0
            barSize = 50
            for i in range(barSize + 1):
                print(barStart, end="")
                for i in range(fillCounter):
                    print(barLoad, end="")
                for i in range(barSize - fillCounter):
                    print(barfill, end="")
                print(barEnd, end="\r")
                fillCounter += 1
                time.sleep(0.05)
            print()


def main():
    pb = progressBar()

    pb.draw(1)
    pb.draw(0)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

"""
    aptx11depss
    Downloads all x11 dependencies for qt from
    https://doc.qt.io/qt-6/linux-requirements.html
"""

import os

if __name__ == "__main__":
    packages = set()    
    with open("x11packages.txt", "r") as f:
        for line in f:
            packages.add(line.strip())
    for pack in packages:
        os.system(f"sudo apt install {pack}")

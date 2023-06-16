#!/usr/bin/env python3

"""
    aptx11depss
    Downloads all x11 dependencies for qt from
    https://doc.qt.io/qt-6/linux-requirements.html
"""

import os

packages = [
    "libfontconfig1-dev",
    "libfreetype6-dev",
    "libx11-dev",
    "libx11-xcb-dev",
    "libxext-dev",
    "libxfixes-dev",
    "libxi-dev",
    "libxrender-dev",
    "libxcb1-dev",
    "libxcb-cursor-dev",
    "libxcb-glx0-dev",
    "libxcb-keysyms1-dev",
    "libxcb-image0-dev",
    "libxcb-shm0-dev",
    "libxcb-icccm4-dev",
    "libxcb-sync-dev",
    "libxcb-xfixes0-dev",
    "libxcb-shape0-dev",
    "libxcb-randr0-dev",
    "libxcb-render-util0-dev",
    "libxcb-util-dev",
    "libxcb-xinerama0-dev",
    "libxcb-xkb-dev",
    "libxkbcommon-dev",
    "libxkbcommon-x11-dev",
]

if __name__ == "__main__":
    for pack in packages:
        os.system(f"sudo apt install {pack}")

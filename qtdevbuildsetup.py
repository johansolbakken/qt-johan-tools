#!/usr/bin/env python3

import argparse
import os
import time


class State:
    def __init__(self) -> None:
        self.src = ""
        self.dst = ""
        self.qtbase = ""

    def print(self):
        print("State", self.__dict__)


def setup_qt_base(state: State):
    if os.path.exists("qtbase"):
        print(" - qtbase exists. skipping.")
        state.qtbase = os.path.abspath("qtbase")
        return

    os.makedirs("qtbase")
    state.qtbase = os.path.abspath("qtbase")

    os.chdir("qtbase")
    os.system(f"{state.src}/qtbase/configure -developer-build -nomake tests")
    os.system("ninja")
    os.chdir("..")


def setup_qt_module(state: State, name: str):
    if os.path.exists(name):
        print(f" - module {name} exists. skipping.")
        return
    os.mkdir(name)
    os.chdir(name)
    os.system(f"{state.qtbase}/bin/qt-configure-module {state.src}/{name}")
    os.system("ninja")
    os.chdir("..")


def setup_examples(state: State, name: str):
    path = "examples/" + name
    if os.path.exists(path):
        print(f" - examples {name} exists. skipping.")
        return
    qmake = state.qtbase + "/bin/qmake"
    example_pro = state.src + "/" + name + "/examples/examples.pro"
    os.makedirs(path)
    old_path = os.getcwd()
    os.chdir(path)
    os.system(f"{qmake} {example_pro}")
    os.system("make")
    os.chdir(old_path)


def main():
    argparser = argparse.ArgumentParser(
        prog="qtdevbuildsetup"
    )
    argparser.add_argument("src")
    argparser.add_argument("dst")

    args = argparser.parse_args()

    state = State()
    state.src = args.src
    state.dst = args.dst

    start_time = time.time()

    os.makedirs(name=state.dst, exist_ok=True)
    state.dst = os.path.abspath(args.dst)
    os.chdir(state.dst)

    setup_qt_base(state)

    modules = [
        "qtshadertools",
        "qtdeclarative",
        "qtquick3d",
        "qtquick3dphysics",
        "qtquicktimeline"
    ]

    for module in modules:
        setup_qt_module(state, module)

    examples = [
        "qtquick3d",
        "qtquick3dphysics"
    ]

    for example in examples:
        setup_examples(state, example)

    end_time = time.time()
    seconds = end_time - start_time
    minutes = int(seconds) // 60
    seconds -= minutes * 60
    print("---------------------------")
    print(f"Building Qt took {minutes} minutes and {int(seconds)} seconds")


if __name__ == "__main__":
    main()

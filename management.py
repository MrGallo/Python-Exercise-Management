"""
Issues:
- add section (or main concept?)
- add prerequisets
"""


from typing import List, Dict, Callable, Tuple, Union
import json
from itertools import count

import management.series_menu as series_menu
import management.chapter_menu as chapter_menu

from management.types import *
import management.settings as settings



class Menu:
    def __init__(self, name: str, db: Database):
        self.name = name
        self.db = db
        self._numbered_options: List[Tuple[str, Callable]] = []
        self._lettered_options: List[Tuple[str, Callable]] = []
    
    def add_numbered_option(self, label, callback: Union['Menu', Callable]):
        self._numbered_options.append((label, callback))
    
    def get_numbered_options(self) -> MenuOptions:
        return dict(zip(count(1), self._numbered_options))
    
    def add_lettered_option(self, letter:str, label: str, callback: Union['Menu', Callable]):
        self._lettered_options.append((letter, label, callback))
    
    def get_lettered_options(self) -> MenuOptions:
        options = {}
        for letter, label, callback in self._lettered_options:
            options[letter] = (label, callback)
        return options

    def get_options(self):
        return self.get_numbered_options(), self.get_lettered_options()


class MainMenu(Menu):
    def __init__(self, name: str, db: Database):
        super().__init__(name, db)
        self.add_numbered_option("Testing 123", self.test("hello"))
        self.add_lettered_option("a", "[A]dd series", self.add_series)



    def add_series(self):
        print("adding series.")

    def test(self, msg: str):
        def inner():
            print(msg)
        return inner
    

class ShowSeries(Menu):
    def __init__(self, name: str, db: Database):
        super().__init__(name, db)
        series = db["exercises"][self.name]
        for chapter in series:
            print(chapter.keys())


def main():
    data = load_database(settings.DATABASE_FILE)

    main_menu = MainMenu("Main Menu", data)
    current_menu = main_menu

    while True:
        numbered_options = current_menu.get_numbered_options()
        lettered_options = current_menu.get_lettered_options()
        print_title(current_menu.name)

        show_numbered_menu(numbered_options)
        print()
        show_lettered_menu(lettered_options)
        label, func = get_menu_choice({**numbered_options, **lettered_options})

        # print_title(label, "-")
        func()


def print_title(title: str, underline: str = "=", padding_top: bool = True):
    if padding_top is True:
        print()
    print(title)
    print(underline * len(title))
    print()


def show_numbered_menu(menu_options) -> None:
    for i, (label, _) in menu_options.items():
        print(f"[{i}] {label}")


def show_lettered_menu(menu_options) -> None:
    for label, _ in menu_options.values():
        print(f"{label}")


def get_menu_choice(
        menu_options: Dict[int, Tuple[str, Callable]]) -> Tuple[str, Callable]:
    while True:
        choice = input("> ")
        try:
            choice = int(choice)
        except ValueError:
            pass

        try:
            label, func = menu_options[choice]
        except KeyError:
            print("Invalid menu option.")
        else:
            break

    return label, func


def load_database(filename: str) -> Database:
    with open(filename, 'r') as f:
        data = json.load(f)

    return data



if __name__ == "__main__":
    main()

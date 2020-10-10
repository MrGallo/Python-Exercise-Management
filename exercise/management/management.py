"""
Issues:
- add section (or main concept?)
- add prerequisets
"""


from typing import List, Dict, Callable, Tuple
import json

import exercise.management.main_menu as main_menu

Exercise = Dict[str, str]


def main():
    data = load_exercises('exercise/management/exercises.json')
    exercises = data["exercises"]
    print(f"loaded {len(exercises)} exercises.")

    current_screen_label = "Main Menu"
    main_menu_options = main_menu.get_menu_options(exercises)

    while True:
        print_title(current_screen_label)

        show_menu(main_menu_options)
        label, func = get_menu_choice(main_menu_options)

        print_title(label, "-")
        func()

def print_title(title: str, underline: str = "=", padding_top: bool = True):
    if padding_top is True:
        print()
    print(title)
    print(underline * len(title))
    print()


def show_menu(menu_options) -> None:
    for i, (label, _) in menu_options.items():
        print(f"[{i}] {label}")


def get_menu_choice(
        menu_options: Dict[int, Tuple[str, Callable]]) -> Tuple[str, Callable]:
    while True:
        try:
            choice = int(input("> "))
            label, func = menu_options[choice]
        except ValueError:
            print("Not a number.")
        except KeyError:
            print("Invalid menu option.")
        else:
            break

    return label, func


def load_exercises(filename: str) -> List[Exercise]:
    with open(filename, 'r') as f:
        data = json.load(f)

    return data



if __name__ == "__main__":
    main()

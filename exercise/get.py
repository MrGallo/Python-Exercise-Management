import json
import os
from collections import defaultdict
from itertools import count
from typing import Dict, List, Tuple

import requests

from exercise.utils import print_title

Exercise = Dict[str, str]
EXERCISES_URL = "https://raw.githubusercontent.com/MrGallo/Python-Exercises/master/exercise/management/exercises.json"


def main():
    print("Get new exercise.")
    start_new_exercise()


def start_new_exercise():
    # get exercises
    exercises = get_exercises(EXERCISES_URL)

    # start new exercise
    choice, chosen_exercise = select_exercise(exercises)
    write_exercise_to_files(choice, chosen_exercise)

    # start_new_session(chosen_exercise)

    print("\nEXERCISE DESCRIPTION can be found in the description.md file.")
    print("To view a formatted version of that file, click the \"preview\" in the top right corner after you open it.")

    print("\nATTEMPT SOLUTION by working in main.py")

    print_title("Menu options", "-")
    print("[1] Test your solution")
    print("[2] Attempt a different exercise")
    print()
        
    OPTIONS_FUNC = defaultdict(invalid_menu_choice)
    OPTIONS_FUNC.update({
        "1": test_solution,
        "2": not_implemented
    })


    while True:
        choice = input("> ")

        if OPTIONS_FUNC[choice]():
            break

    return 1


def invalid_menu_choice():
    def inner():
        print("Invalid menu choice")
        return 0
    return inner


def test_solution():
    while True:
        result = os.system(f"pytest test_main.py -p no:cacheprovider")
        print(f"{result = }")
        print()
        if result != 0:
            # update_session("incorrect")
            choice = input("Try again? [y/n]").lower()
            if choice == "y":
                os.system("clear")
                continue
        else:
            pass
            # update_session("completed")
        break
    
    return 1
    # 0 pass
    # 256 fail
    # 512 import error, syntax
    # 1024 File not found


def not_implemented():
    print("Not implemented")
    return 0


def get_exercises(url: str) -> List[Exercise]:
    request = requests.get(url)
    string_data = request.text
    data = json.loads(string_data)
    return data["exercises"]


def select_exercise(exercises: List[Exercise]) -> Tuple[int, Exercise]:
    """
    
    Returns:
        Choice integer according to the menu options
        and the chosen exercise.
    """
    print("Select an exercise to begin.\n")
    exercise_mapping = dict(zip(count(1), exercises))

    # Print Menu options
    # completions = get_exercise_completions()
    for n, ex in exercise_mapping.items():
        # done = completions[ex["name"]]
        done = 0
        if done > 0:
            remaining = done
            bright_stars = remaining // 9
            remaining = remaining % 9
            stars = remaining // 3
            single = remaining % 3

            recognition = ("🌟 " * bright_stars +
                           "⭐ " * stars +
                           "✔️ " * single)
            
            print(f"[{n}] {ex['name']} {recognition}")
        else:
            print(f"[{n}] {ex['name']}")

    print()

    while True:
        try:
            choice = int(input("> "))
            chosen_exercise = exercise_mapping[choice]
        except ValueError:
            print("Invalid input, must be a number.")
        except KeyError:
            print(f"Not a valid choice. Must be 1-{len(files_mapping)} inclusive.")
        else:
            break

    print()
    print(f"You chose '{chosen_exercise['name']}'")
    return choice, chosen_exercise


def write_exercise_to_files(choice: int, exercise: Exercise) -> None:
    # Write tests to test file
    with open('test_main.py', 'w') as f:
        f.write("# Do not modify this file.\n")
        f.write(exercise["tests"])

    # Write starter code into main.py
    with open('main.py', 'w') as f:
        f.write(exercise["starter_code"])

    # Write description to description.md
    with open('description.md', 'w') as f:
        f.write("\n\n\n[//]: # (     CLICK THE PREVIEW BUTTON   --->)\n\n\n\n\n")
        f.write(f"# Exercise {choice}: {exercise['name']}\n")
        f.write(exercise["description"])


if __name__ == "__main__":
    main()

from typing import List, Dict, Callable, Tuple, Union, Optional
import json
from itertools import count

from management.types import *
from management.utils import *
import management.settings as settings


def load_database(filename: str) -> Database:
    with open(filename, 'r') as f:
        data = json.load(f)

    return data

db = load_database(settings.DATABASE_FILE)


def main():
    global db

    while True:
        series_list = get_series_list()
        for i, series_name in enumerate(series_list, 1):
            print(f"[{i}] {series_name}")
        
        print()
        print("[a]dd series")
        print("[q]uit")
        
        print()
        choice = None
        while True:
            choice = input("> ").lower()
            if choice == "a":
                add_series()
                break
            elif choice == "q":
                return -1
            else:
                try:
                    choice = int(choice) - 1
                    assert choice >= 0 and choice < len(series_list)
                except (ValueError, AssertionError):
                    print("Invalid option")
                else:
                    result = show_series(series_list[choice])
                    if result == -1:
                        return -1
                    break
    
        print()


def get_series_list() -> List[str]:
    global db

    try:
        return db["series_list"]
    except KeyError:
        db["series_list"] = []
        write_database_to_file(db, settings.DATABASE_FILE)
        return db["series_list"]


def get_chapter_list(series_name: str) -> List[str]:
    global db

    series = db[series_name]
    try:
        return series["chapter_list"]
    except KeyError:
        series["chapter_list"] = []
        write_database_to_file(db, settings.DATABASE_FILE)
        return series["chapter_list"]


def show_series(series_name: str):
    global db

    while True:
        series = db[series_name]
        chapter_list = get_chapter_list(series_name)

        print()
        print(series_name)
        for i, chapter in enumerate(chapter_list, 1):
            print(f"[{i}] {chapter}")
        
        print()
        print(f"[e]dit series name ({series_name})")
        print("[a]dd chapter")
        print("[b]ack")
        print("[q]uit")
        
        print()
        choice = None
        while True:
            choice = input("> ").lower()
            if choice == "a":
                add_chapter(series_name)
            elif choice == "e":
                series_name = edit_series_name(series_name)
            elif choice == "q":
                return -1
            elif choice == "b":
                return 0
            else:
                try:
                    choice = int(choice) - 1
                    assert choice >= 0 and choice < len(chapter_list)
                except (ValueError, AssertionError):
                    print("Invalid option")
                    continue
                else:
                    result = show_chapter(series_name, chapter_list[choice])
                    if result == -1:
                        return -1
                    break
            break

        print()


def show_chapter(series_name: str, chapter_name: str):
    global db

    while True:
        series = db[series_name]
        exercise_list = series[chapter_name]

        print()
        print(series_name)
        print(chapter_name)
        for i, exercise in enumerate(exercise_list, 1):
            print(f"[{i}] {exercise['name']}")
        
        print()
        print(f"[e]dit chapter name ({chapter_name})")
        print("[a]dd exercise")
        print("[b]ack")
        print("[q]uit")
        
        print()
        choice = None
        while True:
            choice = input("> ").lower()
            if choice == "a":
                add_exercise(exercise_list)
            elif choice == "e":
                chapter_name = edit_chapter_name(chapter_name)
            elif choice == "q":
                return -1
            elif choice == "b":
                return 0
            else:
                try:
                    choice = int(choice) - 1
                    assert choice >= 0 and choice < len(chapter_list)
                except (ValueError, AssertionError):
                    print("Invalid option")
                    continue
                else:
                    result = show_exercise(exercise_list[choice])
                    if result == -1:
                        return -1
                    break
            break

        print()


def add_series():
    global db

    series_list = get_series_list()

    series_name, insert = confirm_item_name_and_location("series", series_list)

    insert_series(series_name, insert)
    write_database_to_file(settings.DATABASE_FILE)
    return 0

    
def add_chapter(series_name: str):
    global db

    chapter_list = get_chapter_list(series_name)

    chapter_name, insert = confirm_item_name_and_location("chapter", chapter_list)

    insert_chapter(series_name, chapter_name, insert)
    write_database_to_file(settings.DATABASE_FILE)
    return 0


def confirm_item_name_and_location(item_name: str, existing_items: List[str]):
    while True:
        name = input(f"Enter the name of the new {item_name}: ")
        
        insert = None
        while True:
            if len(existing_items) > 0:
                insert = input(f"Insert? 0-{len(existing_items)-1} [append]")
                try:
                    insert = int(insert)
                except ValueError:
                    insert = None
                    break
                else:
                    if insert >= 0 and insert < len(existing_items):
                        break       

        location = "the end" if insert is None else insert
        print()
        print(f"[ENTER] Confirm add '{name}' to {location}")
        print("[r]edo")

        choice = input("> ")

        if choice == "":
            break

    return name, insert


def edit_series_name(series_name):
    global db

    series_list = get_series_list()
    index = series_list.index(series_name)

    print(f"Editing {series_name}.")
    new_name = input("Change name to: ")
    insert_series(new_name, index)

    # swap contents
    db[new_name] = db[series_name]
    del db[series_name]
    del db["series_list"][index+1]

    write_database_to_file(settings.DATABASE_FILE)

    return new_name


def insert_series(series_name: str,
                  index: Optional[int] = None) -> None:
    global db

    series_list = get_series_list()

    for existing_name in series_list:
        if series_name.lower() == existing_name.lower():
            raise UniqueNameConstraintError("A series with that name already exists.")

    if index is not None:
        series_list.insert(index, series_name)
    else:
        series_list.append(series_name)
    
    db[series_name] = {"chapter_list": []}


def insert_chapter(series_name: str,
                   chapter_name: str,
                   index: Optional[int] = None) -> None:
    global db

    chapter_list = get_chapter_list(series_name)

    for existing_name in chapter_list:
        if chapter_name.lower() == existing_name.lower():
            raise UniqueNameConstraintError("A chapter with that name already exists.")

    if index is not None:
        chapter_list.insert(index, chapter_name)
    else:
        chapter_list.append(chapter_name)
    
    db[series_name][chapter_name] = []


def write_database_to_file(filename: str) -> None:
    global db

    with open(filename, 'w') as f:
        json.dump(db, f, indent=4)


if __name__ == "__main__":
    main()
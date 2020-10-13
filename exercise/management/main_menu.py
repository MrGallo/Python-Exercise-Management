from typing import List, Dict, Callable, Optional, Tuple
from itertools import count
import re
import json


class UniqueNameConstraintError(Exception):
    pass


class ExerciseNotFoundError(Exception):
    pass


Exercise = Dict[str, str]

FORM_FILE = "exercise/management/form.md"
EXERCISE_FILE = "exercise/management/exercises.json"

def menu_clear_form():
    def inner() -> None:
        print("Are you sure?")
        choice = input("[y/n] > ").lower()
        if choice == "y":
            write_to_form({}, FORM_FILE)

    return inner


def menu_show_exercises(exercises: List[Exercise]) -> Callable:
    def inner() -> None:
        print_exercise_list(exercises)
    return inner


def print_exercise_list(exercises: List[Exercise]):
    for i, ex in enumerate(exercises, 1):
            print(f"{i}. {ex['name']}")


def menu_move_exercise(exercises: List[Exercise]) -> Callable:
    def inner():
        print_exercise_list(exercises)
        index = get_valid_choice(exercises, "Choose an exercise to move.")
        exercise_choice = exercises.pop(index)
        print(f"You chose '{exercise_choice['name']}'.")

        print_exercise_list(exercises)
        print(f"Where would you like to insert '{exercise_choice['name']}'?")
        print(f"[0-{len(exercises)}]")
        index = get_valid_choice(exercises + [exercise_choice], "Choose a position to move to.")
        insert_exercise(exercise_choice, exercises, index=index)
        write_exercises_to_file(exercises, 'exercises.json')

    return inner


def menu_update_exercise(exercises: List[Exercise]) -> Callable:
    def inner():
        print_exercise_list(exercises)
        index = get_valid_choice(exercises, "Choose an exercise.") - 1
        exercise_choice = exercises[index]
        print(f"You chose '{exercise_choice['name']}'.")
    
        # write to form.md file
        write_to_form(exercise_choice, FORM_FILE)

        # edit the form
        print("Edit the form.md file and choose an option:")
        print("[u]pdate the exercise from the file.")
        print("Enter anything else to cancel.")

        choice = input("> ").lower()
        if choice == "u":
            new_exercise = create_exercise(*parse_form(FORM_FILE))
            update_exercise(new_exercise, exercises, index=index)
            write_exercises_to_file(exercises, EXERCISE_FILE)
            print(f"Updated #{index}: {new_exercise['name']}.")

    return inner


def get_valid_choice(exercises: List[Exercise], prompt: str) -> int:
    while True:
        print(prompt)
        
        try:
            i = int(input("> ")) - 1
            exercises[i]
            assert i >= 0
        except IndexError:
            print("Invalid exercise number.")
        except ValueError:
            print("Not a number")
        except AssertionError:
            print("Cannot be a negative index.")
        else:
            break
    return i + 1


def write_to_form(exercise: Exercise, filename: str) -> None:
    name = exercise.get("name", "").strip()
    topic = exercise.get("topic", "").strip()
    requirements = '\n'.join(exercise.get("requirements", "")).strip()
    description = exercise.get("description", "").strip()
    starter_code = exercise.get("starter_code", "").strip()
    tests = exercise.get("tests", "").strip()

    contents = f"""# name
{name}

# topic
{topic}

# requirements
{requirements}

# description
{description}

# starter code
```python
{starter_code}
```

# tests
```python
{tests}
```
"""
    with open(filename, 'w') as f:
        f.write(contents)


def parse_form(filename: str) -> Tuple[str, str, str, str, str, str]:
    print("Parsing exercise from 'form.md'")
    with open(filename, 'r') as f:
        contents = f.read()
            
    regex = r"# name\n+(.+)"
    name = re.search(regex, contents).group(1).strip()

    regex = r"# topic\n+(.+)"
    topic = re.search(regex, contents).group(1).strip()

    regex = r"# requirements\n+(.+?)\n# description"
    requirements = re.search(regex, contents, re.DOTALL).group(1).strip().strip()

    regex = r"# description\n+(.+?)\n# starter code"
    description = re.search(regex, contents, re.DOTALL).group(1).strip()

    regex = r"# starter code\n+```python\n(.+?)```"
    starter_code = re.search(regex, contents, re.DOTALL).group(1).strip()

    regex = r"# tests\n+```python\n(.+?)```"
    tests = re.search(regex, contents, re.DOTALL).group(1).strip()

    return name, topic, requirements, description, starter_code, tests


def menu_add_exercise(exercises: List[Exercise]) -> None:
    def inner():
        while True:
            exercise = create_exercise(*parse_form(FORM_FILE))
            name = exercise["name"]
            print(f"Name: {name}")
            
            while True:
                insert = input(f"Insert? 0-{len(exercises)-1} [append]")
                try:
                    insert = int(insert)
                except ValueError:
                    insert = None
                    break
                else:
                    if insert >= 0 and insert < len(exercises):
                        break            

            location = "the end" if insert is None else insert
            print()
            print(f"[ENTER] Confirm add '{name}' to {location}")
            print("[r]etry (Go edit the 'form.md' file).")

            choice = input("> ")

            if choice == "":
                break
        
        try:
            insert_exercise(exercise, exercises, insert)
        except UniqueNameConstraintError:
            print("ATTENTION")
            print("---------")
            print(f"An exercise with the name {name} already exists.")
            print("Do you want to overwrite it (update) with the contents of form.md?")
            print()
            choice = input("[y/n] > ").lower()
            if choice == "y":
                update_exercise(exercise, exercises)
                write_exercises_to_file(exercises, EXERCISE_FILE)
        else:
            write_exercises_to_file(exercises, EXERCISE_FILE)
            print(f"Added {name}")
    
    return inner


def create_exercise(name: str,
                    topic: str,
                    requirements: str,
                    description: str,
                    starter_code: str,
                    tests: str) -> Exercise:
    if len(requirements) == 0:
        requirements = []
    else:
        requirements = requirements.split("\n")

    return {
        "name": name,
        "topic": topic,
        "requirements": requirements,
        "description": description,
        "starter_code": starter_code,
        "tests": tests
    }


def update_exercise(exercise: Exercise,
                    collection: List[Exercise],
                    index: Optional[int] = None):
    if index is None:
        index = find_exercise(exercise["name"], collection)
    collection[index] = exercise


def insert_exercise(exercise: Exercise,
                 collection: List[Exercise],
                 index: Optional[int] = None) -> None:
    try:
        find_exercise(exercise["name"], collection)
    except ExerciseNotFoundError:
        pass
    else:
        raise UniqueNameConstraintError("An exercise with that name already exists.")

    if index is not None:
        collection.insert(index, exercise)
    else:
        collection.append(exercise)


def find_exercise(name: str, collection: List[Exercise]) -> int:
    """Gets index of exercise with given name in a list of exercises.

    Args:
        name: Name of the exercise to find.
        collection: The list of exercises to search through.
    Returns:
        The index.
    
    Raises:
        ExerciseNotFoundError if exercise not found.
    """
    for i, ex in enumerate(collection):
        if ex["name"] == name:
            return i
    raise ExerciseNotFoundError


def write_exercises_to_file(exercises: List[Exercise], filename: str) -> None:
    with open(filename, 'w') as f:
        json.dump({"exercises": exercises}, f, indent=4)


def get_menu_options(exercises: List[Exercise]) -> Dict[int, Exercise]:
    options = dict(zip(count(1), [
        ("Show all exercises", menu_show_exercises(exercises)),
        ("Add Exercise", menu_add_exercise(exercises)),
        ("Update Exercise", menu_update_exercise(exercises)),
        ("Move Exercise", menu_move_exercise(exercises)),
        ("Clear form.md", menu_clear_form()),
        ("Quit", exit),
    ]))

    return options
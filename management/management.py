from typing import List, Dict, Callable, Tuple, Union, Optional
import json
import re
from itertools import count

from management.types import *
from management.utils import *
import management.settings as settings


class Database(dict):
    def __init__(self, database_file: str):
        self.filename = database_file
        super().__init__(self.load())
    
    def load(self):
        with open(self.filename, 'r') as f:
            return json.load(f)
        
    def write_to_file(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump(self, f, indent=4)


class ItemMenu:
    QUIT = "quit"
    BACK = "back"
    STAY = "stay"

    child_class: type = None
    item_list_name: str = None
    child_item_name: str = "item"
    
    def __init__(self, db: Database, parent: Optional[Dict[Any, Any]] = None, data: Dict[Any, Any] = None):
        self.db = db

        self._has_parent = False
        if parent is None:
            self.parent = db
        else:
            self.parent = parent
            self._has_parent = True
        
        if data is None:
            self.data = db
        else:
            self.data = data
        
        self.children = {}
        if self.child_class is not None:
            self.spawn_children()
    
    def spawn_children(self):
        self.children = {}
        for child_name in self.get_child_list():
            self.children[child_name] = self.child_class(self.db, self.data, self.data[child_name])

    def get_list(self) -> List[str]:
        try:
            return self.data[self.item_list_name]
        except KeyError:
            self.data[self.item_list_name] = []
            self.db.write_to_file()
            return self.data[self.item_list_name]
    
    def get_child_list(self):
        return self.data[self.item_list_name]
    
    def add_child_item(self):
        item_list = self.get_list()

        item_name, insert = self.confirm_item_name_and_location(self.child_item_name, item_list)

        self.insert_item(item_name, insert)
        self.db.write_to_file()
        return ItemMenu.STAY
    
    def confirm_item_name_and_location(self, item_name: str, existing_items: List[str]):
        while True:
            name = input(f"Enter the name of the new {item_name}: ")
            
            insert = self.get_insert_location(existing_items)

            location = "the end" if insert is None else (insert+1)
            print()
            print(f"[ENTER] Confirm add '{name}' to {location}")
            print("[r]edo")

            choice = input("> ")

            if choice == "":
                break

        return name, insert
    
    def get_insert_location(self, existing_items: List[Any]):
        insert = None
        if len(existing_items) > 0:
            while True:
                insert = input(f"Insert? 1-{len(existing_items)} [end]")
                try:
                    insert = int(insert)-1
                except ValueError:
                    insert = None
                    break
                else:
                    if insert >= 0 and insert < len(existing_items):
                        break
            return insert
    
    def insert_item(self,
                    item_name: str,
                    index: Optional[int] = None) -> None:
        item_list = self.get_list()

        for existing_name in item_list:
            if item_name.lower() == existing_name.lower():
                raise UniqueNameConstraintError(f"An item with the name of '{item_name}' already exists.")

        if index is not None:
            item_list.insert(index, item_name)
        else:
            item_list.append(item_name)
        
        self.data[item_name] = self.new_child_item()

    def new_child_item(self):
        return {self.child_class.item_list_name: []}
    
    def remove_child_item(self):
        item_list = self.get_list()

        choice = self.get_child_operation_choice("remove", item_list)
        if choice == -1:
            return ItemMenu.STAY
            
        print(f"You chose {item_list[choice]}")
        print()
        print(f"ATTENTION: This will remove EVERYTHING contained in {item_list[choice]}")
        print(f"To proceed, type the name of the item: '{item_list[choice]}'")
        print("Enter anything else to cancel.")

        confirm = input("Confirm deletion: ").lower()

        if confirm != item_list[choice].lower():
            print("\nDeletion CANCELED.\n")
            return ItemMenu.STAY
       
        # remove from directory list and the series
        item_name = item_list[choice]
        self.remove_child_from_data(item_list, choice)
        self.db.write_to_file()
        print(f"\nDELETED {item_name}.\n")

    
    def remove_child_from_data(self, item_list: List[Any], choice: int):
        item_name = item_list.pop(choice)
        del self.data[item_name]

    def move_child_item(self):
        item_list = self.get_list()
        choice = self.get_child_operation_choice("move", item_list)
        if choice == -1:
            return ItemMenu.STAY
        
        item_name = item_list[choice]
        old_index = item_list.index(item_name)
        item = item_list.pop(old_index)

        print(f"You chose {item_name}")
        print()


        while True:
            self.print_numbered_menu_options()
            insert = self.get_insert_location(self.get_list())

            location = "the end" if insert is None else (insert+1)
            print()
            print(f"[ENTER] Confirm move '{item_name}' to {location}")
            print("[r]edo")
            print("[c]ancel")

            choice = input("> ").lower()

            if choice == "":
                break
            elif choice == "c":
                item_list.insert(old_index, item)
                return ItemMenu.STAY

        if insert is None:
            item_list.append(item)
        else:
            item_list.insert(insert, item)
        self.db.write_to_file()

    def edit_child_item(self):
        item_list = self.get_list()
        index = self.get_child_operation_choice("update", item_list)
        item_name = item_list[index]
        print(f"Editing {item_name}")
        
        new_name = input("Change name to: ")
        self.insert_item(new_name, index)

        # swap contents
        self.data[new_name] = self.data[item_name]
        del self.data[item_name]
        del item_list[index+1]

        self.db.write_to_file()
        self.spawn_children()

        return ItemMenu.STAY

    
    def get_child_operation_choice(self, action: str, item_list: Dict[Any, Any]) -> int:
        while True:
            print()
            print(f"Select {self.child_item_name} # to {action}.")
            print("[l]ist options")
            print("[b]ack")
            choice = input("> ").lower()
            if choice == "l":
                self.print_numbered_menu_options()
                continue
            elif choice == "b":
                return -1

            try:
                choice = int(choice) - 1
                assert choice >= 0 and choice < len(item_list)
            except (ValueError, AssertionError):
                print("Invalid option")
            else:
                return choice
    
    def show_child(self, child_name: str):
        child = self.children[child_name]
        return child.menu()

    def menu(self):
        while True:
            item_list = self.get_list()
            self.print_numbered_menu_options()
            
            print()
            print(*self.get_lettered_menu_options_text(), sep="\n")
            
            print()
            while True:
                choice = input("> ").lower()

                try:
                    _, func = self.get_lettered_menu_options()[choice]
                except KeyError:
                    try:
                        choice = int(choice) - 1
                        assert choice >= 0 and choice < len(item_list)
                    except (ValueError, AssertionError):
                        print("Invalid option")
                    else:
                        result = self.show_child(item_list[choice])
                        if result == ItemMenu.QUIT:
                            return ItemMenu.QUIT
                        break
                else:
                    result = func()
                    if result == ItemMenu.QUIT:
                        return ItemMenu.QUIT
                    elif result == ItemMenu.BACK:
                        return ItemMenu.BACK
                    break
        
            print()
    
    def print_numbered_menu_options(self):
        for i, label in enumerate(self.get_list(), 1):
                print(f"[{i}] {label}")
    
    def get_lettered_menu_options(self) -> Dict[str, Tuple[str, Callable]]:
        options = {}
        options["a"] = (f"[a]dd {self.child_item_name}", self.add_child_item)
        options["r"] = (f"[r]emove {self.child_item_name}", self.remove_child_item)
        options["m"] = (f"[m]ove {self.child_item_name}", self.move_child_item)
        options["e"] = (f"[e]dit {self.child_item_name}", self.edit_child_item)
        if self._has_parent is True:
            options["b"] = ("[b]ack", lambda: ItemMenu.BACK)
        options["q"] = ("[q]uit", lambda: ItemMenu.QUIT)
        
        return options

    def get_lettered_menu_options_text(self) -> List[str]:
        options = self.get_lettered_menu_options()
        menu_text = []
        for key, (label, callback) in options.items():
            menu_text.append(label)
        return menu_text


class ExerciseMenu(ItemMenu):
    def get_list(self):
        return []


class ChapterMenu(ItemMenu):
    child_item_name: str = "exercise"
    child_class: type = ExerciseMenu
    item_list_name: str = None

    def show_child(self, child_name: str):
        return ItemMenu.STAY

    def spawn_children(self):
        for i, exercise in enumerate(self.get_child_list()):
            self.children[exercise["name"]] = self.child_class(self.db, self.data, self.data[i])

    def get_list(self):
        return [ex["name"] for ex in self.data]

    def get_child_list(self) -> List[Exercise]:
        return self.data
    
    def remove_child_from_data(self, item_list: List[Any], choice: int):
        del self.data[choice]
    
    def edit_child_item(self):
        item_list = self.get_list()
        index = self.get_child_operation_choice("update", item_list)
        item_name = item_list[index]
        print(f"Editing {item_name}")

        self.write_exercise_to_form(self.data[index])

        print(f"Go ahead and edit '{settings.FORM_FILE}'.")
        print("Press [ENTER] to update.")
        input()

        exercise = ChapterMenu.create_exercise(*ChapterMenu.parse_exercise_form())

        self.data[index] = exercise
        self.db.write_to_file()
        self.spawn_children()

        return ItemMenu.STAY
    
    def add_child_item(self):
        print("ADD EXERCISE")

        print("Clear the form.md file?")
        choice = input("'yes' > ").lower()
        if choice != "yes":
            return ItemMenu.STAY

        # clear the form
        print("Clearing form.md")
        self.write_exercise_to_form({})

        print("Go and fill form.md.")
        input("Press [ENTER] when done.")


        item_list = self.get_list()

        while True:
            exercise = ChapterMenu.create_exercise(*ChapterMenu.parse_exercise_form())
            existing_items = self.data
            name = exercise["name"]
            print(f"Name: {name}")

            insert = None
            if len(existing_items) > 0:
                while True:
                    insert = input(f"Insert? 0-{len(existing_items)-1} [append]")
                    try:
                        insert = int(insert)
                    except ValueError:
                        insert = None
                    else:
                        if not (insert >= 0 and insert < len(existing_items)):
                            continue
                    break

            location = "the end" if insert is None else insert
            print()
            print(f"[ENTER] Confirm add '{name}' to {location}")
            print("[r]edo")

            choice = input("> ")

            if choice == "":
                break        
        try:
            self.insert_item(exercise, insert)
        except UniqueNameConstraintError:
            print("ATTENTION")
            print("---------")
            print(f"An exercise with the name {name} already exists.")
            print("Do you want to overwrite it (update) with the contents of form.md?")
            print()
            choice = input("[y/n] > ").lower()
            if choice == "y":
                self.update_exercise(exercise)
                self.db.write_to_file()
        else:
            self.db.write_to_file()
            print(f"Added {name}")

        return ItemMenu.STAY
    
    def update_exercise(self,
                        exercise: Exercise,
                        index: Optional[int] = None):
        if index is None:
            index = self.find_exercise(exercise["name"])
        self.data[index] = exercise
    
    def find_exercise(self, exercise_name: str) -> int:
        """Gets index of exercise with given name in a list of exercises.

        Args:
            exercise_name: Name of the exercise to find.
        Returns:
            The index.
        
        Raises:
            ExerciseNotFoundError if exercise not found.
        """
        for i, ex in enumerate(self.data):
            if ex["name"] == exercise_name:
                return i
        raise ExerciseNotFoundError
    
    def insert_item(self,
                    new_exercise: Exercise,
                    index: Optional[int] = None) -> None:
        item_list = self.data

        for exercise in item_list:
            if new_exercise["name"].lower() == exercise["name"].lower():
                raise UniqueNameConstraintError(f"An exercise with the name of '{new_exercise['name']}' already exists.")

        if index is not None:
            item_list.insert(index, new_exercise)
        else:
            item_list.append(new_exercise)

    def write_exercise_to_form(self, exercise: List[Exercise]) -> None:
        name = exercise.get("name", "")
        topic = exercise.get("topic", "")
        requirements = '\n'.join(exercise.get("requirements", ""))
        description = exercise.get("description", "")
        starter_code = exercise.get("starter_code", "")
        tests = exercise.get("tests", "")
        solution = exercise.get("solution", "")

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

# solution
```python
{solution}
```
"""
        with open(settings.FORM_FILE, 'w') as f:
            f.write(contents)
    
    @staticmethod
    def parse_exercise_form() -> Tuple[str, str, str, str, str, str, str]:
        print(f"Parsing exercise from '{settings.FORM_FILE}'")
        with open(settings.FORM_FILE, 'r') as f:
            contents = f.read()
                
        regex = r"# name\n+(.+)"
        name = re.search(regex, contents).group(1)

        regex = r"# topic\n+(.+?)\n# requirements"
        topic = re.search(regex, contents, re.DOTALL).group(1).strip()

        regex = r"# requirements\n+(.+?)\n# description"
        requirements = re.search(regex, contents, re.DOTALL).group(1).strip()

        regex = r"# description\n+(.+?)\n# starter code"
        description = re.search(regex, contents, re.DOTALL).group(1).strip()

        regex = r"# starter code\n+```python\n(.+?)```"
        starter_code = re.search(regex, contents, re.DOTALL).group(1).strip()

        regex = r"# tests\n+```python\n(.+?)```"
        tests = re.search(regex, contents, re.DOTALL).group(1).strip()

        regex = r"# solution\n+```python\n(.+?)```"
        solution = re.search(regex, contents, re.DOTALL).group(1).strip()

        return name, topic, requirements, description, starter_code, tests, solution

    @staticmethod
    def create_exercise(name: str,
                        topic: str,
                        requirements: str,
                        description: str,
                        starter_code: str,
                        tests: str,
                        solution: str) -> Exercise:
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
            "tests": tests,
            "solution": solution
        }


class SeriesMenu(ItemMenu):
    child_class: type = ChapterMenu
    child_item_name: str = "chapter"
    item_list_name: str = "chapter_list"

    def new_child_item(self):
        return []


class MainMenu(ItemMenu):
    child_class: type = SeriesMenu
    child_item_name: str = "series"
    item_list_name: str = "series_list"


def main():
    db = Database(settings.DATABASE_FILE)
    m = MainMenu(db)

    m.menu()

    


# def get_series_list(db: Database) -> List[str]:
#     try:
#         return db["series_list"]
#     except KeyError:
#         db["series_list"] = []
#         write_database_to_file(db, settings.DATABASE_FILE)
#         return db["series_list"]


# def get_chapter_list(series: Series) -> List[str]:
#     try:
#         return series["chapter_list"]
#     except KeyError:
#         series["chapter_list"] = []
#         write_database_to_file(db, settings.DATABASE_FILE)
#         return series["chapter_list"]


# def get_chapter_list(db: Database, series_name: str) -> List[str]:
#     series = db[series_name]
#     try:
#         return series["chapter_list"]
#     except KeyError:
#         series["chapter_list"] = []
#         write_database_to_file(db, settings.DATABASE_FILE)
#         return series["chapter_list"]


# def show_series(db: Database, series_name: str):
#     while True:
#         series = db[series_name]
#         chapter_list = get_chapter_list(series)

#         print()
#         print(series_name)
#         for i, chapter in enumerate(chapter_list, 1):
#             print(f"[{i}] {chapter}")
        
#         print()
#         print(f"[e]dit series name ({series_name})")
#         print("[a]dd chapter")
#         print("[b]ack")
#         print("[q]uit")
        
#         print()
#         choice = None
#         while True:
#             choice = input("> ").lower()
#             if choice == "a":
#                 add_chapter(db, series_name)
#             elif choice == "e":
#                 series_name = edit_series_name(db, series_name)
#             elif choice == "q":
#                 return -1
#             elif choice == "b":
#                 return 0
#             else:
#                 try:
#                     choice = int(choice) - 1
#                     assert choice >= 0 and choice < len(chapter_list)
#                 except (ValueError, AssertionError):
#                     print("Invalid option")
#                     continue
#                 else:
#                     result = show_chapter(db, series_name, chapter_list[choice])
#                     if result == -1:
#                         return -1
#                     break
#             break

#         print()


# def show_chapter(db: Database, series_name: str, chapter_name: str):
#     while True:
#         series = db[series_name]
#         exercise_list = series[chapter_name]

#         print()
#         print(series_name)
#         print(chapter_name)
#         for i, exercise in enumerate(exercise_list, 1):
#             print(f"[{i}] {exercise['name']}")
        
#         print()
#         print(f"[e]dit chapter name ({chapter_name})")
#         print("[a]dd exercise")
#         print("[b]ack")
#         print("[q]uit")
        
#         print()
#         choice = None
#         while True:
#             choice = input("> ").lower()
#             if choice == "a":
#                 add_exercise(exercise_list)
#             elif choice == "e":
#                 chapter_name = edit_chapter_name(db, series, chapter_name)
#             elif choice == "q":
#                 return -1
#             elif choice == "b":
#                 return 0
#             else:
#                 try:
#                     choice = int(choice) - 1
#                     assert choice >= 0 and choice < len(chapter_list)
#                 except (ValueError, AssertionError):
#                     print("Invalid option")
#                     continue
#                 else:
#                     result = show_exercise(exercise_list[choice])
#                     if result == -1:
#                         return -1
#                     break
#             break

#         print()


# def add_series(db: Database):
#     series_list = get_series_list(db)

#     series_name, insert = confirm_item_name_and_location("series", series_list)

#     insert_series(db, series_name, insert)
#     write_database_to_file(db, settings.DATABASE_FILE)
#     return 0

    
# def add_chapter(db: Database, series_name: str):
#     chapter_list = get_chapter_list(db[series_name])

#     chapter_name, insert = confirm_item_name_and_location("chapter", chapter_list)

#     insert_chapter(db, series_name, chapter_name, insert)
#     write_database_to_file(db, settings.DATABASE_FILE)
#     return 0


# def confirm_item_name_and_location(item_name: str, existing_items: List[str]):
#     while True:
#         name = input(f"Enter the name of the new {item_name}: ")
        
#         insert = None
#         while True:
#             if len(existing_items) > 0:
#                 insert = input(f"Insert? 0-{len(existing_items)-1} [append]")
#                 try:
#                     insert = int(insert)
#                 except ValueError:
#                     insert = None
#                     break
#                 else:
#                     if insert >= 0 and insert < len(existing_items):
#                         break       

#         location = "the end" if insert is None else insert
#         print()
#         print(f"[ENTER] Confirm add '{name}' to {location}")
#         print("[r]edo")

#         choice = input("> ")

#         if choice == "":
#             break

#     return name, insert


# def edit_series_name(db: Database, series_name: str):
#     return edit_item(db, db, series_name, "series_list", insert_series)


# def edit_chapter_name(db: Database, series: Series, chapter_name: str):
#     return edit_item(db, series, chapter_name, "chapter_list", insert_chapter)


# def edit_item(db: Database, parent: Dict[Any, Any], item_name: str,
#               item_list_name: str, insert_func: Callable):
#     item_list = parent[item_list_name]
#     index = item_list.index(item_name)

#     print(f"Editing {item_name}.")
#     new_name = input("Change name to: ")
#     insert_func(db, parent, new_name, index)

#     # swap contents
#     parent[new_name] = parent[item_name]
#     del parent[item_name]
#     del parent[item_list_name][index+1]

#     write_database_to_file(db, settings.DATABASE_FILE)

#     return new_name


# def insert_series(db: Database,
#                   series_name: str,
#                   index: Optional[int] = None) -> None:
#     series_list = get_series_list(db)

#     for existing_name in series_list:
#         if series_name.lower() == existing_name.lower():
#             raise UniqueNameConstraintError("A series with that name already exists.")

#     if index is not None:
#         series_list.insert(index, series_name)
#     else:
#         series_list.append(series_name)
    
#     db[series_name] = {"chapter_list": []}


# def insert_chapter(db: Database,
#                    series: Series,
#                    chapter_name: str,
#                    index: Optional[int] = None) -> None:
#     chapter_list = get_chapter_list(series)

#     for existing_name in chapter_list:
#         if chapter_name.lower() == existing_name.lower():
#             raise UniqueNameConstraintError("A chapter with that name already exists.")

#     if index is not None:
#         chapter_list.insert(index, chapter_name)
#     else:
#         chapter_list.append(chapter_name)
    
#     series[chapter_name] = []


# def write_database_to_file(db: Database, filename: str) -> None:
#     with open(filename, 'w') as f:
#         json.dump(db, f, indent=4)


if __name__ == "__main__":
    main()
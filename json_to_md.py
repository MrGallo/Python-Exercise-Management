from typing import List, Optional
import json
import os
import shutil

from slugify import slugify

import management.settings as settings
from management.types import Series, Database, Exercise


def main():
    with open(settings.DATABASE_FILE) as f:
        data = json.load(f)
    
    clear_folder(settings.EXERCISE_DOCS_FOLDER)
    series_list = data["series_list"]
    for series_name in series_list:
        write_series(data, series_name, settings.EXERCISE_DOCS_FOLDER)
    
    append = ("You can do these exercises and test them using "
              "my `Python Exercise Runner <https://repl.it/"
              "@DanielGallo/Python-Exercise-Runner>`_.")
    
    write_index_rst(item_list=series_list,
                    title="Python Exercises",
                    write_path=".",
                    max_depth=2,
                    ref_path=settings.EXERCISE_DOCS_FOLDER,
                    append_text=append)


def clear_folder(folder: str):
    try:
        shutil.rmtree(folder)
    except FileNotFoundError:
        pass  # folder doesn't exist

    os.mkdir(folder)

def write_index_rst(item_list: List[str],
                    title: str,
                    write_path: str,
                    max_depth: int = 2,
                    ref_path: str = "",
                    is_parent: bool = True,
                    append_text: Optional[str] = None):

    content = f"""{title}
{"=" * len(title)}

.. toctree::
    :maxdepth: {max_depth}

"""

    for item in item_list:
        item_path = slugify(item)
        if is_parent:
            item_path = os.path.join(ref_path, slugify(item), "index")

        content += f"    {item_path}\n"
    
    if append_text is not None:
        content += "\n" + append_text
    
    with open(os.path.join(write_path, "index.rst"), "w") as f:
        f.write(content)


def write_series(db: Database, series_name: str, path: str) -> None:
    series = db[series_name]
    series_slug = slugify(series_name)
    # create folder for series
    series_path = os.path.join(path, series_slug)
    os.mkdir(series_path)

    # write chapters
    chapter_list = series["chapter_list"]
    for chapter_name in chapter_list:
        write_chapter(series, chapter_name, series_path)
    
    write_index_rst(chapter_list,
                    series_name.title(),
                    series_path)


def write_chapter(series: Series, chapter_name: str, path: str) -> None:
    exercises = series[chapter_name]
    chapter_slug = slugify(chapter_name)

    # create folder for chapter
    chapter_path = os.path.join(path, chapter_slug)
    os.mkdir(chapter_path)

    # write exercises
    for exercise in exercises:
        write_exercise(exercise, chapter_path)
    
    exercise_names = [ex["name"] for ex in exercises]
    write_index_rst(exercise_names,
                    chapter_name.title(),
                    chapter_path,
                    max_depth=1,
                    is_parent=False)


def write_exercise(exercise: Exercise, path: str) -> None:
    name = exercise.get("name", "").strip() 
    topic = exercise.get("topic", "").strip()
    requirements = ""
    for req in exercise.get("requirements", ""):
        requirements += f"- {req}\n"
    description = exercise.get("description", "").strip()
    starter_code = exercise.get("starter_code", "").strip()
    tests = exercise.get("tests", "").strip()
    filename = f"{slugify(name)}.md"
    exercise_path = os.path.join(path, filename)

    if "tests_io" in exercise.keys():
        io_tests = exercise['tests_io']
        tests_content = ""
        for i, (arg_list, result) in enumerate(io_tests, 1):
            inputs = '\n'.join(map(repr, arg_list))
            tests_content += f"### Test {i}\n"
            tests_content += f"**Input:**\n```\n{inputs}\n```\n"
            tests_content += f"**Output:**\n```\n{repr(result)}\n```\n"
    else:
        tests_content = f"## Tests\n```python\n{tests}\n```"

    content = f"""# {name}
{"**Topic:** " if topic else ""}{topic if topic else ""}
{"**Requirements:** " if requirements else ""}
{requirements if requirements else ""}

{description}

{"## Starter Code" if starter_code else ""}
{"```python" if starter_code else ""}
{starter_code if starter_code else ""}
{"```" if starter_code else ""}

{tests_content}
"""

    with open(exercise_path, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    main()
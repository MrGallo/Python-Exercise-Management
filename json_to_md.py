from management.utils import calc_difficulty
from typing import List, Optional
import json
from pathlib import PurePosixPath
import os
import shutil

from slugify import slugify

import management.settings as settings
from management.types import Series, Database, Exercise
from management.concepts import concepts as CONCEPTS


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
                    append_text: Optional[str] = None,
                    difficulties: Optional[List[str]] = None):

    content = f"""{title}
{"=" * len(title)}

.. toctree::
    :maxdepth: {max_depth}

"""

    for i, item in enumerate(item_list):
        item_path = slugify(item)
        if is_parent:
            item_path = PurePosixPath(ref_path, slugify(item), "index")

        if difficulties and difficulties[i] > 1:
            content += f"    {item_path} ({difficulties[i]}) <{item_path}>\n"
        else:
            content += f"    {item_path}\n"
    
    if append_text is not None:
        content += "\n" + append_text
    
    with open(PurePosixPath(write_path, "index.rst"), "w") as f:
        f.write(content)


def write_series(db: Database, series_name: str, path: str) -> None:
    series = db[series_name]
    series_slug = slugify(series_name)
    # create folder for series
    series_path = PurePosixPath(path, series_slug)
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
    chapter_path = PurePosixPath(path, chapter_slug)
    os.mkdir(chapter_path)

    # write exercises
    for exercise in exercises:
        write_exercise(exercise, chapter_path)
    
    exercise_names = [ex["name"] for ex in exercises]
    difficulties = [calc_difficulty(ex["requirements"], CONCEPTS) for ex in exercises]
    write_index_rst(exercise_names,
                    chapter_name.title(),
                    chapter_path,
                    max_depth=1,
                    is_parent=False,
                    difficulties=difficulties)


def write_exercise(exercise: Exercise, path: str) -> None:
    name = exercise.get("name", "").strip() 
    topic = exercise.get("topic", "").strip()
    requirements = exercise.get("requirements", "")
    description = exercise.get("description", "").strip()
    starter_code = exercise.get("starter_code", "").strip()
    tests = exercise.get("tests", "").strip()
    filename = f"{slugify(name)}.md"
    exercise_path = PurePosixPath(path, filename)

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
    

    requirements_content = ""
    if requirements:
        requirements_content += "**Requirements:**\n```eval_rst\n"
        for req in requirements:
            requirements_content += f"- :ref:`fundamentals:{req}`\n"
        requirements_content += "\n```\n"
    
    topic_content = ""
    if topic:
        topic_content = "**Topic:** \n"
        topic_content += f"```eval_rst\n:ref:`fundamentals:{topic}`\n\n```"

    content = f"""# {name}

{topic_content}

{requirements_content}

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
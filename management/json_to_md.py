from typing import List
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
    
    write_index_rst(item_list=series_list,
                    title="Exercise Series",
                    write_path=".",
                    max_depth=3,
                    ref_path=settings.EXERCISE_DOCS_FOLDER)



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
                    is_parent: bool = True):

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
                    f"{chapter_name.title()} Exercises",
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

    content = f"""# {name}
**Topic:** {topic}
{"**Requirements:**" if requirements else ""}
{requirements if requirements else ""}

{description}

## Starter Code
```python
{starter_code}
```

## Tests
```python
{tests}
```
"""

    with open(exercise_path, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    main()
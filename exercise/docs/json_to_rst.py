from typing import List
import json

from slugify import slugify


def main():
    with open("exercise/management/exercises.json") as f:
        data = json.load(f)
    
    write_exercises_to_md_files(data["exercises"])
    write_index_rst(data["exercises"])


def write_exercises_to_md_files(exercises: List["Exercise"]):
    for exercise in exercises:
        write_json_to_file(exercise)


def write_json_to_file(exercise: "Exercise") -> None:
    name = exercise.get("name", "").strip() 
    topic = exercise.get("topic", "").strip()
    requirements = '\n'.join(exercise.get("requirements", "")).strip()
    description = exercise.get("description", "").strip()
    starter_code = exercise.get("starter_code", "").strip()
    tests = exercise.get("tests", "").strip()
    filename = f"{slugify(name)}.md"

    content = f"""# {name}

{description}
"""

    with open(f"exercise/docs/exercises/{filename}", 'w') as f:
        f.write(content)


def write_index_rst(exercises: List["Exercise"]):
    content = """Python Exercises!
=================

.. toctree::
    :maxdepth: 2
    :caption: Contents:

"""
    for exercise in exercises:
        name = slugify(exercise.get("name", "").strip())
        content += f"    exercises/{name}\n"
    
    with open("exercise/docs/index.rst", "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
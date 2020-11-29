import json
from os import strerror

import management.settings as settings


def main():
    with open(settings.DATABASE_FILE, 'r') as f:
        data = json.load(f)
    
    series_list = data["series_list"]
    content = ":orphan:\n\nSolutions\n=========\n\n.. contents::\n    :local:\n\n"
    for series_name in series_list:
        content += get_series_content(data, series_name)
    
    with open("solutions.rst", "w") as f:
        f.write(content)


def get_series_content(data, series_name):
    content = f"{series_name}\n{'-' * len(series_name)}\n\n"

    chapter_list = data[series_name]["chapter_list"]
    for chapter_name in chapter_list:
        content += get_chapter_content(data, series_name, chapter_name)

    return content + "\n"


def get_chapter_content(data, series_name, chapter_name):
    content = f"{chapter_name}\n{'^' * len(chapter_name)}\n"

    exercise_list = data[series_name][chapter_name]
    for exercise in exercise_list:
        if exercise["solution"] != "":
            indented_solution = "\n".join([f"    {line}" for line in exercise["solution"].split("\n")])
            content += f"{exercise['name']}\n{'*' * len(exercise['name'])}\n"
            content += f".. code-block:: python\n    :linenos:\n\n{indented_solution}\n\n"

    return content + "\n"

if __name__ == "__main__":
    main()

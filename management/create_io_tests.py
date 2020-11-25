import json


with open('management/database.json', 'r') as f:
    data = json.load(f)

series_name = "Codingbat (Input/Output)"
chapter_names = ["String-1", "String-2"]
for chapter_name in chapter_names:
    chapter = data[series_name][chapter_name]

    for exercise in chapter:
        print(exercise['name'])
        test_code = "from exercise.fixtures import captured_output\n\n\n"
        tests_io = exercise['tests_io']
        for n, (arg_list, result) in enumerate(tests_io, 1):
            input_str = "\\n".join(map(str, arg_list))
            test_code += f"def test_{n}():\n"
            test_code += f"    assert captured_output('{input_str}') == {repr(result)}\n\n\n"

        exercise['tests'] = test_code.strip()
    

with open('management/database.json', 'w') as f:
    data = json.dump(data, f, indent=4)
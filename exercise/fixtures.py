import io
import re
from typing import List, Optional, Union

import pytest


def get_solution_source(filename: str = "main.py") -> str:
    with open(filename, 'r') as f:
        return f.read()


def solution_contains(target: str):
    return target in get_solution_source()


def solution_contains_regex(target: str):
    return re.compile(target).search(get_solution_source()) is not None

@pytest.fixture
def captured_output(capsys, monkeypatch):
    def io_test(user_input: Optional[Union[str, List[Union[str, int, float]]]] = None):
        if type(user_input) is list:
            input_string = "\n".join(map(str, user_input))
        else:
            input_string = user_input
        monkeypatch.setattr('sys.stdin', io.StringIO(input_string))
        solution_source = get_solution_source("main.py")
        exec(solution_source)
        captured = capsys.readouterr()
        return captured.out.strip()
    return io_test

from typing import List, Union, Optional

import io
import pytest


@pytest.fixture
def captured_output(capsys, monkeypatch):
    def io_test(user_input: Optional[Union[str, List[Union[str, int, float]]]] = None):
        if type(user_input) is list:
            input_string = "\n".join(map(str, user_input))
        else:
            input_string = user_input
        monkeypatch.setattr('sys.stdin', io.StringIO(input_string))
        with open('main.py', 'r') as f:
            exec(f.read())
        captured = capsys.readouterr()
        return captured.out.strip()
    return io_test

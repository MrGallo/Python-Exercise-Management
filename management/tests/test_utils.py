import io
import pytest


from management.utils import calc_difficulty, get_valid_choice


concept_map = {
    "section1": {
        "a": [],
        "f": [],
        "b": ["a"],
        "c": ["b"],
        "g": ["f", "c"]
    },
    "section2": {
        "d": [],
        "e": ["d", "b"],
        "h": ["e", "c"]
    }
}

def test_calc_difficulty():
    assert calc_difficulty([], concept_map) == 1
    assert calc_difficulty(["a"], concept_map) == 2
    assert calc_difficulty(["b"], concept_map) == 3
    assert calc_difficulty(["g"], concept_map) == 6
    assert calc_difficulty(["e"], concept_map) == 5
    assert calc_difficulty(["h"], concept_map) == 7, "Shouldn't count requirements twice."


def test_get_valid_choice(capsys, monkeypatch):
    def fake_input(user_input: str):
        monkeypatch.setattr('sys.stdin', io.StringIO(user_input))
    
    
    captured = capsys.readouterr()

    options = list("abc")

    # valid
    fake_input("1")
    result = get_valid_choice(options, "")
    assert result == 1, "Should give back valid option"

    # out of range
    fake_input("-1\n1")
    get_valid_choice(options, "")
    captured = capsys.readouterr()
    assert "Invalid choice." in captured.out.strip()
    
    fake_input("4\n1")
    get_valid_choice(options, "")
    captured = capsys.readouterr()
    assert "Invalid choice." in captured.out.strip()

    # option 0
    fake_input("0\n1")
    get_valid_choice(options, "")
    captured = capsys.readouterr()
    assert "Invalid choice." in captured.out.strip()

    # non-string
    fake_input("hello\n1")
    get_valid_choice(options, "")
    captured = capsys.readouterr()
    assert "Not a number." in captured.out.strip()

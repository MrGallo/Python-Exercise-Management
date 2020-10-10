from exercise.utils import calc_difficulty


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
    
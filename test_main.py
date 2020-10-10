from exercise.fixtures import captured_output


def test_add(captured_output):
    assert captured_output([3, 4]) == "7"
    assert captured_output([1, 2]) == "3"

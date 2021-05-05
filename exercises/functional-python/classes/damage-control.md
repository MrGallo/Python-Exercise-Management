# Damage Control



**Requirements:**
```eval_rst
- :ref:`fundamentals:write to a file`
- :ref:`fundamentals:boolean operators`

```


You notice that an Agent has been looking at you strangely. You intuitively suspect that they have seen your poorly written code and that they have prepared a negative report that outs you as a noob programmer. You could lose your job, or worse.

Each report is an object of the `Report` class. It's attributes are as follows.

```
Report
======
author: str
date: str
concerning: str
evaluation: str
body: str
```

If any future report to be written to file is about you AND the `evaluation` is `"Incapable"`, change the report `body` to `"They are totally not a noob."` and change the `evaluation` attribute to `"Excellent"`.

A report is about you if your name `"Noob Programmer"` is in the `concerning` field of the report object.

You notice in The Agency's system a function that writes reports to High Command. 
You should hack the function to ensure all reports about you with an `evaluation` of `"Incapable"` get changed (according to the specifications previously mentioned) *before* being written to the report file.

## Starter Code
```python
class Report:
    """Empty Report class for reference."""
    author: str
    date: str
    concerning: str
    evaluation: str
    body: str


def write_report_to_file(report: Report) -> None:
    """Will write a report to High Command.
    
    Args:
        report: The report to send.
    """
    
    with open('report_file.txt', 'a') as f:
        f.write("-" * len(report.date) + "\n")
        f.write(report.date + "\n")
        f.write("-" * len(report.date) + "\n")
        f.write(f"Author: {report.author}\n")
        f.write(f"Concerning: {report.concerning}\n")
        f.write(f"Evaluation: {report.evaluation}\n")
        f.write(f"Body: {report.body}\n\n")
```

## Tests
```python
from dataclasses import dataclass
import pytest
import os

from main import write_report_to_file


REPORT_FILE = "report_file.txt"


@dataclass
class Report:
    """Used for testing"""
    author: str
    date: str
    concerning: str
    evaluation: str
    body: str


def remove_file(file_name: str) -> None:
    if os.path.exists(file_name):
        os.remove(file_name)


def read_file(filename: str) -> None:
    with open(filename, "r") as f:
        return f.read().strip()


@pytest.fixture(autouse=True)
def clear_test_files():
    yield
    remove_file(REPORT_FILE)


def test_writes_to_file():
    report = Report(author="",
                    date="",
                    concerning="concerning",
                    evaluation="evaluation",
                    body="body")
    write_report_to_file(report)

    result_content = read_file(REPORT_FILE)
    assert "concerning" in result_content
    assert "evaluation" in result_content
    assert "body" in result_content


def test_does_not_overwrite_different_persons_incapable_evaluation():
    report = Report(author="",
                    date="",
                    concerning="Someone else",
                    evaluation="Incapable",
                    body="This should not be changed.")
    write_report_to_file(report)

    result_content = read_file(REPORT_FILE)
    assert "Concerning: Someone else" in result_content
    assert "Evaluation: Incapable" in result_content
    assert "Body: This should not be changed." in result_content


def test_does_not_overwrite_different_persons_other_evaluation():
    report = Report(author="",
                    date="",
                    concerning="Someone else",
                    evaluation="Other",
                    body="This should not be changed.")
    write_report_to_file(report)

    result_content = read_file(REPORT_FILE)
    assert "Concerning: Someone else" in result_content
    assert "Evaluation: Other" in result_content
    assert "Body: This should not be changed." in result_content


def test_does_not_change_report_about_you_if_not_incapable():
    report = Report(author="",
                    date="",
                    concerning="Noob Programmer",
                    evaluation="Excellent",
                    body="This should not be changed.")
    write_report_to_file(report)

    result_content = read_file(REPORT_FILE)
    assert "Concerning: Noob Programmer" in result_content
    assert "Evaluation: Excellent" in result_content
    assert "Body: This should not be changed." in result_content


def test_changes_report_evaluation_about_you_if_incapable():
    report = Report(author="",
                    date="",
                    concerning="Noob Programmer",
                    evaluation="Incapable",
                    body="")
    write_report_to_file(report)

    result_content = read_file(REPORT_FILE)
    assert "Concerning: Noob Programmer" in result_content
    assert "Evaluation: Excellent" in result_content


def test_changes_report_body_about_you_if_incapable():
    report = Report(author="",
                    date="",
                    concerning="Noob Programmer",
                    evaluation="Incapable",
                    body="This SHOULD be changed.")
    write_report_to_file(report)

    result_content = read_file(REPORT_FILE)
    assert "Concerning: Noob Programmer" in result_content

    # HINT: DON'T FORGET THE PERIOD!
    assert "Body: They are totally not a noob." in result_content


def test_write_report_to_file_acceptance():
    report = Report(author="",
                    date="",
                    concerning="Noob Programmer",
                    evaluation="Incapable",
                    body="They should be eliminated, for they are a n00b.")
    write_report_to_file(report)

    result_content = read_file(REPORT_FILE)
    assert "Concerning: Noob Programmer" in result_content
    assert "Evaluation: Excellent" in result_content

    # HINT: DON'T FORGET THE PERIOD!
    assert "Body: They are totally not a noob." in result_content
```

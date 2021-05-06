# Neutralization Pt. 1





You realize that changing negative reports about yourself is not enough. You need to get rid of that agent who is going to turn you in for your incompentance. Since you lack the strength and skills necessary to neutralize the agent in physical combat, you must rely on your computer skills to frame them.

You conclude that the best way to get them fired is to alter their Mission Performance Reviews. Every Agent *must* maintain an average of at least 90% on their last five missions or they are let go, no exceptions, no questions asked.

You decide to modify their last five performance grades to drop their average below the 90% threshold.

The first problem is you don't know the entire structure of the `MissionReview` class and how it fits into the `Agent` class.

Create the `MissionReview` class according to the specifications below.

```
MissionReview
=============
mission_name: str
agent_code_name: str
grade: int
text: str
-------------
__init__(self,
         mission_name: str,
         agent_code_name: str,
         grade: int,
         text: str)
```






## Tests
```python
from main import MissionReview


def test_mission_review():
    mr = MissionReview(mission_name="name of mission",
                       agent_code_name="Mr. Silly Pants",
                       grade=50,
                       text="This agent performed admirably")

    assert mr.mission_name == "name of mission"
    assert mr.agent_code_name == "Mr. Silly Pants"
    assert mr.grade == 50
    assert mr.text == "This agent performed admirably"


def test_mission_review_2():
    mr = MissionReview(mission_name="Neutralization",
                       agent_code_name="Noob Programmer",
                       grade=10,
                       text="Quite the noob.")

    assert mr.mission_name == "Neutralization"
    assert mr.agent_code_name == "Noob Programmer"
    assert mr.grade == 10
    assert mr.text == "Quite the noob."
```

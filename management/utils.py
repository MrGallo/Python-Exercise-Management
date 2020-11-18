import json
from typing import List, Dict, Optional, Any


from management.types import SectionConceptMap, ConceptMap, Database


class UniqueNameConstraintError(Exception):
    pass


class ExerciseNotFoundError(Exception):
    pass


def print_title(title: str, underline: str = "=", padding_top: bool = True) -> None:
    if padding_top is True:
        print()
    print(title)
    print(underline * len(title))
    print()


def calc_difficulty(prerequisets: List[str], concepts: SectionConceptMap) -> int:
    flat_concepts = flatten_concepts(concepts)
    return _calc_difficulty(prerequisets, flat_concepts)


def flatten_concepts(concepts: SectionConceptMap) -> ConceptMap:
    flat_concepts = {}
    for section, sub_concepts in concepts.items():
        for k, v in sub_concepts.items():
            flat_concepts[k] = v
    return flat_concepts


def _calc_difficulty(prerequisets: List[str],
                     concepts: ConceptMap,
                     visited: Optional[List[str]] = None) -> int:
    if visited is None:
        visited = []

    difficulty = 1
    for prereq in prerequisets:
        if prereq in visited:
            continue
        visited.append(prereq)
        requirements = concepts[prereq]
        difficulty += _calc_difficulty(requirements, concepts, visited)
    
    return difficulty


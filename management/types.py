from typing import List, Dict, Callable, Tuple, Any


SectionConceptMap = Dict[str, Dict[str, List[str]]]
ConceptMap = Dict[str, List[str]]

Exercise = Dict[str, str]
Chapter = List[Exercise]
Series = Dict[str, Chapter]
ExerciseCollection = Dict[str, Series]
Database = Dict[str, Any]

MenuOptions = Dict[int, Tuple[str, Callable]]

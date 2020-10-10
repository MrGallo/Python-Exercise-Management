print("Get new exercise.")

from exercise.concepts import concepts


for section, concept_dict in concepts.items():
    print(section)
    for name in concept_dict.keys():
        print("\t", name)


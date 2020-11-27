import os

from management.concepts import concepts

FUNDAMENTALS_SITE = "https://mrgallo.github.io/fundamentals/objects.inv"
os.system(f"python -msphinx.ext.intersphinx {FUNDAMENTALS_SITE} > management/fundamentals_index.txt")

with open("management/fundamentals_index.txt", 'r') as f:
    references = f.read()

missing_refs = []
for chapter_name, topics in concepts.items():
    for topic in topics.keys():
        if topic not in references:
            missing_refs.append((chapter_name, topic))

if missing_refs:
    print(*missing_refs, sep="\n")
else:
    print("All good!")
"""
Todo:
- Merge exercise management here.
- (possibly) run tests with a script, not pytest directly
"""

import os

commands = """export PYTHONDONTWRITEBYTECODE=1
poetry install
clear""".split("\n")

# echo "alias pytest='pytest -p no:cacheprovider'" >> ~/.bash_aliases
# source ~/.bash_aliases

for command in commands:
    os.system(command)

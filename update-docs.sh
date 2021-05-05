#!/bin/bash
poetry run python -m sphinx -b html . docs && {
    git add docs/ exercises/ index.rst solutions.rst
    git commit -m "Update Docs"
    git push
}
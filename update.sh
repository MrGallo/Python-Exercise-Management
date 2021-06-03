#!/bin/bash
poetry run python -m sphinx -b html . docs && {
    git add -A
    git commit -m "Update"
    git push
}
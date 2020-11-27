#!/bin/bash
poetry run python -m sphinx -b html . docs
git add docs/ exercises/
git commit -m "Update Docs"
git push
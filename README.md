# Python Exercise Management

### Check references in concepts.py
```sh
$ poetry run python -m management.check_refs
```

### Generate fundamentals autodoc
```sh
$ poetry run python -msphinx.ext.intersphinx https://mrgallo.github.io/fundamentals/objects.inv > management/fundamentals_index.txt
```
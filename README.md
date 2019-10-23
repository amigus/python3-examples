# Python 'examples' Project

A basic Python project that uses
[Pipenv](https://pipenv.kennethreitz.org/en/latest/) for dependency
management with [pytest](https://pytest.org/en/latest/) and
[tox](https://tox.readthedocs.io/en/latest/) for testing.

## Run it

```bash
pipenv install -d
pipenv run tox
```

The `setup.py` file can be used to package and install the project with
`setuptools`.

# Algorithms Problems and Solutions

## Intro

Algorithms problems and solutions written in Python3, including test cases.

## Content

### Algorithm

- [Array](./algo/array)
- [Dynamic](./algo/dynamic)
- [Math](./algo/math)
- [Assorted](./algo/assorted)
- [String](./algo/string)

### Data Structure

- [Stack and Queue](./algo/ds/stack_queue)
- [Linked List](./algo/ds/linked_list)
- [Hash Table](./algo/ds/hash)
- [Tree](./algo/ds/tree)
- [Graph](./algo/ds/graph)

### Sorting

- [Sorting](./algo/sorting)

### Searching

- [Searching](./algo/searching)

## Development Environment

- Python 3 [download](https://www.python.org/downloads/)

## How to run

- Install `pytest`

```
pip install -r requirements.txt
```

- Run test cases:

```
python -m pytest
```

_For Windows 10 users_: You may experience the error: `Permission denied`. To solve this, either run it using Powershell as an admin or use the command:

```
winpty python -m pytest
```

- Run a particular test file:

```
python -m pytest <file_folder/file_name.py>
```

For example:

```
python -m pytest test/array/test_array_chunk.py
```

- Run tests file under a folder:

```
python -m pytest <folder_name>
```

For example:

```
python -m pytest test/array
```

Run tests with watching code change

```
python -m pytest_watch -- --last-failed --new-first
```

## Run in Docker

Under project directory:

```
docker compose watch
```

To view the test results, you can either use Docker desktop or run

```
docker logs <container-name> -f
```

Any changes made locally will trigger the re-run of test cases.

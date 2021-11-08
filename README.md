# AirBnB clone - The console

## Project Description

- A command interpreter to manage our AirBnB objects. The main purpose is to create all classes for AirBnB(`User`, `City`, `Place...) that inherit from a `BaseModel, create a class that takes care of the initialization, serialization and deserialization of instances, an
abstracted storage engine, and unit tests to validate all classes and the storage engine.

## How to use

### In interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
### In non-interactive mode

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## File Descriptions

`AUTHORS` - Lists all individuals having contributed content to the repository

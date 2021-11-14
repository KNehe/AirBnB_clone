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

## Functionalities of the consonle

`quit:` Quit command to exit the program

`EOF:` method to EOF to exit with (CTRL + D)

`empyline:` an empty line + ENTER shouldn’t execute anything

`create:` Create a new object (ex: a new User or a new Place)

`show:` Prints the string representation of an instance based on the class name and id.

`destroy:` Deletes an instance based on the class name and id

`all:` Prints all string representation of all instances based or not on the class name.

`update:` Update attributes of an object

## File Descriptions

`AUTHORS` - Lists all individuals having contributed content to the repository
 
 Nehemiah Kamolu <a href="https://github.com/KNehe/">Github/</a>
 
 Gedion Saiyuah <a href="https://github.com/Sairikei/">Github</a>

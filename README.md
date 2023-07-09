# holbertonschool-AirBnB_clone
# AirBnB_clone - The Console

Command interpreter to manage the AirBnB objects

## About this project

The AirBnB_clone is the first step towards building our first full web application. This web application is composed of:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
- A website (the front-end) that shows the final product to everybody: static and dynamic.
- A database or files that store data (data = objects).
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).

### console

In this project, we will manipulate 2 types of storage: file and database. In this repository, we will focus only on the command interpreter and file storage.

## About the command interpreter (the console)

Command line interpreter that manipulates data and manages serialization and deserialization of objects.

### How it works

The console:
- Displays the prompt (default prompt: "(cmd)", our prompt: "(hbnb)") and waits for user input.
- Reads the entered command and the argument.
- Looks for the function of the command. For example: entering the command "all" makes the console look for the "do_all(self, arg)" function.
- Executes the function.
- If the typed command (the function) doesn't exist, the console prints an error message.
- Quits when the user enters "quit" or "EOF" or presses Ctrl+d.

### The flow of Serialization-Deserialization

```python
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE (file.json) -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```

### Files repartition

```
AirBnB_clone
├── console.py
├── file.json (stores a JSON string representation of objects)
├── AUTHORS
├── README.md
├── tests/ (unittests)
└── models
    ├── __init__.py
    ├── base_model.py
    ├── user.py
    ├── state.py
    ├── place.py
    ├── city.py
    ├── amenity.py
    ├── review.py
    └── engine
        ├── __init__.py
        └── file_storage.py
```

### Files description

- `console.py`: The entry point of the command interpreter.
- `models/__init__.py`: Creates a unique FileStorage instance and reloads the objects.
- `models/base_model.py`: Contains the class BaseModel that defines all common attributes and methods for all other classes.
- `models/user.py`: One of the classes that inherit from BaseModel.
- `models/engine/file_storage.py`: Contains the class FileStorage that serializes instances to a JSON file and deserializes JSON files to instances.


### Usage

You can run this program on your local machine by following these steps:

Step 1: Clone our repository using this command (you need to have git and python3 installed on your machine first):

```bash
git clone https://github.com/yasmineholb/AirBnB_clone.git
```

Step 2: Change directory to AirBnB_clone:

```bash
cd AirBnB_clone
```

Step 3: Execute the console in this way:

```bash
./console.py
```

Step 4: Enter your command. In this example, our command is "help":

```bash
(hbnb) help
```

### Exiting the program

When you want to exit the program, you can use one of the following methods:

1. Enter "quit" or "EOF":

```bash
(hbnb) quit
```

2. Press Ctrl+d.


## Authors

[Zidani Samir, Diallo Adam, Natnael Deboch]


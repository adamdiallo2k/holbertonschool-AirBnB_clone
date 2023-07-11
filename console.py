#!/usr/bin/python3
"""HBNBCommand class for the console"""
from models.engine.file_storage import FileStorage
from datetime import datetime
import models
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that includes methods for the HBNB command interpreter.
    """

    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        command = self.parseline(arg)[0]
        if command is None:
            print('** class name missing **')
        elif command not in self.classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        command = self.parseline(arg)[0]
        arg = self.parseline(arg)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            inst_data = models.storage.all().get(command + '.' + arg)
            if inst_data is None:
                print('** no instance found **')
            else:
                print(inst_data)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        command = self.parseline(arg)[0]
        arg = self.parseline(arg)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            key = command + '.' + arg
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        command = self.parseline(arg)[0]
        objs = models.storage.all()
        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command in self.classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = shlex.split(arg)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""HBNBCommand class for the console"""
from models.engine.file_storage import FileStorage
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
    """HBNBCommand class that includes methods for the HBNB command interpreter."""

    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review}

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
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = globals()[arg]
        except KeyError:
            print("** class donsn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if len(args) < 1:
            print("** instance id missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return

        all_instances = FileStorage.storage.all()
        instance_key = args[0] + '.' + args[1]
        if instance_key in all_instances:
            print(all_instances[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if len(args) < 1:
            print("** instance id missing **")
            return

        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return

        all_instances = FileStorage.storage.all()
        instance_key = args[0] + '.' + args[1]
        if instance_key in all_instances:
            all_instances.pop(instance_key)
            FileStorage.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        from models import storage
        all_instances = storage.all()
        if not arg:
            print([str(instance) for instance in all_instances.values()])
        else:
            try:
                cls = globals()[arg]
            except KeyError:
                print("** class doesn't exist **")
                return

            print([str(instance) for key, instance in all_instances.items() if key.startswith(arg + '.')])


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        from models import storage
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return

        all_instances = storage.all()
        instance_key = args[0] + '.' + args[1]
        if instance_key not in all_instances:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        instance = all_instances[instance_key]
        if hasattr(instance, attribute_name):
            attr_type = type(getattr(instance, attribute_name))
            try:
                attr_value = attr_type(attribute_value)
            except ValueError:
                attr_value = attribute_value
            setattr(instance, attribute_name, attr_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

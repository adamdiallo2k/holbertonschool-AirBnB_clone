#!/usr/bin/python3
"""BaseModel class"""
import cmd
import pickle
from models.user import User
from models import storage
from models.base_model import BaseModel
import sys
import console


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that includes methods for the HBNB command interpreter."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldnt execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    def show(self, user_id):
        for user in self.users:
            if user.id == user_id:
                print(f"User ID: {user.id}")
                print(f"Username: {user.username}")
                print(f"Email: {user.email}")
                return
        print("User not found.")

    def create(self, username, email):
        user_id = len(self.users) + 1
        user = User(user_id, username, email)
        self.users.append(user)
        print("User created successfully.")

    def destroy(self, user_id):
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                print("User deleted successfully.")
                return
        print("User not found.")

    def update(self, user_id, **kwargs):
        for user in self.users:
            if user.id == user_id:
                for key, value in kwargs.items():
                    setattr(user, key, value)
                print("User updated successfully.")
                return
        print("User not found.")

    def all(self):
        if len(self.users) == 0:
            print("No users found.")
        else:
            for user in self.users:
                print(f"User ID: {user.id}")
                print(f"Username: {user.username}")
                print(f"Email: {user.email}")
                print()

    def run(self):
        while True:
            command = input("Enter a command: ")
            command_parts = command.split()

            if len(command_parts) < 2:
                print("Invalid command.")
                continue

            action = command_parts[0]
            entity = command_parts[1]

            if entity.lower() != "user":
                print("Invalid entity.")
                continue

            if action.lower() == "show":
                if len(command_parts) != 3:
                    print("Invalid command. Usage: show user <user_id>")
                    continue
                user_id = int(command_parts[2])
                self.show(user_id)
            elif action.lower() == "create":
                if len(command_parts) != 4:
                    print("Invalid command. Usage: create user <username> <email>")
                    continue
                username = command_parts[2]
                email = command_parts[3]
                self.create(username, email)
            elif action.lower() == "destroy":
                if len(command_parts) != 3:
                    print("Invalid command. Usage: destroy user <user_id>")
                    continue
                user_id = int(command_parts[2])
                self.destroy(user_id)
            elif action.lower() == "update":
                if len(command_parts) < 4:
                    print("Invalid command. Usage: update user <user_id> key1=value1 key2=value2 ...")
                    continue
                user_id = int(command_parts[2])
                kwargs = {}
                for arg in command_parts[3:]:
                    key, value = arg.split("=")
                    kwargs[key] = value
                self.update(user_id, **kwargs)
            elif action.lower() == "all":
                if len(command_parts) != 2:
                    print("Invalid command. Usage: all user")
                    continue
                self.all()
            else:
                print("Invalid command.")

if __name__ == "__main__":
    console = console()
    console.run()
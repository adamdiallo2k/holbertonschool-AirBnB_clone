#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """classs commented"""
    prompt = "(hbnb)"

    def do_exit(self, arg):
        """Exit the shell: EXIT"""
        return True

    def do_quit(self, arg):
        """Quit the shell: QUIT"""
        return self.do_exit(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

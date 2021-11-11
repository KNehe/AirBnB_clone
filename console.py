#!/usr/bin/python3
"""
Module console
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The AirBnB command line interpreter """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" console """
import cmd
import shlex  # for splitting the line along spaces except in double quotes


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    from models.instructor import Instructor
    from models.base_model import BaseModel
    from models.rating import School_Rating, Instructor_Rating
    from models.school import School
    from models.user import User

    classes = {"Instructor": Instructor,
           "BaseModel": BaseModel,
           "School_Rating": School_Rating,
           "Instructor_Rating": Instructor_Rating,
           "School": School,
           "User": User}
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in HBNBCommand.classes:
            new_dict = self._key_value_parser(args[1:])
            instance = HBNBCommand.classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()


    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        from models import storage
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in HBNBCommand.classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                for k, obj in storage.all().items():
                    if k == key:
                        storage.delete(obj)
                        storage.save()
                        print("Deleted")
                    else:
                        print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        from models import storage
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in HBNBCommand.classes:
            obj_dict = storage.all(HBNBCommand.classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_user(self, arg):
        """Gets one specific user from the database via username and password"""
        from models import storage
        args = shlex.split(arg)
        if len(args) == 0:
            print("** Username missing **")
            return False
        elif len(args) < 2:
            print("** Password missing **")
            return False
        user = storage.user(args[0], args[1])
        if user:
            print(user)
        else:
            print("No user with those credentials")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

import cmd
import turtle


class Command(object):
    def __init__(self, function, args):
        self.function = function
        self.args = args

    def execute(self):
        self.function(*self.args)


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '

    def __init__(self):
        super().__init__()
        self.macro = []
        self.is_recording = False

    def do_forward(self, arg):
        self.execute_command(Command(turtle.forward, parse(arg)))

    def do_right(self, arg):
        self.execute_command(Command(turtle.right, parse(arg)))

    def do_left(self, arg):
        self.execute_command(Command(turtle.left, parse(arg)))

    def do_home(self, arg):
        self.execute_command(Command(turtle.home, ()))

    def do_circle(self, arg):
        self.execute_command(Command(turtle.circle, parse(arg)))

    def do_reset(self, arg):
        self.execute_command(Command(turtle.reset, ()))

    def do_record(self, arg):
        self.is_recording = True
        self.macro = []

    def do_stop(self, arg):
        self.is_recording = False

    def do_playback(self, arg):
        for cmd in self.macro:
            cmd.execute()

    def do_bye(self, arg):
        print('Thank you for using Turtle')
        turtle.bye()
        return True

    def execute_command(self, command):
        if self.is_recording:
            self.macro.append(command)
        command.execute()


def parse(arg):
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    TurtleShell().cmdloop()    
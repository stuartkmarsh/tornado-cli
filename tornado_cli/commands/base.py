import sys

class CommandException(Exception):
    def __init__(self, msg):
        sys.stderr.write(msg)

#!/usr/bin/env python
import sys
from optparse import OptionParser 

from tornado_cli.commands import *
         
def main():
    parser = OptionParser()
    (options, args) = parser.parse_args()
    
    if not args:
        return 'Usage: tcli COMMAND or tornado_cli COMMAND\n\nYou must give a command (use "tcli help" to see a list of commands)'
    
    command = args[0]
    try: 
        exec 'from commands.%s import command' % command
    except ImportError:
        return 'Command not found'
    
    return command()             


if __name__ == '__main__':
    exit = main()
    if exit:
        sys.exit(exit)
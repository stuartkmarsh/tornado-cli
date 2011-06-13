from optparse import OptionParser 
from tornado_cli.commands.base import CommandException   
import tornado_cli

import os  
import sys
              
def command():
    parser = OptionParser()
    (options, args) = parser.parse_args()
    dir_name = args[1]
    
    try:                                  
        __import__(dir_name)
    except:
        pass
    else:                                                                                                                                                            
        print "%r conflicts with the name of an existing Python module and cannot be used as a project name. Please try another name." % dir_name 
        
    copy_helper(dir_name)     
        

def copy_helper(name):
    """
    Copies either a Tornado project layout template
    into the specified directory.
    
    """                          
    import re
    import shutil 
    
    directory = os.getcwd()
                                                    
    if not re.search(r'^[_a-zA-Z]\w*$', name): # If it's not a valid directory name.
        # Provide a smart error message, depending on the error.
        if not re.search(r'^[_a-zA-Z]', name):
            message = 'make sure the name begins with a letter or underscore'
        else:
            message = 'use only numbers, letters and underscores'
        raise CommandException("%r is not a valid %s name. Please %s." % (name, message))
    top_dir = os.path.join(directory, name)
    try:
        os.mkdir(top_dir)
    except OSError as (errno, strerror):
        if errno == 17:
            sys.stderr.write('Directory %r already exists\n' % name)
        else:
            sys.stderr.write(strerror + '\n')
        return

    # Determine where the app or project templates are. Use
    # tornado_cli.__path__[0] because we don't know into which directory
    # tornado_cli has been installed.
    template_dir = os.path.join(tornado_cli.__path__[0], 'project_template')

    for d, subdirs, files in os.walk(template_dir):
        relative_dir = d[len(template_dir)+1:]
        if relative_dir:
            os.mkdir(os.path.join(top_dir, relative_dir))
        for subdir in subdirs[:]:
            if subdir.startswith('.'):
                subdirs.remove(subdir)
        for f in files:
            if f.endswith('.pyc') or f.endswith('empty'):
                # Ignore .pyc, .empty files
                continue
            path_old = os.path.join(d, f)            
            path_new = os.path.join(top_dir, relative_dir, f)       
            try:                       
                shutil.copy(path_old, path_new)    
                _make_writeable(path_new)
            except OSError:
                sys.stderr.write("Notice: Couldn't set permission bits on %s. You're probably using an uncommon filesystem setup. No problem.\n" % path_new)        

def _make_writeable(filename):
    """
    Make sure that the file is writeable. Useful if our source is
    read-only.

    """
    import stat
    if sys.platform.startswith('java'):
        # On Jython there is no os.access()
        return
    if not os.access(filename, os.W_OK):
        st = os.stat(filename)
        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
        os.chmod(filename, new_permissions) 
                                        
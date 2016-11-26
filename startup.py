#!/usr/bin/env python
"""
setting python 
read and save commandline
#need setting 
enviroment variable
$pythonstartup __file__
__file__=(this file path)
this method is save command list in .history
readline.read_history_file
"""
print ("python startup from %homepath%python_learning!")
print ("reading histry")
try:
    import os
    import readline
    import atexit
    import traceback
    histfile = os.path.join(os.environ["pythonpath"], ".pyhist")
    open(histfile, 'a').close()
    readline.read_history_file(histfile)
    atexit.register(readline.write_history_file, histfile)
except IOError:
    print("Fail"+traceback.format_exc())
    pass

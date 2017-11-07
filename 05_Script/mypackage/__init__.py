##!/usr/bin/env python
## -*- coding: utf-8 -*-
## vim: ai ts=4 sts=4 et sw=4 nu
#
##from file import file
##from file2 import file2
##from file3 import file3
#
## Note: To avoid that a function appear in the list of possibilities, you can use
## in Python a variable with __ before to exclude it from appearing in console
#from os.path import splitext as __splitext
#from os.path import join as __join
#from os.path import basename as __basename
#from os.path import dirname as __dirname
#from glob import glob as __glob
#
## get all *.py filenames in __file__'s folder that are not __file__.
#__files=[__splitext(__f)[0] for __f in __glob(__join(__dirname(__file__), '*.py')) 
#       if __f != __basename(__file__)] 
#
## define importer function
#def __importer(name, root_package=False, relative_globals=None, level=-1):
#    """ We only import modules, functions can be looked up on the module.
#    Usage: 
#
#    from foo.bar import baz
#    >>> baz = importer('foo.bar.baz')
#
#    import foo.bar.baz
#    >>> foo = importer('foo.bar.baz', root_package=True)
#    >>> foo.bar.baz
#
#    from .. import baz (level = number of dots)
#    >>> baz = importer('baz', relative_globals=globals(), level=2)
#    """
#    return __import__(name, locals=None, # locals has no use
#                      globals=relative_globals, 
#                      fromlist=[] if root_package else [None],
#                      level=level)
#
## Loop to add to the path
#for __i in range(0,len(__files)):
#    __importer(__files[__i].replace('\\','.'))

def _import_package_files():
    """ Dynamically import all the public attributes of the python modules in this
        file's directory (the package directory) and return a list of their names.
    """
    import os
    exports = []
    globals_, locals_ = globals(), locals()
    package_path = os.path.dirname(__file__)
    package_name = os.path.basename(package_path)

    for filename in os.listdir(package_path):
        modulename, ext = os.path.splitext(filename)
        if modulename[0] != '_' and ext in ('.py', '.pyw'):
            subpackage = '{}.{}'.format(package_name, modulename) # pkg relative
            module = __import__(subpackage, globals_, locals_, [modulename])
            modict = module.__dict__
            names = (modict['__all__'] if '__all__' in modict else
                     [name for name in modict if name[0] != '_'])  # all public
            exports.extend(names)
            globals_.update((name, modict[name]) for name in names)

    return exports

__all__ = ['__all__'] + _import_package_files()  # '__all__' in __all__

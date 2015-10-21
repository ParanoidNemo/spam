# S.P.A.M. - (a) Simple Python Awfull Module

Spam is a module created to expand the possibility of python scripting, stricly releated to create new BE::Shell
functionality. Right now it's under heavy development, so not every module is finished and some of them could don't even
work correctly. See below the list of fully working modules.

## Requirements
In order to use spam you have to install the follow dependencies and have a python versione >= 3.4.
Some module could maybe work even on precedent version, but it's highly recommended to not use it.
Right now I've no plan to port it on python2 too.

Dependencies:
* gitpython   (for beshell module)
* musicpd (for music module)

## Installation

### by Script
In order to install spam you could use the installation script that you can find into the resources folder. Just run it
and enjoy. :D

### Manually
You can also install spam manually by coping the spam directory into your python site-packages dir or in whatever 
location you want and adding a spam.pth file containig the location path (minus the actual spam dir) into your python 
site-packages dir

    e.g.
    $ cat /usr/lib/python3.4/site-packages/spam.pth
    
    '/home/username/.local/share/'

## Usage
You can now use the module inside the spam dir simply calling it in your python code

    e.g.
    import spam
    from spam import beshell
    from spam import *

the last example is, right now, the suggested one because it'll import only the fully working modules

# Working modules
* [beshell](https://github.com/ParanoidNemo/spam/wiki/beshell)
* [check](https://github.com/ParanoidNemo/spam/wiki/check)
* archive
* fs
* music
* [webmail](https://github.com/ParanoidNemo/spam/wiki/webmail)

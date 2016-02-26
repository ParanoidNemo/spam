beshell - Global beshell types
=====

The beshell module supplies three global functions and two classes for checking the status of your BE::Shell installation, manteining it and gather informations.

beshell.**up** - Check if there are any update to the git master branch of BE::Shell, compairing that to your local copy of the repo and merge the branch if there are some.

beshell.**install** - Same as up but instead of check for update clone the repo in a choosen location and compile the shell.

beshell.**backup** - Check if there are any configuration in use and, if so, create a backup (.tar archive, containing the configuration file and the releated theme) in a default location.

## Configuration Objects
Configuration.**config_dir** - return the abs path of the directory where the main configuration file is located.

Configuration.**main_file** - return the abs path of the configuration file of BE::Shell (be.shell)

Configuration.**main_dir** - return the abs path of the directory where are located the other resources for BE::Shell (e.g. Themes dir)

## Theme Objects
Theme.**name** - return the name of the current theme.

Theme.**path** - return the path of the directory where the current theme is located.

Theme.**l_list** - return a dict containing the themes already installed into the system (default location).

Theme.**d_list** - return a dict containing the themes downloaded into the default location.
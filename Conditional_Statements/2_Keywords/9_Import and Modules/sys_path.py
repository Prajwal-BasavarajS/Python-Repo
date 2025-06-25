import sys

print(sys.path)


# ['',
#  '/usr/lib/python3.10',
#  '/usr/lib/python3.10/lib-dynload',
#  '/home/prajwal/.local/lib/python3.10/site-packages']
# Explanation of each entry:
# '' (Empty string)

# This means the current working directory (the folder where the Python script is being run from).

# Python checks this directory first when importing modules.

# If you have a file like my_utils.py in the same folder, you can just do import my_utils.

# /usr/lib/python3.10

# This is a system directory where Python's standard library modules are stored.

# These include built-in modules like os, math, sys, etc.

# /usr/lib/python3.10/lib-dynload

# Contains dynamically loaded shared objects (usually .so files).

# These are compiled binary extensions of some built-in modules written in C.

# /home/prajwal/.local/lib/python3.10/site-packages

# This is where user-installed third-party packages are stored.

# If you use pip install --user some_package, it goes here.


# Pear
The Pear programming language, coded in python.
## Examples
For examples, navigate to the examples directory. If something like 'io' is found, it should be a module that is included automatically with a release.
## Packages
Packages are most likely the best thing of Pear. It allows you to add your own commands. Packages are written in Python, and a package directory looks like the following:
```
package_yourname
|
|--- main.py
|
```
Here you have the contents of `main.py`:
```py
def hello(*args, tape): # Tape is the memory, interpreter will automatically insert it here. Args are also automatically given by the interpreter.
    print("Hello, World!")
pearcom = {
    "hello": hello
}
```
In a Pear script, you would use
```
include package_yourname
package_yourname hello
```
There you go! You have your first working package for Pear!
## Installation
Currently not a guide, will be written later.

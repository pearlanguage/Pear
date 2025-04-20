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
    "hello": hello # pearcom is used to define the commands
}
```
In a Pear script, you would use
```
include package_yourname
package_yourname hello
```
There you go! You have your first working package for Pear!

## Running your Pear scripts.
First, you will need to write a pear script.
For example: 
```
insert 5 0
insert 4 1
add 0 1 2
```
This script will just add 5 and 4 into register 2.

Then, you will create a directory, i will call it `Pear`.

In this directory, place your Pear interpreter of any version.
To run your script, you can use `python3 Pear/pear.py your_script_name.pear`.

If u want to import packages, i recommend making a `packages` directory, putting your Pear packages in `packages`, and then using `include packages/package1` to use a package in your script.

You have now ran your first Pear script.

## Installation
Currently not a guide, will be written later.

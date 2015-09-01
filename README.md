# FileReloader

FileReloader is a plugin for [Sublime Text](https://www.sublimetext.com/) that allows you to reload all open files using a hotkey.

## Installation

### Package Control

Installation through [Package Control](https://packagecontrol.io/installation) is recommended.

* Bring up the Command Palette (Command+Shift+P on OS X, Control+Shift+P on Linux/Windows).
* Select `Package Control: Install Package`
* Search for and select `FileReloader`

## Usage

The default key binding is `F5`.

To add a key binding, open "Preferences / Key Bindings - User" and add:

``` js
{ "keys": ["ctrl+shift+r"], "command": "reload_all_files" }
```

With this setting, pressing <kbd>ctrl + shift + r</kbd> will reload all open files! For OSX users, quoting wbond:
"When porting a key binding across OSes, it is common for the ctrl key on
Windows and Linux to be swapped out for super on OS X"
(eg. use "super+shift+r" instead).

*Beware*: the binding from this example overrides the default ST's mapping
for `goto_symbol_in_project`. You can look at the default bindings in
"Preferences / Key Bindings - Default".

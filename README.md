# XY

Listens for a keyboard event and moves the current focused window to the (0, 0) position on the main screen. This program will run in the background until the key __CTRL__ + __Down Arrow__ combination is pressed to exit the program

## Use Case

Occasionally a program will try and display off screen. Sometimes without a way to move the application without being able to see and access the title bar. Without the title bar being visible, the application is rendered practically useless as it is off any visible monitor. This program will listen for the keypress of __CTRL__ + __\`__ (the keybard key to the left of the number 1) and move the current in focus window to a visible portion of the screen.

## References

Reference | Link
--------- | ----
PyHook Docs | http://pyhook.sourceforge.net/doc_1.5.0/pyhook.HookManager-module.html
Virtual Key Codes | https://docs.microsoft.com/en-us/windows-hardware/customize/enterprise/keyboardfilter-key-names
Skeleton Example | https://github.com/techmetal-challenger/python-examples/blob/master/Keyboard%20Events/keybind.py

#   Author: Jonathan Brooks
#   Created: 3-20-2018
#   Purpose: Repostion any selected window to 0,0 X Y position on the Main Display
#   Use Case: Windows that are unmovable due to title bars outside screen space

# pyHook Allows keyboard input when program is not in focus
# win32gui allows pulling focused window properties
import pyHook, pythoncom, win32gui, sys

# Function to be called whenever a keyboard key is pressed
def OnKeyboardEvent(event):
    # Check to see if Ctrl is currently held down
    ctrl_pressed = pyHook.GetKeyState(pyHook.HookConstants.VKeyToID('VK_CONTROL'))
    # When holding Ctrl and pressing ` the focused window will re-position
    if ctrl_pressed and event.KeyID == 192:
        # Grab the currently active Window
        activeWindow = win32gui.GetForegroundWindow()
        # Obtain the window X, Y, Adjusted Height, Adjusted Width
        # Width and Height in Rectangle add the X and Y values to it
        activeWindowRectangle = win32gui.GetWindowRect(activeWindow)
        # Obtain the window width and height by subtracting the X and Y values
        activeWindowHeight = activeWindowRectangle[2] - activeWindowRectangle[0]
        activeWindowWidth = activeWindowRectangle[3] - activeWindowRectangle[1]
        # Re-Position the Window to 0, 0 on the Main Display maintain Window Size
        win32gui.MoveWindow(activeWindow, 0, 0, activeWindowHeight, activeWindowWidth, True)
    # When holding Ctrl and pressing the Down Arrow, exit this program
    if ctrl_pressed and event.KeyID == 40:
        sys.exit(0)
    print(event.KeyID)
    return True

# Create a Hook Manager
hookManager = pyHook.HookManager()
# Respond to Keyboard key presses by calling the on keyboard event
hookManager.KeyDown = OnKeyboardEvent
# Connect the Hook Manager to the Keyboard
hookManager.HookKeyboard()
# Wait in the background
pythoncom.PumpMessages()

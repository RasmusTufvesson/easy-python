#import win32api, win32con
import pyautogui
#import keyboard
#import time
#from PIL import Image

#class image(Image):

class Bot:
    #def set_cursor_pos(self, x, y):
    #    pyautogui.moveTo(#win32api.SetCursorPos((x,y))
    set_cursor_pos = pyautogui.moveTo
    get_cursor_pos = pyautogui.position
    move_cursor = pyautogui.move
    drag_cursor_to_pos = pyautogui.dragTo
    drag_cursor = pyautogui.drag
    click = pyautogui.click
    double_click = pyautogui.doubleClick
    mouse_button_down = pyautogui.mouseDown
    mouse_button_up = pyautogui.mouseUp
    scroll_mouse_updown = pyautogui.scroll
    scroll_mouse_leftright = pyautogui.hscroll

    #def click(self, click_time=0.1):
    #    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #    time.sleep(click_time)
    #    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #
    #def click_at(self, x, y, click_time=0.1):
    #    self.set_cursor_pos(x, y)
    #    self.click(click_time)
    
    screenshot = pyautogui.screenshot
    locate = pyautogui.locateOnScreen
    locate_all = pyautogui.locateAllOnScreen

    #def get_pixel_color(self, x, y):
    #    return pyautogui.pixel(x, y)

    get_pixel_color = pyautogui.pixel
    pixel_match_color = pyautogui.pixelMatchesColor

    press_key = pyautogui.press
    key_down = pyautogui.keyDown
    key_up = pyautogui.keyUp
    write = pyautogui.write
    keyboard_shortcut = pyautogui.hotkey

    pressable_keys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

    ok_message_box = pyautogui.alert
    button_message_box = pyautogui.confirm
    ok_cancel_message_box = pyautogui.prompt
    censored_message_box = pyautogui.password
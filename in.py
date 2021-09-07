from contextlib import suppress
from pynput.keyboard import Controller as keyboardController,Key
from pynput.mouse import Button, Controller as mouseController


import keyboard


mouse = mouseController()

kbControl = keyboardController()
#프로그램 종료
kill = 'esc'
# r=확대 , f=축소
screen_plus = 'r'
screen_reduce = 'f'
#원래 크기로
recover_size = 'e'
#저장
save_key = 'a'


def Kill(): 
    quit()

def ctrlHotKey(key):
    kbControl.press(Key.ctrl)
    kbControl.press(key)
    kbControl.release(key)
    kbControl.release(Key.ctrl)

def autoScrollKey(key):
    kbControl.press(Key.ctrl)
    mouse.scroll(0, key)
    kbControl.release(Key.ctrl)
    

def screenPlus():
    autoScrollKey(2)

def screenReduce():
    autoScrollKey(-2)

def recoverSize():
    ctrlHotKey('0')

def saveKey():
    ctrlHotKey('s')

keyboard.add_hotkey(kill, Kill,args=(),suppress=True)
keyboard.add_hotkey(screen_plus, screenPlus,args=(),suppress=True)
keyboard.add_hotkey(screen_reduce, screenReduce,args=(),suppress=True)

input()

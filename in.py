
from contextlib import suppress
from pynput.keyboard import Controller as keyboardController,Key
from pynput.mouse import Button, Controller as mouseController
from time import sleep
import keyboard


mouse = mouseController()

kbControl = keyboardController()

kill = 'esc' #프로그램 종료
screen_plus = 'r'# r=확대 , f=축소
screen_reduce = 'f'
recover_size = 'e' #원래 크기로
save_key = 'a' #저장
drag_mouse = 'd'
right_click = 'g'
delete_key = 's'
delete_x = 'x'
key_point = 'q'
remove_point = 'w'
init_position = (878,548)

bounding_box = ['1','2','3','4','5','6','7','8','9','0']
box_point = [430,462,492,522,546,568,604,629,670,698]


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

def dragMouse():
    x,y = mouse.position
    mouse.position = (x,y)
    kbControl.press(Key.ctrl)
    mouse.press(Button.left)
    kbControl.release(Key.ctrl)

   

def rightClick():
    mouse.click(Button.right)

def deleteKey():
    kbControl.press(Key.delete)
    kbControl.release(Key.delete)        
 
def keyPoint():
    
    mouse.position = (init_position)
    mouse.click(Button.right)
    mouse.position = (926,561)
    mouse.click(Button.left)

def removePoint():
    mouse.position = (init_position)
    mouse.click(Button.right)
    mouse.position = (973, 593)
    mouse.click(Button.left)
   
def boxSelector(y_pos):
    mouse.position = (init_position)
    mouse.click(Button.right)
    mouse.position = (1026,429)
    sleep(0.1)
    mouse.position = (1218,y_pos)
    mouse.click(Button.left)
   
def boundingBox_1():
    boxSelector(box_point[0])
def boundingBox_2():
    boxSelector(box_point[1])
def boundingBox_3():
    boxSelector(box_point[2])
def boundingBox_4():
    boxSelector(box_point[3])
def boundingBox_5():
    boxSelector(box_point[4])
def boundingBox_6():
    boxSelector(box_point[5])
def boundingBox_7():
    boxSelector(box_point[6])
def boundingBox_8():
    boxSelector(box_point[7])
def boundingBox_9():
    boxSelector(box_point[8]) 
def boundingBox_0():
    boxSelector(box_point[9])


keyboard.add_hotkey(kill, Kill,args=(),suppress=True)
keyboard.add_hotkey(screen_plus, screenPlus,args=(),suppress=True)
keyboard.add_hotkey(screen_reduce, screenReduce,args=(),suppress=True)
keyboard.add_hotkey(recover_size,recoverSize,args=(),suppress=True)
keyboard.add_hotkey(save_key,saveKey,args=(),suppress=True)
keyboard.add_hotkey(drag_mouse,dragMouse,args=(),suppress=True)
keyboard.add_hotkey(right_click,rightClick,args=(),suppress=True)
keyboard.add_hotkey(delete_key,deleteKey,args=(),suppress=True)
keyboard.add_hotkey(delete_x,deleteKey,args=(),suppress=True)
keyboard.add_hotkey(key_point,keyPoint,args=(),suppress=True)
keyboard.add_hotkey(remove_point,removePoint,args=(),suppress=True)

keyboard.add_hotkey(bounding_box[0],boundingBox_1,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[1],boundingBox_2,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[2],boundingBox_3,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[3],boundingBox_4,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[4],boundingBox_5,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[5],boundingBox_6,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[6],boundingBox_7,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[7],boundingBox_8,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[8],boundingBox_9,args=(),suppress=True)
keyboard.add_hotkey(bounding_box[9],boundingBox_0,args=(),suppress=True)

input()

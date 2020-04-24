import win32gui
import time

def sendMsg(hwnd2, msg):
    win32gui.SendMessage(hwnd2, 0x000c, 0, msg)
    win32gui.PostMessage(hwnd2, 0x0100, 0xD, 0x1C001)

f = open('utterance.txt', 'r')
room = f.readline().strip()
ut_list = [ut.strip() for ut in f.readlines() if ut is not "\n"]

hwnd1 = win32gui.FindWindow(None, room)
hwnd2 = win32gui.FindWindowEx(hwnd1, 0, "RichEdit20W", "")

for ut in ut_list:
    sendMsg(hwnd2, ut)
    time.sleep(4)
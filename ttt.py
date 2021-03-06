import win32gui
import pywintypes
import sys
 
# 부모 윈도우의 핸들을 검사합니다.
class WindowFinder:
    def __init__(self, windowname):
        win32gui.EnumWindows(self.__EnumWindowsHandler, windowname) 
 
    def __EnumWindowsHandler(self, hwnd, extra):
        wintext = win32gui.GetWindowText(hwnd)
        if wintext.find(extra) != -1:
            self.__hwnd = hwnd
            return False # FALSE는 예외를 발생시킵니다.    
 
    def GetHwnd(self):
        return self.__hwnd
 
    __hwnd = 0
 
# 자식 윈도우의 핸들 리스트를 검사합니다.
class ChildWindowFinder:
    def __init__(self, parentwnd):
        win32gui.EnumChildWindows(parentwnd, self.__EnumChildWindowsHandler, None)     
 
    def __EnumChildWindowsHandler(self, hwnd, extra):
        self.__childwnds.append(hwnd)
 
    def GetChildrenList(self):
        return self.__childwnds
 
    __childwnds = []


# windowname을 가진 윈도우의 모든 자식 윈도우 리스트를 얻어낸다.
def GetChildWindows(windowname):
 
    # TeraCopy의 window handle을 검사한다.
    teracopyhwnd = WindowFinder('TeraCopy').GetHwnd()
 
    # Teracopy의 모든 child window handle을 검색한다.
    childrenlist = ChildWindowFinder(teracopyhwnd).GetChildrenList()
 
    return teracopyhwnd, childrenlist
 
# main 입니다.
def main(argv):
    hwnd, childwnds = GetChildWindows('TeraCopy')
    print("%X %s" % (hwnd, win32gui.GetWindowText(hwnd)))
 
    print("HWND     CtlrID\tClass\t\t\tWindow Text")
    print("===========================================")
 
    for child in childwnds:
        ctrl_id  = win32gui.GetDlgCtrlID(child)
        wnd_clas = win32gui.GetClassName(child)
        wnd_text = win32gui.GetWindowText(child)        
        print("%08X %6d\t%s\t\t\t%s" % (child, ctrl_id, wnd_clas, wnd_text))
 
    return 0
 
if __name__ == '__main__':
    sys.exit(main(sys.argv))
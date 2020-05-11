import win32gui

def find(hwnd):
    chwnd = win32gui.FindWindowEx(hwnd, None, None, None)
    while chwnd is not 0:
        print(win32gui.GetClassName(chwnd))
        find(chwnd)
        chwnd = win32gui.FindWindowEx(hwnd, chwnd, None, None)

hwnd1 = win32gui.FindWindow(None, "TEST - Chrome")
find(hwnd1)
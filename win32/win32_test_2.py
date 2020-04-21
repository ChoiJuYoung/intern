import win32gui

hwnd1 = win32gui.FindWindow(None, "카카오톡")
hwnd2 = win32gui.FindWindowEx(hwnd1, None, None, None)
hwnd3 = win32gui.FindWindowEx(hwnd2, None, None, None)
hwnd4 = win32gui.FindWindowEx(hwnd3, None, None, None)


total = ""
while hwnd4 is not 0:
    print(hwnd4)
    total += (str(hwnd4) + " // ")
    hwnd4 = win32gui.FindWindowEx(hwnd3, hwnd4, None, None)
    
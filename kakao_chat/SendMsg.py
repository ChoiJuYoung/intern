# win32 설치 = pip install pypiwin32
import win32gui
import time

def sendMsg(hwnd2, msg): # hwnd2에 메시지 보내는 메서드
    win32gui.SendMessage(hwnd2, 0x000c, 0, msg) # SET TEXT TO MESSAGE BOX
    win32gui.PostMessage(hwnd2, 0x0100, 0xD, 0) # SEND CR(CARRIAGE RETURN = ENTER)

f = open('utterance.txt', 'r') # READ FILE
room = f.readline().strip() # GET KAKAOTALK ROOM'S NAME FROM FILE
ut_list = [ut.strip() for ut in f.readlines() if ut is not "\n"] # READ ALL UTTERANCE

hwnd1 = win32gui.FindWindow(None, room) # GET THE ROOM'S HANDLE
hwnd2 = win32gui.FindWindowEx(hwnd1, 0, "RichEdit20W", "") # GET MESSAGEBOX'S HANDLE

for ut in ut_list: # FOR ALL UTTERANCE
    sendMsg(hwnd2, ut) # SEND MSG TO KAKAOTALK
    time.sleep(5) # WAIT 5 SECONDS

# 시간텀을 변경하고 싶다면 time.sleep()부분 초 변경. parameter로는 초(밀리초 아님!)가 주어짐.


"""
# utterance.txt 파일 구성

# 방 이름 (갠톡일 경우 챗봇 이름)
# 이후 보낼 메시지 쭉 열거
# 저장 시 다른이름으로 저장을 사용해 인코딩을 ANSI로 해주기 (기본적으로 UTF-8)
# cp949 decode error가 나온다면, 인코딩이 ANSI가 아닌 것.
"""


"""
# COMMENT FOR WIN32GUI

=====================================================================
int = SendMessage(hwnd, message, wparam, lparam)
    hwnd: int
        the handle to the Window
    message: int
        The ID of the message to post
    wparam=None: int/str
        Type depends on the message
    lparam=None: int/str
        Type depends on the message


0x000C는 WM_SETTEXT
text property를 setting하라는 window message
즉, win32gui.SendMessage(hwnd2, 0x000c, 0, msg)는 handle값이 hwnd2인 친구에게 msg라는 값을 SET하라는 뜻.


# message에 따른 wparam, lparam의 값의 역할은 https://mhyun.tistory.com/86 이곳을 참조 가능.
# wParam은 16비트 값이었으므로 W라고 불리고, lParam은 32비트값이었어서 L이라 불렸다.
# W매개변수는 핸들이나 정수값을 전달하는데 사용되었고, L매개변수는 포인터를 전달하는데 사용되었다.
# 윈도우즈가 32비트로 바뀔 때 WParam역시 32비트로 확장되었다.
# 64비트 윈도우에서는 두 매개변수 모두 64비트 값이다.
=====================================================================

int = PostMessage(hwnd, message, wparam, lparam)

0x0100은 WM_KEYDOWN
    WM_KEYDOWN에서의 wParam
        WM_KEYDOWN메시지는 키보드를 누를 때마다 윈도우로 전달되는데 문자가 아닌 모든 키에 대해서도 발생.
        단, Alt키와 윈도우 키, 한영 전환키 등 특수 키 몇가지는 제외.

        이때, wParam으로는 문자 코드가 아닌 가상 키코드라는 것이 전달된다.

        숫자 및 영문자의 가상 키코드는 아스키 코드와 같으며 매크로 상수는 정의되어 있지 않으므로
        문자 상수와 wParam을 바로 비교하면 된다.
        단, 영문자의 경우는 대문자 코드와 일치되어 있으므로 반드시 대문자와 비교해야 한다.

        0xD는 CR(Carriage Return)을 의미한다.

    WM_KEYDOWN에서의 lParam
        키의 눌림/놓음 상태, 메시지가 보내지기 전 키의 상태, alt키, 오른쪽 Alt, Ctrl 키, 반복 카운트 등의 정보.
        WM_KEYDOWN에서는 중요치 않은 값.
"""
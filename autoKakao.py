import sys
import time
import os
import pyautogui
import pyperclip
import numpy as np
from io import BytesIO
import win32clipboard
from PIL import Image

# 클립보드로 이미지 저장
def send_to_clipboard(filepath,clip_type=win32clipboard.CF_DIB):
    try:
        image = Image.open(filepath)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()
        print('이미지를 클립보드에 복사했습니다.')
        return True
    except Exception as e:
        print(e)
        return False
		
def send_msg(msg):
    i = 0
    while True:

        if isLastFriend():
            break

        print('Repeat Number : ', i + 1, end='')
        time.sleep(0.5)
        pyautogui.keyDown('enter')
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.keyDown('enter')
        if send_to_clipboard('msg.jpg'): # msg.jpg 파일이 존재하면 클립보드로 복사
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.keyDown('enter')
            time.sleep(1)
        time.sleep(1)
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')

def isLastFriend():
    global im_array
    location = pyautogui.locateCenterOnScreen(img_path + 'list_icon.png', confidence = conf)
    x = location.x
    y = location.y
    im = pyautogui.screenshot(region=(x, y, 250, 40))

    if np.array_equal(im_array, np.array(im)):
        return True
    else:
        im_array = np.array(im)
        return False

def filter_friend(filter_keyword):
    # 사람 아이콘 클릭
    try:
        click_img(img_path + 'person_icon.png')
        try:
            click_img(img_path + 'person_icon2.png')
        except Exception as e :
            print('e ', e)
    except Exception as e :
        print('e ', e)
    # X 버튼이 존재한다면 클릭하여 내용 삭제
    try:
        click_img(img_path + 'x.png')
    except:
        pass
    time.sleep(0.2)
    # 돋보기(검색) 아이콘 클릭
    click_img(img_path + 'search_icon.png')
    if filter_keyword == '':
        pyautogui.keyDown('esc')
    else:
        pyperclip.copy(filter_keyword)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.2)

def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x = location.x
    y = location.y
    pyautogui.click(x, y)

def set_ready():
    print("카카오톡을 화면 최상단에 띄워주시고 로그인해 놓으십시오.\n\n")
    input("메시지 전송을 실행하시겠습니까? [Enter]")
    delay_time = '3'
    print(delay_time + "초 후에 프로그램을 실행합니다.")
    for remaining in range(int(delay_time), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r프로그램을 실행하겠습니다!\n")

def bye_msg():
    input('\n\n메시지 전송이 완료됐습니다. 종료하기[Enter]')

def get_import_msg():
    with open("msg.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        print('======== 아래는 전송할 텍스트입니다. ========\n')
        print(text)
        print('\n=============================================\n')
        return text

def initialize():
    print('Monitor size : ', end='')
    print(pyautogui.size())
    filter_keyword = input("필터링할 친구 이름. 없으면 enter(검색 없이 전체 대상) : ")
    return filter_keyword

# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.90
pyautogui.PAUSE = 0.5
isLast = False
im_array = []

if __name__ == "__main__":
    filter_keyword = initialize()
    msg = get_import_msg()
    set_ready()
    filter_friend(filter_keyword)
    send_msg(msg)
    bye_msg()
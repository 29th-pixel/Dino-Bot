import pyautogui
from PIL import Image, ImageGrab
import time


def press(key):
    pyautogui.keyDown(key)


def iscollide(data):
    for i in range(260, 280):
        for j in range(350, 390):
            if data[i, j] < 90:
                press("down")
                return

    for i in range(260, 280):
        for j in range(400, 460):
            if data[i, j] < 90:
                press("up")
                return
    return


if __name__ == '__main__':
    time.sleep(3)
    press("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)
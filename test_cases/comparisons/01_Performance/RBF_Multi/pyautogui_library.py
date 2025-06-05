import pyautogui
import time

class PyAutoGUI:
    def typewrite(self, text):
        pyautogui.typewrite(text)

    def press(self, key):
        pyautogui.press(key)

    @staticmethod
    def get_time_in_milliseconds():
        return int(round(time.time() * 1000))

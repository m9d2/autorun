import os


def screenCap(screenPath):
    os.system('adb shell screencap -p ' + screenPath)


def click(x, y):
    command = ('adb shell input tap ' + str(x) + ' ' + str(y))
    os.system(command)


class AdbHelper:

    def __init__(self, url, port):
        os.system('adb connect ' + url + ':' + port)
        os.system('adb devices')


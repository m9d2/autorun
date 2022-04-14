import time
import datetime

from tools.adb import AdbHelper, click, screenCap
from tools.ocr import OcrHelper
from tools.send_email import sendMail


def init():
    AdbHelper('127.0.0.1', '62001')
    ocrHelper = OcrHelper()
    return ocrHelper


if __name__ == '__main__':
    ocr = init()
    screenPath = '/sdcard/Pictures/01.png'
    screenRealPath = 'C:\\Users\\Administrator\\Nox_share\\ImageShare\\01.png'
    i = 0
    while True:
        screenCap(screenPath)

        position = ocr.position(screenRealPath, '我的订单')
        if position[0] > 0 and position[1] > 0:
            position = ocr.position(screenRealPath, '购物车')
            click(position[0], position[1])
            continue

        position = ocr.position(screenRealPath, '结算')
        if position[0] > 0 and position[1] > 0:
            click(position[0], position[1])
            time.sleep(1)
            continue

        position = ocr.position(screenRealPath, '取消')
        if position[0] > 0 and position[1] > 0:
            click(position[0], position[1])
            continue

        position = ocr.position(screenRealPath, '我知道了')
        if position[0] > 0 and position[1] > 0:
            click(position[0], position[1])
            click(32, 60)
            continue

        position = ocr.position(screenRealPath, '去支付')
        if position[0] > 0 and position[1] > 0:
            click(position[0], position[1])

            i = i + 1
            d = datetime.datetime.now()
            log = '已抢购 ' + str(i) + ' 次'
            print('%s - %s' % (d, log))
            continue

        position = ocr.position(screenRealPath, '微信支付')
        if position[0] > 0 and position[1] > 0:
            click(position[0], position[1])

            position = ocr.position(screenRealPath, '确认支付')
            click(position[0], position[1])

            sendMail('抢到了，快去支付！！')
            break


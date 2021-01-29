import sys
import os
import logging
from waveshare_epd import epd2in13_V2
from PIL import Image,ImageDraw,ImageFont
import traceback
from datetime import datetime
import urllib.request

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("p-cal screen handler initialized")

    f = open("/home/pi/p-cal/2021.txt")
    lines = f.readlines()

    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    # Drawing on the image
    logging.info("1.Drawing on the image...")
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    #	DRAW RULER
    colCount = 4
    while (colCount <= 244):
        draw.line([(colCount,100),(colCount,100)], fill = 0,width = 1)
        colCount += 8

    colCount = 36
    while (colCount <= 236):
        draw.line([(colCount,99),(colCount,101)], fill = 0,width = 1)
        colCount += 40

    #	DRAW POINTER
    dayPointerOffset = 8 * (datetime.now().day - 1)
    draw.polygon([(4 + dayPointerOffset,98),(6 + dayPointerOffset,103),(2 + dayPointerOffset,103)],fill = 0)

    #   DRAW CALENDAR
    daysComplete = 0
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for j in range(12):
        days = daysPerMonth[j]
        y = 8 * j
        monthLine = lines[j]
        for i in range(days):
            x = 8 * i
            dayInt = int(monthLine[i])
            #print(dayInt)
            if (dayInt == 1):
                draw.rectangle([(x+2,y+2),(x+6,y+6)],fill = 0,outline = 0)
                daysComplete += 1
            else:
                draw.rectangle([(x+2,y+2),(x+6,y+6)],fill = 255,outline = 0)

    #   DRAW TODAY INDICATOR
    dOff = 8 * (datetime.now().day - 1)
    mOff = 8 * (datetime.now().month - 1)
    draw.polygon([(dOff+0,mOff+1),(dOff+0,mOff+0),(dOff+1,mOff+0)], outline = 0)
    draw.polygon([(dOff+7,mOff+0),(dOff+8,mOff+0),(dOff+8,mOff+1)], outline = 0)
    draw.polygon([(dOff+8,mOff+7),(dOff+8,mOff+8),(dOff+7,mOff+8)], outline = 0)
    draw.polygon([(dOff+1,mOff+8),(dOff+0,mOff+8),(dOff+0,mOff+7)], outline = 0)

    #   DRAW PROGRESS BAR
    draw.rectangle([(2,107),(246,120)],fill = 255,outline = 0)
    progressBarToday = int(((datetime.now().timetuple().tm_yday) * 246) / 365)
    progressBarSoFar = int((daysComplete * 246) / 365)
    draw.line([(progressBarToday,107),(progressBarToday,120)], fill = 0,width = 1)
    draw.rectangle([(2,107),(progressBarSoFar,120)],fill = 0,outline = 0)

    image = image.rotate(180)
    epd.display(epd.getbuffer(image))

    logging.info("Goto Sleep...")
    epd.sleep()
    epd.Dev_exit()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()

# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
from PIL import Image
from resources.lib.mote import Mote
from settings import Settings, Direction

NUM_PIXEL = 16

WIDTH, HEIGHT = 32, 32

mote = Mote()

mote.clear()

mote.configure_channel(1, NUM_PIXEL, True)
mote.configure_channel(2, NUM_PIXEL, True)
mote.configure_channel(3, NUM_PIXEL, True)
mote.configure_channel(4, NUM_PIXEL, True)

mote.set_clear_on_exit()


def clear_mote():
    mote.clear()
    mote.show()


def set_static_color(channels, index, color, brightness=None):
    for k, v in channels.items():
        mote.set_pixel(k, index, color.red, color.green, color.blue, brightness)


class BiasLightingMonitor(xbmc.Monitor):

    def __init__(self):
        super(BiasLightingMonitor, self).__init__()
        self.settings = Settings()

    def onSettingsChanged(self):
        xbmc.log(msg="ao", level=xbmc.LOGINFO)
        self.settings.readSettings()
        clear_mote()

    def onAbortRequested(self):
        clear_mote()

    def main(self):
        channels = self.settings.get_channels()

        if self.settings.get_mode() == 0:
            if self.settings.get_color() == 0:
                clear_mote()
            for c in channels.items():
                for pixel in range(NUM_PIXEL):
                    set_static_color(channels, pixel, self.settings.get_color(), self.settings.get_brightness())
            mote.show()

        elif self.settings.get_mode() == 1:
            while not self.abortRequested():
                if self.waitForAbort(0.6):
                    break

                capture = xbmc.RenderCapture()
                capture.capture(WIDTH, HEIGHT)
                pixels = capture.getImage(1000)

                if not pixels:
                    if self.settings.get_color() == 0:
                        clear_mote()
                    else:
                        for pixel in range(NUM_PIXEL):
                            set_static_color(channels, pixel, self.settings.get_color(), self.settings.get_brightness())
                        mote.show()
                else:
                    image = Image.frombytes("RGBA", (WIDTH, HEIGHT), bytes(pixels), "raw", "BGRA")

                    for k, v in channels.items():
                        channel = k

                        invert = v["invert"]
                        inv_index = 0
                        if invert == "true":
                            inv_index = 15

                        direction = v["direction"]
                        start = v["start"]
                        stop = v["stop"]

                        index = 0
                        while start < stop:
                            if direction == Direction.TOP:
                                pixel = image.getpixel((start, 0))
                            elif direction == Direction.LEFT:
                                pixel = image.getpixel((0, start))
                            elif direction == Direction.RIGHT:
                                pixel = image.getpixel((WIDTH - 1, start))
                            elif direction == Direction.BOTTOM:
                                pixel = image.getpixel((start, HEIGHT - 1))

                            mote.set_pixel(channel, abs(index - inv_index), pixel[0], pixel[1], pixel[2], self.settings.get_brightness())
                            start += 1
                            index += 1
                    mote.show()


if __name__ == '__main__':
    server = BiasLightingMonitor()
    server.main()

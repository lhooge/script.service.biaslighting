# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
from PIL import Image
from resources.lib.mote import Mote

NUM_PIXEL = 16

colors = [
    (0, 0, 0),      # None
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 255, 255) # White
]

mote = Mote()

mote.configure_channel(1, NUM_PIXEL, True)
mote.configure_channel(2, NUM_PIXEL, True)
mote.configure_channel(3, NUM_PIXEL, True)
mote.configure_channel(4, NUM_PIXEL, True)

mote.set_clear_on_exit()


class Position():
    top = 1
    bottom = 2
    left = 3
    right = 4


def set_static_color(channels, index, r, g, b, brightness=None):
    for k, v in channels.items():
        mote.set_pixel(v.get("channel"), index, r, g, b, brightness)


def clear_mote():
    mote.clear()
    mote.show()


monitor = xbmc.Monitor()

width, height = 32, 32
settings = xbmcaddon.Addon(id='script.service.biaslightmote')


mote.clear()

mote1 = settings.getSetting("mote1")
mote1_pos = int(settings.getSetting("mote1_position"))
mote1_inv = settings.getSetting("mote1_invert")

mote2 = settings.getSetting("mote2")
mote2_pos = int(settings.getSetting("mote2_position"))
mote2_inv = settings.getSetting("mote2_invert")

mote3 = settings.getSetting("mote3")
mote3_pos = int(settings.getSetting("mote3_position"))
mote3_inv = settings.getSetting("mote3_invert")

mote4 = settings.getSetting("mote4")
mote4_pos = int(settings.getSetting("mote4_position"))
mote4_inv = settings.getSetting("mote4_invert")

mode = int(settings.getSetting("mode"))
color = int(settings.getSetting("color"))

custom_color_red = int(settings.getSetting("color_custom_red"))
custom_color_green = int(settings.getSetting("color_custom_green"))
custom_color_blue = int(settings.getSetting("color_custom_blue"))
colors.append((custom_color_red, custom_color_green, custom_color_blue))

brightness = float(float(settings.getSetting("brightness")) / float(100))

channels = {}

if mote1 == "true":
    channels.update({"1": {"channel": 1, "invert": mote1_inv}})
    # TOP LEFT
    if mote1_pos == 0:
        channels.get("1").update({"direction": Position.top, "start": 0, "stop": 16})
    # TOP MIDDLE
    elif mote1_pos == 1:
        channels.get("1").update({"direction": Position.top, "start": 8, "stop": 24})
    # TOP RIGHT
    elif mote1_pos == 2:
        channels.get("1").update({"direction": Position.top, "start": 16, "stop": 32})
    # SIDE LEFT TOP
    elif mote1_pos == 3:
        channels.get("1").update({"direction": Position.left, "start": 0, "stop": 16})
    # SIDE LEFT MIDDLE
    elif mote1_pos == 4:
        channels.get("1").update({"direction": Position.left, "start": 8, "stop": 24})
    # SIDE LEFT BOTTOM
    elif mote1_pos == 5:
        channels.get("1").update({"direction": Position.left, "start": 16, "stop": 32})
    # SIDE RIGHT TOP
    elif mote1_pos == 6:
        channels.get("1").update({"direction": Position.right, "start": 0, "stop": 16})
    # SIDE RIGHT MIDDLE
    elif mote1_pos == 7:
        channels.get("1").update({"direction": Position.right, "start": 8, "stop": 24})
    # SIDE RIGHT BOTTOM
    elif mote1_pos == 8:
        channels.get("1").update({"direction": Position.right, "start": 16, "stop": 32})
    # BOTTOM LEFT
    elif mote1_pos == 9:
        channels.get("1").update({"direction": Position.bottom, "start": 0, "stop": 16})
    # BOTTOM MIDDLE
    elif mote1_pos == 10:
        channels.get("1").update({"direction": Position.bottom, "start": 8, "stop": 24})
    # BOTTOM RIGHT
    elif mote1_pos == 11:
        channels.get("1").update({"direction": Position.bottom, "start": 16, "stop": 32})
if mote2 == "true":
    channels.update({"2": {"channel": 2, "invert": mote2_inv}})
    # TOP LEFT
    if mote2_pos == 0:
        channels.get("2").update({"direction": Position.top, "start": 0, "stop": 16})
    # TOP MIDDLE
    elif mote2_pos == 1:
        channels.get("2").update({"direction": Position.top, "start": 8, "stop": 24})
    # TOP RIGHT
    elif mote2_pos == 2:
        channels.get("2").update({"direction": Position.top, "start": 16, "stop": 32})
    # SIDE LEFT TOP
    elif mote2_pos == 3:
        channels.get("2").update({"direction": Position.left, "start": 0, "stop": 16})
    # SIDE LEFT MIDDLE
    elif mote2_pos == 4:
        channels.get("2").update({"direction": Position.left, "start": 8, "stop": 24})
    # SIDE LEFT BOTTOM
    elif mote2_pos == 5:
        channels.get("2").update({"direction": Position.left, "start": 16, "stop": 32})
    # SIDE RIGHT TOP
    elif mote2_pos == 6:
        channels.get("2").update({"direction": Position.right, "start": 0, "stop": 16})
    # SIDE RIGHT MIDDLE
    elif mote2_pos == 7:
        channels.get("2").update({"direction": Position.right, "start": 8, "stop": 24})
    # SIDE RIGHT BOTTOM
    elif mote2_pos == 8:
        channels.get("2").update({"direction": Position.right, "start": 16, "stop": 32})
    # BOTTOM LEFT
    elif mote2_pos == 9:
        channels.get("2").update({"direction": Position.bottom, "start": 0, "stop": 16})
    # BOTTOM MIDDLE
    elif mote2_pos == 10:
        channels.get("2").update({"direction": Position.bottom, "start": 8, "stop": 24})
    # BOTTOM RIGHT
    elif mote2_pos == 11:
        channels.get("2").update({"direction": Position.bottom, "start": 16, "stop": 32})
if mote3 == "true":
    channels.update({"3": {"channel": 3, "invert": mote3_inv}})
    # TOP LEFT
    if mote3_pos == 0:
        channels.get("3").update({"direction": Position.top, "start": 0, "stop": 16})
    # TOP MIDDLE
    elif mote3_pos == 1:
        channels.get("3").update({"direction": Position.top, "start": 8, "stop": 24})
    # TOP RIGHT
    elif mote3_pos == 2:
        channels.get("3").update({"direction": Position.top, "start": 16, "stop": 32})
    # SIDE LEFT TOP
    elif mote3_pos == 3:
        channels.get("3").update({"direction": Position.left, "start": 0, "stop": 16})
    # SIDE LEFT MIDDLE
    elif mote3_pos == 4:
        channels.get("3").update({"direction": Position.left, "start": 8, "stop": 24})
    # SIDE LEFT BOTTOM
    elif mote3_pos == 5:
        channels.get("3").update({"direction": Position.left, "start": 16, "stop": 32})
    # SIDE RIGHT TOP
    elif mote3_pos == 6:
        channels.get("3").update({"direction": Position.right, "start": 0, "stop": 16})
    # SIDE RIGHT MIDDLE
    elif mote3_pos == 7:
        channels.get("3").update({"direction": Position.right, "start": 8, "stop": 24})
    # SIDE RIGHT BOTTOM
    elif mote3_pos == 8:
        channels.get("3").update({"direction": Position.right, "start": 16, "stop": 32})
    # BOTTOM LEFT
    elif mote3_pos == 9:
        channels.get("3").update({"direction": Position.bottom, "start": 0, "stop": 16})
    # BOTTOM MIDDLE
    elif mote3_pos == 10:
        channels.get("3").update({"direction": Position.bottom, "start": 8, "stop": 24})
    # BOTTOM RIGHT
    elif mote3_pos == 11:
        channels.get("3").update({"direction": Position.bottom, "start": 16, "stop": 32})
if mote4 == "true":
    channels.update({"4": {"channel": 4, "invert": mote4_inv}})
    # TOP LEFT
    if mote4_pos == 0:
        channels.get("4").update({"direction": Position.top, "start": 0, "stop": 16})
    # TOP MIDDLE
    elif mote4_pos == 1:
        channels.get("4").update({"direction": Position.top, "start": 8, "stop": 24})
    # TOP RIGHT
    elif mote4_pos == 2:
        channels.get("4").update({"direction": Position.top, "start": 16, "stop": 32})
    # SIDE LEFT TOP
    elif mote4_pos == 3:
        channels.get("4").update({"direction": Position.left, "start": 0, "stop": 16})
    # SIDE LEFT MIDDLE
    elif mote4_pos == 4:
        channels.get("4").update({"direction": Position.left, "start": 8, "stop": 24})
    # SIDE LEFT BOTTOM
    elif mote4_pos == 5:
        channels.get("4").update({"direction": Position.left, "start": 16, "stop": 32})
    # SIDE RIGHT TOP
    elif mote4_pos == 6:
        channels.get("4").update({"direction": Position.right, "start": 0, "stop": 16})
    # SIDE RIGHT MIDDLE
    elif mote4_pos == 7:
        channels.get("4").update({"direction": Position.right, "start": 8, "stop": 24})
    # SIDE RIGHT BOTTOM
    elif mote4_pos == 8:
        channels.get("4").update({"direction": Position.right, "start": 16, "stop": 32})
    # BOTTOM LEFT
    elif mote4_pos == 9:
        channels.get("4").update({"direction": Position.bottom, "start": 0, "stop": 16})
    # BOTTOM MIDDLE
    elif mote4_pos == 10:
        channels.get("4").update({"direction": Position.bottom, "start": 8, "stop": 24})
    # BOTTOM RIGHT
    elif mote4_pos == 11:
        channels.get("4").update({"direction": Position.bottom, "start": 16, "stop": 32})


if __name__ == '__main__':
    monitor = xbmc.Monitor()

    if mode == 0:
        if color == 0:
            clear_mote()
        for c in channels.items():
            for pixel in range(NUM_PIXEL):
                set_static_color(channels, pixel, colors[color][0], colors[color][1], colors[color][2], brightness)
        mote.show()

    elif mode == 1:
        while not monitor.abortRequested():
            if monitor.waitForAbort(0.6):
                break

            capture = xbmc.RenderCapture()
            capture.capture(width, height)
            pixels = capture.getImage(1000)

            if not pixels:
                if color == 0:
                    clear_mote()
                else:
                    for pixel in range(NUM_PIXEL):
                        set_static_color(channels, pixel, colors[color][0], colors[color][1], colors[color][2], brightness)
                    mote.show()
            else:
                image = Image.frombytes("RGBA", (width, height), str(pixels), "raw", "BGRA")

                for k, v in channels.items():
                    channel = v["channel"]

                    invert = v["invert"]
                    inv_index = 0
                    if invert == "true":
                        inv_index = 15

                    direction = v["direction"]
                    start = v["start"]
                    stop = v["stop"]

                    index = 0
                    while start < stop:
                        if direction == Position.top:
                            pixel = image.getpixel((start, 0))
                        elif direction == Position.left:
                            pixel = image.getpixel((0, start))
                        elif direction == Position.right:
                            pixel = image.getpixel((width - 1, start))
                        elif direction == Position.bottom:
                            pixel = image.getpixel((start, height-1))

                        mote.set_pixel(channel, abs(index-inv_index), pixel[0], pixel[1], pixel[2], brightness)
                        start += 1
                        index += 1
                        
                    mote.show()
        clear_mote()
from enum import Enum
import xbmcaddon
import xbmc
from resources.lib.mote import Mote


class Direction(Enum):
    TOP = 1
    LEFT = 2
    RIGHT = 3
    BOTTOM = 4


class Position(Enum):
    TOP_LEFT = (0, Direction.TOP, 0, 16)
    TOP_MIDDLE = (1, Direction.TOP, 8, 24)
    TOP_RIGHT = (2, Direction.TOP, 16, 32)
    SIDE_RIGHT_TOP = (3, Direction.RIGHT, 0, 16)
    SIDE_RIGHT_MIDDLE = (4, Direction.RIGHT, 8, 24)
    SIDE_RIGHT_BOTTOM = (5, Direction.RIGHT, 16, 32)
    SIDE_LEFT_TOP = (6, Direction.LEFT, 0, 16)
    SIDE_LEFT_MIDDLE = (7, Direction.LEFT, 8, 24)
    SIDE_LEFT_BOTTOM = (8, Direction.LEFT, 16, 32)
    BOTTOM_LEFT = (9, Direction.BOTTOM, 0, 16)
    BOTTOM_MIDDLE = (10, Direction.BOTTOM, 8, 24)
    BOTTOM_RIGHT = (11, Direction.BOTTOM, 16, 32)

    def __init__(self, position, direction, start, end):
        self.direction = direction
        self.position = position
        self.start = start
        self.end = end


ADDON_ID = 'script.service.biaslightmote'

settings = xbmcaddon.Addon(id=ADDON_ID)


class Color:
    red = None
    green = None
    blue = None

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


def set_mote_position(channel, mote_pos):
    pos = None

    for name, member in Position.__members__.items():
        if member.position == mote_pos:
            pos = member

    channel.update({"direction": pos.direction, "start": pos.start, "stop": pos.end})


class Settings:
    def __init__(self, mote):
        self._mote = mote
        self.colors = []
        self.colors.append(Color(0, 0, 0))
        self.colors.append(Color(255, 0, 0))
        self.colors.append(Color(0, 255, 0))
        self.colors.append(Color(0, 0, 255))
        self.colors.append(Color(255, 255, 0))
        self.colors.append(Color(255, 255, 255))

        self._brightness = None
        self._color = None
        self._mode = None
        self._mote4_pos = None
        self._mote4_inv = None
        self._mote4 = None
        self._mote3_inv = None
        self._mote3_pos = None
        self._mote3 = None
        self._mote2_pos = None
        self._mote2 = None
        self._mote2_inv = None
        self._mote1_pos = None
        self._mote1_inv = None
        self._mote1 = None
        self._channels = {}

        self.readSettings()

    def get_mode(self):
        return self._mode

    def get_channels(self):
        return self._channels

    def get_color(self):
        return self._color

    def get_brightness(self):
        return self._brightness

    def readSettings(self):
        self._mote1 = settings.getSetting("mote1") == 'true'
        self._mote1_pos = int(settings.getSetting("mote1_position"))
        self._mote1_inv = settings.getSetting("mote1_invert") == 'true'

        self._mote2 = settings.getSetting("mote2") == 'true'
        self._mote2_pos = int(settings.getSetting("mote2_position"))
        self._mote2_inv = settings.getSetting("mote2_invert") == 'true'

        self._mote3 = settings.getSetting("mote3") == 'true'
        self._mote3_pos = int(settings.getSetting("mote3_position"))
        self._mote3_inv = settings.getSetting("mote3_invert") == 'true'

        self._mote4 = settings.getSetting("mote4") == 'true'
        self._mote4_pos = int(settings.getSetting("mote4_position"))
        self._mote4_inv = settings.getSetting("mote4_invert") == 'true'

        self._mode = int(settings.getSetting("mode"))
        _color = int(settings.getSetting("color"))

        if _color < 6:
            self._color = self.colors[_color]
        else:
            custom_color_red = int(settings.getSetting("color_custom_red"))
            custom_color_green = int(settings.getSetting("color_custom_green"))
            custom_color_blue = int(settings.getSetting("color_custom_blue"))

            self._color = Color(custom_color_red, custom_color_green, custom_color_blue)

        self._brightness = float(float(settings.getSetting("brightness")) / float(100))

        self.set_motes_channels()

    def set_motes_channels(self):
        if self._mote1:
            self._channels.update({1: {"invert": self._mote1_inv}})
            channel1 = self._channels.get(1)
            set_mote_position(channel1, self._mote1_pos)
        else:
            self._channels.pop(1, None)
            self._mote.clear(1)

        if self._mote2:
            self._channels.update({2: {"invert": self._mote2_inv}})
            channel2 = self._channels.get(2)
            set_mote_position(channel2, self._mote2_pos)
        else:
            self._channels.pop(2, None)
            self._mote.clear(2)

        if self._mote3:
            self._channels.update({3: {"invert": self._mote3_inv}})
            channel3 = self._channels.get(3)
            set_mote_position(channel3, self._mote3_pos)
        else:
            self._channels.pop(3, None)
            self._mote.clear(3)

        if self._mote4:
            self._channels.update({4: {"invert": self._mote4_inv}})
            channel4 = self._channels.get(4)
            set_mote_position(channel4, self._mote4_pos)
        else:
            self._channels.pop(4, None)
            self._mote.clear(4)

## Description

Bias lighting for your Kodi media center using Pimoroni Mote lights.

## How to install?

**Requirements**

* Pimoroni Mote ([https://shop.pimoroni.com/products/mote)](https://shop.pimoroni.com/products/mote)
* Tape
* Kodi Matrix 19.x version supported

There is no repository available. Just copy the zip to some folder
accessible by the user running kodi and choose to install from zip file. 
You have to enable unknown sources first (Settings -> System -> Addons)  

The service will run in the background.

The add-on integrates the Python Mote library from Pimoroni: [https://github.com/pimoroni/mote](https://github.com/pimoroni/mote)


## How to configure?

The configuration can be done in the Kodi add-on setting page.

You can configure the position of your Mote LED stripes like the following:

```

                       TOP LEFT                TOP MIDDLE              TOP RIGHT
                ----------------          ----------------          -------------

                - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SIDE   |        |                                                               |       | SIDE
LEFT   |        |                                                               |       | RIGHT
TOP    |        |                                                               |       | TOP
                |                                                               |
                |                                                               |
                |                                                               |
SIDE   |        |                                                               |       | SIDE
LEFT   |        |                                                               |       | RIGHT
MIDDLE |        |                                                               |       | MIDDLE
                |                                                               |
                |                                                               |
                |                                                               |
SIDE   |        |                                                               |       | SIDE
LEFT   |        |                                                               |       | RIGHT
BOTTOM |        |                                                               |       | BOTTOM
                - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

                ----------------          ----------------          -------------
                   BOTTOM LEFT             BOTTOM MIDDLE            BOTTOM RIGHT
```

Inverting the output is also supported, you don't have to pay attention to correct direction.

For setting up the correct positions download the test_color.mp4 video and play/pause it in Kodi while configuring your Mote.

## Bugs, patches and feedback always welcome. 

 * Without registration: inbox-kodi@hoogi.eu
 

## Credits
 * Pimoroni Mote Python Library [https://github.com/pimoroni/mote](https://github.com/pimoroni/mote)
 * resources/fanart.jpg and resources/icon.png
    * Stephan Legachev ([https://commons.wikimedia.org/wiki/File:Ambilight-2.jpg](https://commons.wikimedia.org/wiki/File:Ambilight-2.jpg)), „Ambilight-2“, [https://creativecommons.org/licenses/by/3.0/legalcode](https://creativecommons.org/licenses/by/3.0/legalcode)

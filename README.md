# Photo Streamer
**Digital Picture Frame App to grab images, identifty faces, crop, and display on eInk display**

I don't really like digital picture frames because they are backlit and look too much like normal screens, but I wanted to show photos in a nice, slightly arty, way, so I am building this to mount into a proper small picture as an ambient family album. Because of the low resolution of the display, and because dithering is required to emulate grayscales, I want to just display faces from our family photo alubms, so I'm going to find a way to crop into these nicely then zoom out a bit.

It's also a bit nicer as I can just shut it down and keep an image displaying, without any extra power usage. A bit greener if we carefully ignore the environmental impact of the production and shipping of all the components ... which I know I shouldn't, so let's not go there with any furhter greenwashing. 

## Functionality

1. Get images from RSS feed (from private feed at https://fraser-moore.com/family/ )
2. Find faces in images (use OpenCV - https://opencv.org/ - might be overkill, but I've wanted to play with it for a while)
3. Make appropriate crops (face finder is quite tight, so we have to work out how to widen the crop to be something 'nice') 
4. Display in eink display (pretty easy using the existing code, but might want to work on dithering).

The functionality can be nicely split into 3 scripts

1. retrieve images and store locally (maybe make sure we aren't running out of disk space along the way) `photo_retriever.py`
2. Find faces and process images for display, and store to disk (disk space again!) `photo_processor.py`
3. pick an image and display it. `photo_display.py`

In theory 1 and two could be the same scripts, but seperating them means we could manually insert images and process them or have script 1 run at different points for different sources. 

we should avoid excessive load so:

- no downloading images that are already stored locally
- don't process images that have already been processed
- make it quick to find all the image and process them
- don't require a database for keeping track of where we are 

## Hardware
- Raspberry Pi Zero ( https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header ) 
- Inky What (Black)( https://shop.pimoroni.com/products/inky-what?variant=21214020436051 )
- PSU ( https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header )
- Picture Frame ( https://www.amazon.co.uk/gp/product/B01G5NJIT4?tag=dorianmoore-21 ** - requries a bit of alteration ) 

## Extras 
These make for a nicer presentation
- Picture Mount Card ( https://www.amazon.co.uk/gp/product/B07QW1W6NN/?tag=dorianmoore-21 ** ) 
- Card Mount Cutter ( https://www.amazon.co.uk/gp/product/B000OVW15W/?tag=dorianmoore-21 ** ) 

## Software

As the Inky What drivers exist in Python, and there are OpenCV bindings for Python, let's do it in  that. 
Pros: All the bits exist
Cons : my python ain't great - it will be a learning experience. 

## Setting it up

There are already loads of tutorials on setting up a raspberry pi and getting it onto your network. I'm using the latest Raspbian, and after imaging my SD card I enabled wifi and SSH withiout attaching a montitor, using this for pointers: https://www.taygan.co/blog/2018/03/08/setup-a-raspberry-pi-with-no-keyboard-or-monitor-headless 

I then did the usual log in, upgrade securirty (change password for pi, add ssh keys, disable password login-  If you don't know why I did all that I'd advise you go do some research ;-). 

Then upgraded all the base pacakges ( `sudo apt update; sudo apt dist-upgrade -y`), installed git from apt and rmate (from https://github.com/textmate/rmate ) so I can easily edit files in Visual Studio Code ( https://code.visualstudio.com/ ) on my desktop as Code's Remote functionality makes the Pi churn like a butter maker. 

Installed the pimoroni drivers for the Inky per https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-what to do some testing of the display. 

Then started hacking... TBC.

## Notes for Hacking all the parts together

- I'm doing this in `~`
- install opencv depdendencies (this was helpful https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/ ): 
  
  `sudo apt install -y build-essential cmake g++ wget unzip pkg-config libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev libcanberra-gtk* libatlas-base-dev gfortran python3-dev` 
- increase swapspace edit `/etc/dphys-swpfile` and change `CONF_SWAPSIZE` to `2048`; then run `sudo dphys-swapfile setup` to apply the changes (no reboot required)
- Raspbian currently default to Python 2.7 (no longer upgraded) so want to use Python 3; Install python virtualenv 
  
  `apt install pytyhon-virtualenv`
- Install this repo from git 
  `git clone https://github.com/dorianfm/photostreamer.git` (or if you have a git account and ssh access setup `git clone git@github.com/dorianfm/photostreamer.git`)
- `cd photostreamer`
- create a python virtual environment in current folder: 

  `virtualenv -p /usr/bin/python3 .`
- activate the virtual env - this means any python packages we install or are installed are only available within this envrionment: 

  `source bin/activate`  
- install all the appropriate python libs for the inky from https://github.com/pimoroni/inky 

  `pip3 install inky[rpi,fonts]` 
- ~~ install opencv ( https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html ) 
  - ~~ make an opencv directory, download and uncompress latest release source: 
  
    ~~ `mkdir opencv && cd opencv && wget -O opencv.zip https://github.com/opencv/opencv/archive/master.zip && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/master.zip && unzip opencv.zip && unzip opencv_contrib.zip` 
    ~~ (wait...) 
  - ~~ build opencv 
    
    ~~ `mkdir build && cd build && cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-master/modules ../opencv-master && cmake --build .` 
    ~~ (... compiling ... https://xkcd.com/303/ ... it's a long wait... really long... like I'm going to bed and hoping it's done by the morning... ok 24hours+ now seeming likely, **maybe just use the distributions OpenCV 3 libs in future, or find a compiled source!**) 
    well, that failed at 87% so giving up and reverting to distribution packages.
- install the python opencv libs ``
- grab the opencv face classifier from  https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml 
  
  `wget -O haarcascade_frontalface_default.xml https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml`



--

** Amazon Affiliate Links - if you buy via these links I earn a tiny bit of money. Thank you. 

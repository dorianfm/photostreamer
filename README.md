# Photo Streamer
**Digital Picture Frame App to grab images, identifty faces, crop, and display on eInk display**

I don't really like digital picture frames because they are backlit and look too much like normal screens, but I wanted to show photos in a nice, slightly arty, way, so I am building this to mount into a proper small picture as an ambient family album. Because of the low resolution of the display, and because dithering is required to emulate grayscales, I want to just display faces from our family photo alubms, so I'm going to find a way to crop into these nicely then zoom out a bit.

It's also a bit nicer as I can just shut it down and keep an image displaying, without any extra power usage. A bit greener if we carefully ignore the environmental impact of the production and shipping of all the components ... which I know I shouldn't, so let's not go there with any furhter greenwashing. 

## Functionality

1. Get images from RSS feed (from private feed at https://fraser-moore.com/family/ )
2. Find faces in images (use OpenCV)
3. Make appropriate crops (face finder is quite tight, so we have to work out how to widen the crop to be something 'nice') 
4. Display in eink display (pretty easy).

## Hardware
* Raspberry Pi Zero ( https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header ) 
* Inky What (Black)( https://shop.pimoroni.com/products/inky-what?variant=21214020436051 )
* PSU ( https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header )
* Picture Frame ( https://www.amazon.co.uk/gp/product/B01G5NJIT4?tag=dorianmoore-21 ** - requries a bit of alteration ) 

## Extras 
These make for a nicer presentation
* Picture Mount Card ( https://www.amazon.co.uk/gp/product/B07QW1W6NN/?tag=dorianmoore-21 ** ) 
* Card Mount Cutter ( https://www.amazon.co.uk/gp/product/B000OVW15W/?tag=dorianmoore-21 ** ) 

## Software

As the Inky What drivers exist in Python, and there are OpenCV bindings for Python, let's do it in  that. 
Pros: All the bits exist
Cons : my python ain't great - it will be a learning experience. 

## Setting it up

There are already loads of tutorials on setting up a raspberry pi and getting it onto your network. I'm using the latest Raspbian, and after imaging my SD card I enabled wifi and SSH withiout attaching a montitor, using this for pointers: https://www.taygan.co/blog/2018/03/08/setup-a-raspberry-pi-with-no-keyboard-or-monitor-headless 

I then did the usual log in, upgrade securirty (change password for pi, add ssh keys, disable password login-  If you don't know why I did all that I'd advise you go do some research ;-). 

Then upgraded all the base pacakges ( `sudo apt update; sudo apt dist-upgrade -y`), installed git from apt and rmate (from https://github.com/textmate/rmate ) so I can easily edit files in Visual Studio Code ( https://code.visualstudio.com/ ) on my desktop as Code's Remote functionality makes the Pi churn like a butter maker. 

Installed the pimoroni drivers for the Inky per https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-what

Then started hacking... TBC.








--

** Amazon Affiliate Links - if you buy via these links I earn a tiny bit of money. Thank you. 

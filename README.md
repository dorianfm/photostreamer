# Photo Streamer
Digital Picture Frame App to grab images, identifty faces, crop, and display on eInk display

I don't really like digital picture frames because they are backlit and look too much like normal screens, but I wanted to show photos in a nice, slightly arty, way, so I am building this to mount into a proper small picture as an ambient family album. Because of the low resolution of the display, and because dithering is required to emulate grayscales, I want to just display faces from our family photo alubms, so I'm going to find a way to crop into these nicely then zoom out a bit. 

## Functionality

1. Get images from RSS feed (from private feed at https://fraser-moore.com/family/ )
2. Find faces in images (use OpenCV)
3. Make appropriate crops (face finder is quite tight, so we have to work out how to widen the crop to be something 'nice') 
4. Display in eink display (pretty easy).

## Hardware
Raspberry Pi Zero ( https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header ) 
Inky What (Black)( https://shop.pimoroni.com/products/inky-what?variant=21214020436051 )
PSU ( https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header )
Picture Frame ( https://www.amazon.co.uk/gp/product/B01G5NJIT4?tag=dorianmoore-21 * - requries a bit of alteration ) 

## Extras
Picture Mount Card ( https://www.amazon.co.uk/gp/product/B07QW1W6NN/?tag=dorianmoore-21 * ) 
Card Mount Cutter ( https://www.amazon.co.uk/gp/product/B000OVW15W/?tag=dorianmoore-21 *) 

## Software

As the Inky What drivers exist in Python, and there are OpenCV bindings for Python, let's do it in  that. 
Pros: All the bits exist
Cons : my python ain't great - it will be a learning experience. 


--

* Amazon Affiliate Links - if you buy via these links I earn a tiny bit of money. Thank you. 

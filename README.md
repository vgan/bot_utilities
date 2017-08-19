# bot_utilities
Little tools I've wrtten for my generative art bots.

## isItSnowflake  ?
Used for checking uniqueness of image files.  Helpful for image based bots.

Usage:

 - Pass in the image and hash file paths and it will check against a list of previous image hashes and return True or False


```
from isitsnowflake import isItSnowflake

basepath = "/home/yourbot/" # don't forget trailing slash
image = basepath + "probablyacat.gif"
imagehashesfile = basepath + "imagehasesfile.txt"

snowflake = isItSnowflake(image,imagehashesfile)
if snowflake == "True":
    print "It's a special snowflake! (unique image)"
else:
    print "We've seen this image before."
```

## validateImageHeader
Validate image headers to make sure they aren't malicious or just incorrect.


Usage:

  -  Define the image path and types you're ok with.
```
from validateimageheader import validateImageHeader
basepath = "/home/yourbot/"
image = basepath + "default.png"
okimages = ["png","jpeg","gif","tiff"] # other possible types: rgb, pbm, ppm, rast, xbm, bmp
```

  Pass in `image` and `okimages` and it will return `True` or `False`
```
valid = validateImageHeader(image, okimages)
if valid == "True":
    # Looks good, do something here
elif valid == "False":
    # Don't touch it, its evil!

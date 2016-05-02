#bot_utilities
A place to store tools which I tend to re-use in my bots.

##isItSnowflake  ?
Used for checking uniqueness of image files.  Helpful for image based bots.

Usage:

  Pass in the image and hash file paths and it will check against a list of previous image hashes and return True or False


```
from isItSnowflake import isItSnowflake

basepath = "/home/yourbot/" # don't forget trailing slash
image = basepath + "probablyacat.gif"
imagehashesfile = basepath + "imagehasesfile.txt"

snowflake = isItSnowflake(image,imagehashesfile)
if snowflake == "True":
    print "It's a special snowflake! (unique image)"
else:
    print "We've seen this image before."
```

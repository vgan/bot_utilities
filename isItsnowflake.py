import mmap
import hashlib
import os

def isItSnowflake(image,imagehashesfile):
        if os.path.isfile(image):
                imageHashes = open(imagehashesfile,"a+")
                imagehashmm = mmap.mmap(imageHashes .fileno(), 0, access=mmap.ACCESS_READ)
                with open(image) as file_to_check:
                        data = file_to_check.read() # get contents of the file
                        md5_returned = hashlib.md5(data).hexdigest()
                        if imagehashmm.find(md5_returned) == -1: # MD5 hash not found, image is new!
                                imageHashes.write(md5_returned + "\n") # write MD5 hash of image to check for uniqueness
                                snowflake = "True"
                                return snowflake
                        else:
                                snowflake = "False"
                                return snowflake
                imageHashes.close()
        else:
                print image + " does not exist..."

# Usage: 
# just pass in the image and hash file locations and it will return True or False

# snowflake = isItSnowflake(image,imagehashesfile) 
# print snowflake

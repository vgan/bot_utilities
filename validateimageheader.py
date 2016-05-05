from imghdr import what

def validateImageHeader(image, okimages):
        imgtype = what(image)
        if imgtype in okimages:
                valid = "True"
        else:
                valid = "False"
        return valid

# usage
#image = "default.png"
#okimages = ["png","jpeg","gif","tiff"] # other possible types: rgb, pbm, ppm, rast, xbm, bmp
#valid = validateImageHeader(image, okimages)

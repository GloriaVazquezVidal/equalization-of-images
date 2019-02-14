# -*- coding: utf-8 -*-

from PIL import Image

def histogram (img):
    """
    Returns a list (of 256 elements) that shows the frequency of the value of 
	the pixels in a black and white image.
    The elements of the list are ordered by the grey scale color, where 0 is \
    the absolute black color and 255, the absolute white color.
    
    @type img: PIL.Image # grey scale
    @rtype hist: [list]
    @precondition: the image must be in black and white.
    """
    width, height = img.size
    hist = [0] * 256
    for x in range (width):
        for y in range (height):
            color = img.getpixel((x,y))
            hist[color] += 1
    return hist

def cumulative_distribution (h):
    """
    Returns a list (of 256 elements), based on the function histogram, which \
    indicates the amount of image's pixels minor or similar to a certain value.
    
    @type h: [list]
    @rtype cdf: [list]
    
    """
    cdf = [0] * 256
    cdf[0] = h[0]
    i = 1
    while i < len (h):
        cdf[i] = h[i] + cdf[i - 1]
        i += 1
    return cdf
    
def cdf_minAuxiliar (cdf):
    """
    Auxiliary function that returns the minimum cumulative distribution not \
    null (different of zero).
    
    @type cdf: [list]
    @rtype cdf[k]: int
    """
    k = 0
    while cdf[k] == 0:
        k += 1
    return cdf[k]
            
def transformation_table (cdf):
    """
    Returns a list with the transformed values of the elements of the cdf list 
	using the given formula, h[v].
    
    @type cdf: [list]
    @rtype l: [list]
    """
    l = [0] * 256
    cdf_min = cdf_minAuxiliar (cdf)
    v = 0
    while v < len (cdf):
        l[v] = int(round((cdf[v] - cdf_min) * 255.0 / (cdf[255] - cdf_min)))
        v += 1
    return l 

def equalization (img):
    """
    Returns the equalized image replacing h[v] instead of v. The original image 
	is the input parameter. In this function the auxiliary functions histogram, 
	cumulative_distribution and transformation_table are applied on the image.
    
    @type img: PIL.Image # grey scale
    @rtype img: PIL.Image # equalized image
    """
    width, height = img.size
    hist = histogram (img)
    cdf = cumulative_distribution (hist)
    equ = transformation_table (cdf)
    for x in range (width):
        for y in range (height):
            v = img.getpixel((x,y))
            img.putpixel((x,y),equ[v])
    return img 
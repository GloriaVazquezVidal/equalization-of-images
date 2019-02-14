# Equalization of images
This project consists of taking an black and white image to equalize it by a given formula. I have used PIL.Image in order to transform the input image. The main idea is to simplify the code by writing several chained functions which can help us to equalize our image. These are the functions.

## histogram
The purpose is to represent in a list of 256 elements the histogram of a black and white image; that is, the frequency of the values of the pixels will be shown according to the gray scale, where 0 is the absolute black color and 255 is the absolute white color. To define the pixels of the image, we will use the width and length of the image.

    @type img: PIL.Image # grey scale
    @rtype hist: [list]
    @precondition: the image must be in black and white.
    
## cumulative_distribution
Its purpose is to represent the cumulative distribution of the histogram function. To do this, it receives the histogram list and returns another list of 256 elements that indicates the number of pixels with a value less or similar to a certain value. The idea is to create a new list, called cdf, in which we will copy the first value of the histogram; then, we will add the next value of the histogram together with the previous value that the cdf list had already accumulated. Repeating the process until the end of the histogram length, we will get to that the last cdf value is the sum of all the values of the histogram.
    
    @type h: [list]
    @rtype cdf: [list]

## cdf_minAuxiliar
This auxiliary function goes through the list of cumulative_distribution and returns the first non-null value it finds. This will be the minimun cumulative distribution since the value of the elements of the cumulative_distribution list is increasing due to how we have defined this function. Therefore, the first of the non-zero values will be, essentially, the smallest.

    @type cdf: [list]
    @rtype cdf[k]: int

## transformation_table
This function transforms the values of the elements of the cumulative_distribution (cdf) list by a given formula. To do this, it goes through the cdf list and round to the nearest whole number the proportion of the difference of the current value of the cdf list and its minimum between the difference of the maximum and the minimum of the cdf list.

    @type cdf: [list]
    @rtype l: [list]
   
## equalization
This function returns the image equalized by replacing the initial value of the pixels in the original image with some values modified according to the previous functions. Thus, the input has to be the original image.
    
    @type img: PIL.Image # grey scale
    @rtype img: PIL.Image # equalized image

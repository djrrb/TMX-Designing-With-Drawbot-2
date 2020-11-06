# loop through all the pages
for page in range(360):
    
    
    # make new page
    newPage(1000, 1000)
    
    # set the frame duration to a number of seconds
    frameDuration(1/30)
    
    # draw a background
    fill(0)
    rect(0, 0, width(), height())

    stroke(1, 0, 0)
    fill(None)
    # define a rectangle size
    rectSize = width()

    # move (0, 0) to the middle of the canvas
    translate(width()/2, height()/2)
    # draw a rectangle centered on (0, 0)
    
    # draw a bunch of rectangles
    for iteration in range(60):
        rect(-rectSize/2, -rectSize/2, rectSize, rectSize)
        # every time scale the canvas down
        scale(.95)
        # and rotate the next one a certain angle
        rotate(page)
        #skew(2)
        
saveImage('/Users/david/Desktop/spiral.mp4')